
////// prepare data
cd "C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final"
use matched, clear
cd "C:/Users/fx236/Documents/AME_git/AME/code/court_cases_codes/stata_exports/yearly without co2"

//cd "C:/Users/fx236/Documents/AME_git/AME/code/court_cases_codes/stata_exports/full data"
//keep if city=="NEW YORK"
set matsize 11000 //set max number of vars
bys date city: gen id=_n //for jedes unique date+city ab 1 hochzählen
egen idtime=group(id date) //group= jedes unique id+date gleicher index. idtime is only used for a ttest once
g year=year(date) // welches jahr (2000 bis 2004)
g month=month(date) // wievielter monat (1 bis 12)
g week=week(date) // welche kq (1 bis 52)

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
global pollutants ozone pm25 //co
bys city week month year:egen meantemp=mean(temp6t4) //for jedes unique city+week+month+year calculate mean of tem6t4
// i do this seperately: maybe I should exclude this?
foreach var in $weather6t4{
drop if `var'==.
}


///////// 2000
preserve
keep if year == 2000
**TABLE 1 and Figure 5
qui xi:  reg res  $weather6t4 $pollutants $dummies , vce (cluster cm)
estimate store base_6t4_2000

///////// 2001
restore 
preserve
keep if year == 2001
**TABLE 1 and Figure 5
qui xi:  reg res  $weather6t4 $pollutants $dummies , vce (cluster cm)
estimate store base_6t4_2001

///////// 2002
restore
preserve
keep if year == 2002
**TABLE 1 and Figure 5
// I assume qui means quiet, and xi is something with dummies? "esttab" returns stored result
qui xi:  reg res  $weather6t4 $pollutants $dummies , vce (cluster cm)
estimate store base_6t4_2002

///////// 2003
restore
preserve
keep if year == 2003
**TABLE 1 and Figure 5
qui xi:  reg res  $weather6t4 $pollutants $dummies , vce (cluster cm)
estimate store base_6t4_2003


///////// 2004
restore
preserve
keep if year == 2004
**TABLE 1 and Figure 5
qui xi:  reg res  $weather6t4 $pollutants $dummies , vce (cluster cm)
estimate store base_6t4_2004


////////// combine all results

esttab base_6t4_2000 base_6t4_2001 base_6t4_2002 base_6t4_2003 base_6t4_2004  using years.tex, replace keep($weather6t4 $pollutants temp6t410 ) se brackets  star(* 0.10 ** 0.05 *** 0.01) ///
mtitles("2000" "2001" "2002" "2003" "2004")	
