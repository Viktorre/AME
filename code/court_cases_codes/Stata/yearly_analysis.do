cd "C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final"


use matched, clear
keep if city == "NAPANOCH"

cd "C:/Users/fx236/Documents/AME/code/court_cases_codes/stata_exports"

set matsize 11000 //set max number of vars

foreach i = 2000 2001 2002 2003 2004 {

gen var_`i' = 1

}

