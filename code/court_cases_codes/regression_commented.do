cd "C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final"


use matched, clear


cd "C:/Users/fx236/Documents/AME/code/court_cases_codes/stata_exports"

set matsize 11000 //set max number of vars

bys date city: gen id=_n //for jedes unique date+city ab 1 hochzählen
egen idtime=group(id date) //group= jedes unique id+date gleicher index. idtime is only used for a ttest once


g year=year(date) // welches jahr (2000 bis 2004)
g month=month(date) // wievielter monat (1 bis 12)
g week=week(date) // welche kq (1 bis 52)

g yearmonth=string(year) + string(month)//zb20001 oder 200301 (eine 0 fehlt)
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
global pollutants ozone co pm25



bys city week month year:egen meantemp=mean(temp6t4) //for jedes unique city+week+month+year calculate mean of tem6t4

// i dp this seperately
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

test temp6t410=press6t4=dew6t4=prcp6t4=wind6t4=skycove=0


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

drop if type==.	
drop if nati==.
	
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

	

	
	
*********************
**CITY AND SEASON	
*********************


tabulate city, g(ct_dummy)

forvalues i=1(1) 43{
g intraction`i'=avgtemp*ct_dummy`i'
}

forvalues i=1(1) 43{
g intractionblock`i'=temp6t4*ct_dummy`i'
}

drop intractionblock30

qui reg res intractionblock* $weather6t4 $pollutants $dummies , cluster (cm)
estimate store intraction


qui reg res  $weather6t4 $pollutants $dummies if winter==0, vce (cluster cm)
estimate store winter

****************************
**rain and temp intraction 
****************************	
	
	
g raintemp=temp6t4*skycover
	
	
reg res  $weather6t4 raintemp $pollutants $dummies , cluster (cm)
estimate store raintemp	


**TABLE 4

esttab base_6t4 base_daily base_dev intraction winter raintemp	 using city.tex,replace keep(temp6t410 avgtemp10 deviation raintemp ) se brackets star(* 0.10 ** 0.05 *** 0.01) ///
	mtitles("pref" "daily"  "deviation" "intarction" "winter" "raintemp")	

****************************
**MALE AND FEMALE 
****************************
	
g female=0
replace female=1 if gender=="female"
	
quietly reg res  $weather6t4  $dummies $pollutants if female==1 , vce (cluster cm)
estimate store female

quietly reg res  $weather6t4  $dummies $pollutants if female==0 , vce (cluster cm)
estimate store male

**TABLE A.2
	
esttab  female male using gender.tex,replace keep(temp6t410) se brackets star(* 0.10 ** 0.05 *** 0.01) ///
	mtitles("female"  "male")	

quietly reg res  $weather6t4 $pollutants $dummies  if female==0 	
estimate store male

qui reg res  $weather6t4  $pollutants if female==1 
estimate store female

suest female male, vce (cluster cm)

test ([female_mean]temp6t4 = [male_mean]temp6t4)

*******************************
*** ALTERNATOVE SEs: TABLE 	A4:
*******************************
	
qui reg res  $weather6t4 $pollutants $dummies , vce (cluster yw)
estimate store base_cw

qui reg res  $weather6t4 $pollutants $dummies , vce (cluster ym)
estimate store base_ym

qui reg res  $weather6t4 $pollutants $dummies , vce (cluster cy)
estimate store base_cy

qui reg res  $weather6t4 $pollutants $dummies , vce (cluster city)
estimate store base_city

qui reg res  $weather6t4 $pollutants $dummies , vce (robust)
estimate store base_white	

qui reg res  $weather6t4 $pollutants $dummies , vce (cluster chair)
estimate store base_judge	

qui reg res  $weather6t4 $pollutants $dummies , vce (cluster jm)
estimate store base_judgemonth

ivreg2 res  $weather6t4 $pollutants $dummies , cluster (city week) 
estimate store base_twoway

tsset ct idtime
xi: newey2 res  $weather6t4 $pollutants $dummies, lag(3) force
estimate store neweywest	
	
esttab base_cw base_ym base_cy base_city base_white base_judge  base_judgemonth  using standarderror.tex,replace keep(temp6t410) se brackets star(* 0.10 ** 0.05 *** 0.01) ///
	mtitles("cw"  "ym" "cy" "city" "white" "judge"  "judgemonth" )
	
**************************	
***TABLE 6
***************************

replace yearaftertemp=temp6t4 if yearaftertemp==.
replace yeartemp=temp6t4 if yeartemp==.


	
qui reg res yearaftertemp press6t4 dew6t4 prcp6t4 wind6t4 $pollutants $dummies , vce (cluster cm)
estimate store placebo_after

qui reg res yeartemp press6t4 dew6t4 prcp6t4 wind6t4 $pollutants $dummies , vce (cluster cm)	
estimate store placebo_before

qui reg res gtemp press6t4 dew6t4 prcp6t4 wind6t4 $pollutants $dummies , vce (cluster cm)	
estimate store placebo_fur

esttab base_6t4 placebo_after placebo_before placebo_fur using placebo.tex,replace keep(temp6t410 yearaftertemp yeartemp gtemp) se brackets star(* 0.10 ** 0.05 *** 0.01)  ///
	mtitles("pref" "after"  "before" "furthest")
	
	
*****************************
***ROBUSTNESS
*****************************	

quietly reg res   $weather6t4  $dummies , vce (cluster cm)
estimate store nopollution

g ca=0
replace ca=1 if city=="SAN PEDRO" | city=="SAN FRANCISCO" | city=="SAN DIEGO" | city=="LOS ANGELES" |city=="LAS VEGAS" | city=="LANCASTER" |city=="IMPERIAL"


quietly reg res  $weather6t4  $dummies $pollutants if ca==0 , vce (cluster cm)
estimate store noca

quietly reg res  $weather6t4  $dummies $pollutants if skycover<0.1 , vce (cluster cm)
estimate store clearsky

quietly reg res  $weather6t4  $dummies $pollutants if precipitationwaterequiv==0 , vce (cluster cm)
estimate store norain

quietly reg res  $weather6t4  $dummies $pollutants if precipitationwaterequiv==0 & lprcp==0, vce (cluster cm)
estimate store norain2


qui reg res  $heat $pollutants $dummies, cluster (cm)
estimate store heat_6t4


qui reg res  $heat   $dummies $pollutants if heat10>=0.075 , cluster (cm)
estimate store heat_75


bys ij_name: egen rate=mean(res)

quietly reg res  $weather6t4  $dummies $pollutants if rate>0.081 & rate<=0.22 , vce (cluster cm)
estimate store quartile

quietly reg res  $weather6t4  $dummies $pollutants if rate>0.047 & rate<=0.31 , vce (cluster cm)
estimate store decile


***TABLE 5
	
esttab base_6t4  nopollution noca clearsky norain norain2  heat_6t4 heat_75 quartile decile	 using robustness.tex,replace keep(temp6t410 heat10) se brackets star(* 0.10 ** 0.05 *** 0.01)  ///
	mtitles("prefferd" "pollution"  "CA"  "clear" "rain" "rain2"  "heat" "heat>75" "qurtile" "decile" )	
	
	

	
*****************************
***Nonlinear Results: 
*****************************	
	

recode avgtemp (min/20=20)(20/25=25) (25/30=30) (30/35=35) (35/40=40)(40/45=45)(45/50=50) (50/55=55) (55/60=60) (60/65=65) (65/70=70) (70/75=75) (75/80=80) (80/85=85) (85/max=max), gen(t2aveb)
table t2aveb, c(min avgtemp max avgtemp count avgtemp)
tab t2aveb, gen(t2avebdum)
drop t2avebdum8

recode temp6t4 (min/20=20) (20/25=25) (25/30=30) (30/35=35) (35/40=40) (40/45=45)(45/50=50) (50/55=55) (55/60=60) (60/65=65) (65/70=70) (70/75=75) (75/80=80) (80/85=85) (85/max=max), gen(t6aveb)
table t6aveb, c(min temp6t4 max temp6t4 count temp6t4)
tab t6aveb, gen(t6avebdum)
drop t6avebdum8

**FOR BARCHART GRAPH
*recode temp6t4 (min/10=10) (10/20=20) (20/30=30) (30/40=40) (40/50=50) (50/60=60)(60/70=70) (70/80=80) (80/90=90) (90/max=max), gen(t6aveb)
*table t6aveb, c(min temp6t4 max temp6t4 count temp6t4)
*tab t6aveb, gen(t6avebdum)



recode dew6t4 (min/20=20) (20/25=25) (25/30=30) (30/35=35) (35/40=40) (40/45=45)(45/50=50) (50/55=55) (55/60=60) (60/65=65) (65/70=70) (70/75=75) (75/80=80) (80/85=85) (85/max=max), gen(rh6aveb)
table rh6aveb, c(min dew6t4 max dew6t4 count dew6t4)
tab rh6aveb, gen(rh6avebdum)
drop rh6avebdum8

recode avgdewpt (min/20=20)(20/25=25) (25/30=30) (30/35=35) (35/40=40) (40/45=45) (45/50=50) (50/55=55) (55/60=60) (60/65=65) (65/70=70) (70/75=75) (75/80=80) (80/85=85) (85/max=max), gen(rh2aveb)
table rh2aveb, c(min avgdewpt max avgdewpt count avgdewpt)
tab rh2aveb, gen(rh2avebdum)
drop rh2avebdum8


recode heat (min/20=20)(20/25=25) (25/30=30) (30/35=35) (35/40=40)(40/45=45)(45/50=50) (50/55=55) (55/60=60) (60/65=65) (65/70=70) (70/75=75) (75/80=80) (80/85=85) (85/90=90)  (90/95=95)  (95/max=max) , gen(heat2aveb)
table heat2aveb, c(min heat max heat count heat)
tab heat2aveb, gen(ht2avebdum)
drop ht2avebdum8

global nweather6t4 t6avebdum* rh6avebdum* press6t4 prcp6t4 wind6t4 skycover
global nweather t2avebdum* rh2avebdum* skycover pressureavgsealevel windspeed precipitationwaterequiv
global heatweather ht2avebdum* press6t4 prcp6t4 wind6t4 skycover 



quietly  reg res $nweather6t4 $pollutants $dummies, vce (cluster cm)
estimate store bin6t4

**FIGURE 6

coefplot, keep(t6avebdum*) vertical yline(0) ci(95) scheme(s1mono) saving(nonlineartemp10, replace)



quietly  reg res $heatweather $pollutants $dummies, vce (cluster cm)
estimate store heat

coefplot, keep(ht2avebdum*) vertical yline(0) ci(95) scheme(s1mono) saving(heat, replace)



drop ht2avebdum11
quietly  reg res $heatweather $pollutants $dummies if heat>65, vce (cluster cm)
estimate store heat65

***FIGURE 7

coefplot, keep(ht2avebdum*) vertical yline(0) ci(95) scheme(s1mono) saving(heat65, replace)

**TABLE A.3

esttab bin6t4 heat heat65 using nonlinear.tex,replace keep( t6avebdum* ht2avebdum* ) se brackets star(* 0.10 ** 0.05 *** 0.01) ///
	mtitles("temp"  "heat" "heat75")


****************************
**Randomization test 
****************************


g typeofap=0
replace typeofap=1 if  c_asy_type=="E"


g middleast=0
replace middleast=1 if (nat_name=="BAHRAIN" | nat_name=="CYPRUS" | nat_name=="EGYPT" | nat_name=="IRAN" | nat_name=="IRAQ" | nat_name=="ISRAEL"| nat_name=="JORDAN" | nat_name=="KUWAIT"| nat_name=="LEBANON" | nat_name=="OMAN" | nat_name=="PALESTINE" | nat_name=="QATAR" | nat_name=="SAUDI ARABIA" | nat_name=="SYRIA" | nat_name=="TURKEY" | nat_name=="UNITED ARAB EMIRATES" | nat_name=="YEMEN")

qui reg typeofap $weatherdaily  $pollutants i.dayofweek  i.nati i.year i.cm i.chair  , cluster (cm)
estimate store random_type


qui reg middleast $weatherdaily  $pollutants i.dayofweek  i.type i.year i.cm i.chair  , cluster (cm)
estimate store random_national


qui reg female $weatherdaily  $pollutants i.dayofweek  i.type i.year i.cm i.nati  , cluster (cm)
estimate store random_chair

**TABLE A.5

esttab random_type random_national random_chair using random.tex,replace keep(avgtemp10) se brackets star(* 0.10 ** 0.05 *** 0.01) ///
	mtitles("type"  "national" "chair")


*****FIGURE A.1	
	
	
qui reg typeofap l3avgtemp  l2avgtemp lavgtemp  avgtemp le1avgtemp le2avgtemp le3avgtemp  press6t4 dew6t4 prcp6t4 wind6t4   $pollutants  i.dayofweek  i.nati i.year i.cm i.chair, vce (cluster cm)
estimate store lead_lag_typeofap

coefplot, keep(l3avgtemp  l2avgtemp lavgtemp  avgtemp  le1avgtemp le2avgtemp le3avgtemp) vertical yline(0) ci(95) scheme(s1mono) saving(exposuretype, replace)

qui reg middleast  l3avgtemp l2avgtemp lavgtemp  avgtemp  le1avgtemp le2avgtemp le3avgtemp  press6t4 dew6t4 prcp6t4 wind6t4  $pollutants i.dayofweek  i.type i.year i.cm i.chair , vce (cluster cm)
estimate store lead_lag_nati


coefplot, keep(l3avgtemp l2avgtemp lavgtemp  avgtemp  le1avgtemp le2avgtemp le3avgtemp ) vertical yline(0) ci(95) scheme(s1mono) saving(exposurenati, replace)

qui reg female  l3avgtemp l2avgtemp lavgtemp  avgtemp  le1avgtemp le2avgtemp le3avgtemp  press6t4 dew6t4 prcp6t4 wind6t4  $pollutants i.dayofweek  i.type i.year i.cm i.nati , vce (cluster cm)
estimate store lead_lag_chair


coefplot, keep(l3avgtemp l2avgtemp lavgtemp  avgtemp  le1avgtemp le2avgtemp le3avgtemp ) vertical yline(0) ci(95) scheme(s1mono) saving(exposurechair, replace)


qui reg typeofap $nweather $pollutants i.dayofweek  i.nati i.year i.cm i.chair , cluster (cm)
estimate store random_type_nl

coefplot, keep(t2avebdum*) vertical yline(0) ci(95) scheme(s1mono) saving(nltype, replace)


qui reg middleast $nweather  $pollutants i.dayofweek  i.type i.year i.cm i.chair , cluster (cm)
estimate store random_national_nl

coefplot, keep(t2avebdum*) vertical yline(0) ci(95) scheme(s1mono) saving(nlnati, replace)

qui reg female $nweather $pollutants i.dayofweek  i.type i.year i.cm i.nati  , cluster (cm)
estimate store random_chair_nl

coefplot, keep(t2avebdum*) vertical yline(0) ci(95) scheme(s1mono) saving(nlchair, replace)


***FIGURE A.2
g num=1
bys date city chair: egen totcase=sum(num)

duplicates drop date city chair, force

 reg totcase $weatherdaily $pollutants i.cm i.year i.dayofweek i.chair , cluster (cm)
estimate store numberofcase	
	
esttab numberofcase using number.tex,replace keep(avgtemp10) se brackets

qui reg totcase $nweather $pollutants i.cm i.year i.dayofweek i.chair  , cluster (cm)
estimate store random_total_nl

coefplot, keep(t2avebdum*) vertical yline(0) ci(95) scheme(s1mono) saving(nltot, replace)

qui reg totcase  l3avgtemp l2avgtemp lavgtemp  avgtemp  le1avgtemp le2avgtemp le3avgtemp  $weatherdailyt $pollutants i.dayofweek  i.type i.year i.cm i.chair , vce (cluster cm)
estimate store totalcase_lag

coefplot, keep(l3avgtemp l2avgtemp lavgtemp  avgtemp  le1avgtemp le2avgtemp le3avgtemp ) vertical yline(0) ci(95) scheme(s1mono) saving(exposuretotalcase, replace)



*************************
*T TESTs presented in table 3
*************************




	
qui reg res  $weather6t4 $pollutants i.nati 
estimate store base_3


suest base_1 base_3 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_3_mean]temp6t4
	
qui reg res  $weather6t4 $pollutants  i.dayofweek   i.nati  
estimate store base_4

suest base_1 base_4 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_4_mean]temp6t4


qui reg res  $weather6t4 $pollutants  i.nati i.type i.dayofweek
estimate store base_5

suest base_1 base_5 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_5_mean]temp6t4


qui reg res  $weather6t4 $pollutants  i.nati i.type i.dayofweek i.chair
estimate store base_6

suest base_1 base_6 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_6_mean]temp6t4


qui reg res  $weather6t4 $pollutants  i.nati i.type i.dayofweek i.chair i.cm 
estimate store base_7

suest base_1 base_7 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_7_mean]temp6t4


qui reg res  $weather6t4 $pollutants i.nati i.type i.chair i.dayofweek i.ct i.ym
estimate store base_8

suest base_1 base_8 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_8_mean]temp6t4

	
qui reg res  $weather6t4 $pollutants i.nati i.type  i.chair i.dayofweek i.cym  
estimate store base_9

suest base_1 base_9 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_9_mean]temp6t4

	
qui reg res  $weather6t4 $pollutants i.nati i.type i.chair i.dayofweek i.jm i.ct i.year
estimate store base_10

suest base_1 base_10 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_10_mean]temp6t4

qui reg res  $weather6t4 $pollutants i.nati i.type i.chair i.cm i.year i.date
estimate store base_11

suest base_1 base_11 , vce (cluster cm)
test [base_1_mean]temp6t4 = [base_11_mean]temp6t4





