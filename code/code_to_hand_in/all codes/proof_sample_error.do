cd "C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final"


use matched, clear

cd "C:/Users/fx236/Documents/AME/code/court_cases_codes/stata_exports"


g year=year(date) // welches jahr (2000 bis 2004


drop if co == .

keep if year == 2001