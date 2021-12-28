cd "C:/Users/fx236/Documents/AME_files/court_cases_data/data/Data/final"


use matched, clear


cd "C:/Users/fx236/Documents/AME_files/AME/code/court_cases_codes/stata_exports"

set matsize 11000 //set max number of vars

bys date city: gen id=_n
egen idtime=group(id date) //generate var idtime


g year=year(date) // g means generate variable
g month=month(date)
g week=week(date)

g yearmonth=string(year) + string(month)
g cityweek=string(week) + city
g cityyear= city + string(year) 
g citymonth= city + string(month)
g yearweek= string(week) + string(year)

g cityyearmonth= city + string(month) + string(year)
encode cityyearmonth, g(cym)

g judgemonth=ij_name + string(month)
encode judgemonth, g(jm)

g judgemonthyear=ij_name + string(year) +string(month)
encode judgemonthyear, g(jym)

encode yearmonth, g(ym)
encode cityweek, g(cw)
encode cityyear, g(cy)
encode citymonth, g(cm)
encode yearweek, g(yw)


g dayofweek=dow(date)

encode city, g(ct)
encode c_asy_type, g(type)
encode nat_name, g (nati)

global temp l2avgtemp l3avgtemp lavgtemp  temp6t4  le1avgtemp le2avgtemp le3avgtemp le3temp6t4  le2temp6t4  letemp6t4 ltemp6t4 l2temp6t4 l3temp6t4 avgtemp yearaftertemp gtemp yeartemp heat //create list of vars

foreach var in $temp{ //create new vars 
  
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



bys city week month year:egen meantemp=mean(temp6t4)

foreach var in $weather6t4{
drop if `var'==.
}

foreach var in $pollutants{
drop if `var'==.
}
	


**TABLE 1 and Figure 5

// I assume qui means quiet, and xi is something with dummies? "esttab" returns stored result

g deviation=temp6t4-meantemp	



**TABLE 2
//ssc install estout needed for esttab

**FIGURE 5	
	
	
**TABLE	A1

	

****************************
**TABLE 3
****************************

drop if type==.	
drop if nati==.

	
	
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

****************************
**rain and temp intraction 
****************************	
	
	
g raintemp=temp6t4*skycover
	


**TABLE 4

****************************
**MALE AND FEMALE 
****************************
	
g female=0
replace female=1 if gender=="female"
	

**TABLE A.2
	

*******************************
*** ALTERNATOVE SEs: TABLE 	A4:
*******************************

//tsset ct idtime //mach var idtime iwie zu time/panel variabl?

**************************	
***TABLE 6
***************************

//replace yearaftertemp=temp6t4 if yearaftertemp==.
//replace yeartemp=temp6t4 if yeartemp==.


	
*****************************
***ROBUSTNESS
*****************************	

g ca=0 //generate clalifornia subset
replace ca=1 if city=="SAN PEDRO" | city=="SAN FRANCISCO" | city=="SAN DIEGO" | city=="LOS ANGELES" |city=="LAS VEGAS" | city=="LANCASTER" |city=="IMPERIAL"


bys ij_name: egen rate=mean(res)


***TABLE 5

	

	
*****************************
***Nonlinear Results:  ALL COMMENTED OUT DUE TO RECOD COMMANDS
*****************************	
/*	

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
*/

**FIGURE 6







//drop ht2avebdum11 //var does not exist due to skippd lines in figur 5


***FIGURE 7



**TABLE A.3



****************************
**Randomization test 
****************************


g typeofap=0
replace typeofap=1 if  c_asy_type=="E"


g middleast=0
replace middleast=1 if (nat_name=="BAHRAIN" | nat_name=="CYPRUS" | nat_name=="EGYPT" | nat_name=="IRAN" | nat_name=="IRAQ" | nat_name=="ISRAEL"| nat_name=="JORDAN" | nat_name=="KUWAIT"| nat_name=="LEBANON" | nat_name=="OMAN" | nat_name=="PALESTINE" | nat_name=="QATAR" | nat_name=="SAUDI ARABIA" | nat_name=="SYRIA" | nat_name=="TURKEY" | nat_name=="UNITED ARAB EMIRATES" | nat_name=="YEMEN")


**TABLE A.5


*****FIGURE A.1	
	
	

***FIGURE A.2
g num=1
bys date city chair: egen totcase=sum(num)

//duplicates drop date city chair, force


*************************
*T TESTs presented in table 3
*************************

