cd "C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final"


use matched, clear


cd "C:/Users/fx236/Documents/AME_git/AME/code/court_cases_codes/stata_exports/full data without co2"

set matsize 11000 //set max number of vars

bys date city: gen id=_n //for jedes unique date+city ab 1 hochzählen
egen idtime=group(id date) //group= jedes unique id+date gleicher index. idtime is only used for a ttest once


g year=year(date) // welches jahr (2000 bis 2004)
g month=month(date) // wievielter monat (1 bis 12)
g week=week(date) // welche kq (1 bis 52)


//keep if year == 2001

g yearmonth=string(year) + string(month)
g cityweek=string(week) + city // zb: 1LAS VEGAS
g cityyear= city + string(year) // LAS VEGAS2000
g citymonth= city + string(month) // LAS VEGAS1
g yearweek= string(week) + string(year) // 12000

g cityyearmonth= city + string(month) + string(year) //LAS VEGAS12000 also city-month-year tatsächlich
encode cityyearmonth, g(cym) // encode turs str into long, which is numeric with string labels

g judgemonth=ij_name + string(month) //ij_name is judge id // 721
encode judgemonth, g(jm) //judgemonth as integer

g judgemonthyear=ij_name + string(year) +string(month) // 7220001
encode judgemonthyear, g(jym) //

encode yearmonth, g(ym) //all only encode
encode cityweek, g(cw) //
encode cityyear, g(cy) //
encode citymonth, g(cm) //
encode yearweek, g(yw) //


g dayofweek=dow(date) //0=Sunday,...,6=Saturday

encode city, g(ct) //3 encodes
encode c_asy_type, g(type) //type of asylumn, ka was I,E usw heißt
encode nat_name, g (nati)

global temp l2avgtemp l3avgtemp lavgtemp  temp6t4  le1avgtemp le2avgtemp le3avgtemp le3temp6t4  le2temp6t4  letemp6t4 ltemp6t4 l2temp6t4 l3temp6t4 avgtemp yearaftertemp gtemp yeartemp heat //create list of vars

foreach var in $temp{ //with each element create new var which is /1000 
  
g `var'10=`var'/1000
}

global weatherdaily avgtemp10 skycover pressureavgsealevel windspeed precipitationwaterequiv avgdewpt //create more lists
global weatherdailyt  skycover avgdewpt pressureavgsealevel windspeed precipitationwaterequiv
global weathertemp  press6t4 dew6t4 prcp6t4 wind6t4 skycover
global weather6t4  temp6t410 press6t4 dew6t4 prcp6t4 wind6t4 skycover 
global heat heat10 press6t4  prcp6t4 wind6t4 skycover
global dailyheat dailyheat skycover pressureavgsealevel windspeed precipitationwaterequiv 
global dummies i.dayofweek  i.nati i.type i.year i.cm i.chair
//global pollutants ozone co pm25
global pollutants ozone pm25 //co excluded!



bys city week month year:egen meantemp=mean(temp6t4) //for jedes unique city+week+month+year calculate mean of tem6t4

// i do this seperately: maybe I should exclude this?
foreach var in $weather6t4{
drop if `var'==.
}
// i dp this seperately
foreach var in $pollutants{
drop if `var'==.
}
	


**TABLE 1 and Figure 5

// I assume qui means quiet, and xi is something with dummies? "esttab" returns stored result
qui xi: reg res  $weatherdaily $pollutants $dummies , vce (cluster cm)
estimate store base_daily

g deviation=temp6t4-meantemp //self exp.	

qui xi: reg res deviation $weathertemp $pollutants $dummies , cluster (cm)
estimate store base_dev
	
	
qui xi:  reg res  $weather6t4 $pollutants $dummies , vce (cluster cm)
estimate store base_6t4

test temp6t410=press6t4=dew6t4=prcp6t4=wind6t4=skycove=0 // no var ceation


qui xi: reg res ltemp6t410 $weather6t4  $dummies $pollutants , vce (cluster cm)
estimate store lag_6t4



qui xi: reg res  letemp6t410  $weather6t4  $dummies $pollutants , vce (cluster cm)
estimate store lead_6t4




qui xi: reg res   ltemp6t410 temp6t410  letemp6t410 press6t4 dew6t4 prcp6t4 wind6t4 skycover $dummies $pollutants , vce (cluster cm)
estimate store all_6t4_one



**TABLE 2
//ssc install estout needed for esttab
esttab base_6t4 lag_6t4 lead_6t4  all_6t4_one using base_6t4.tex,replace keep(ltemp6t410 temp6t410  letemp6t410 ) se brackets  star(* 0.10 ** 0.05 *** 0.01) ///
	mtitles("base"  "1-Daylag" "1-Day lead"  "all")	

**FIGURE 5	
	
qui xi: reg res   l3avgtemp10 l2avgtemp10 lavgtemp10  temp6t410  le1avgtemp10 le2avgtemp10 le3avgtemp10  press6t4 dew6t4 prcp6t4 wind6t4  $dummies $pollutants , vce (cluster cm)
estimate store all_6t4

coefplot, keep(l3avgtemp10 l2avgtemp10 lavgtemp10  temp6t410  le1avgtemp10 le2avgtemp10 le3avgtemp10 ) vertical yline(0) ci(95) scheme(s1mono) saving(timing, replace)
	
**TABLE	A1

esttab base_6t4 lag_6t4 lead_6t4  all_6t4_one using fullbase_6t4.tex,replace keep($weather6t4 $pollutants ltemp6t410 temp6t410  letemp6t410 ) se brackets star(* 0.10 ** 0.05 *** 0.01) ///
	mtitles("base"  "1-Daylag" "1-Day lead"  "all")	

	

****************************
**TABLE 3
****************************

drop if type==.	//drop na
drop if nati==. //drop na
	
qui reg res  $weather6t4 $pollutants  , vce (cluster cm)
estimate store base_6t4_nothing

qui reg res  $weather6t4 $pollutants $dummies 
estimate store base_1

qui reg res  $weather6t4 $pollutants 
estimate store base_2


suest base_1 base_2 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_2_mean]temp6t4

	
qui reg res  $weather6t4 $pollutants i.nati , cluster (cm)
estimate store base_6t4_nati

	
qui reg res  $weather6t4 $pollutants  i.dayofweek   i.nati  , cluster (cm)
estimate store base_6t4_nati_dow

qui reg res  $weather6t4 $pollutants  i.nati i.type i.dayofweek , cluster (cm)
estimate store base_6t4_nati_dow_type

qui reg res  $weather6t4 $pollutants  i.nati i.type i.dayofweek i.chair , cluster (cm)
estimate store base_6t4_nati_dow_type_j

qui reg res  $weather6t4 $pollutants  i.nati i.type i.dayofweek i.chair i.cm , cluster (cm)
estimate store base_6t4_nati_dow_type_j_cm

qui reg res  $weather6t4 $pollutants i.nati i.type i.chair i.dayofweek i.ct i.ym , cluster (cm)
estimate store base_6t4_city_ym

	
qui reg res  $weather6t4 $pollutants i.nati i.type  i.chair i.dayofweek i.cym  , cluster (cm)
estimate store base_6t4_cym

	
qui reg res  $weather6t4 $pollutants i.nati i.type i.chair i.dayofweek i.jm i.ct i.year , cluster (cm)
estimate store base_6t4_jm_ct_year

qui reg res  $weather6t4 $pollutants i.nati i.type i.chair i.cm i.year i.date, cluster (cm)
estimate store base_6t4_date


esttab base_6t4_nothing base_6t4_nati base_6t4_nati_dow base_6t4_nati_dow_type base_6t4_nati_dow_type_j base_6t4_nati_dow_type_j_cm base_6t4_city_ym base_6t4_cym  base_6t4_jm_ct_year base_6t4_date base_6t4 using FEmoving.tex,replace keep(temp6t410 ) se brackets star(* 0.10 ** 0.05 *** 0.01) ///
	mtitles("nothing" "nat" "dow" "type" "judge" "cm" "city/ym" "cym"  "jm/c/y" "date" "base" )	

