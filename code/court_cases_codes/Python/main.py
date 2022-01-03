# -*- coding: utf-8 -*-

from DataImporter import DataImporter
from TexWriter import TexWriter
from SummaryStats import SummaryStats
import time
import pandas as pd
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 12)

if __name__ == '__main__':
    startTime = time.time()
    DataImporter = DataImporter()
    TexWriter = TexWriter()
    data_source_path = 'C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final/matched.dta'
    DataImporter.put_dta_into_df(data_source_path)
    from RegressionSettings import RegressionSettings
    RegressionSettings = RegressionSettings()
    from DataFormatter import DataFormatter
    DataFormatter = DataFormatter()
    print(DataImporter.data)
    df = DataFormatter.return_formatted_df(DataImporter.data,
                                           "table1", RegressionSettings)

    from Plotter import Plotter

    Plotter.double_plot_year_dist_with_and_whithout_co(df)
    
    Plotter.plot_na_dist_of_n_cols_with_most_na(df,RegressionSettings)
    

#    SummaryStats = SummaryStats()
#    
    table_1 = SummaryStats.return_summary_of_varlist(df,['res',
            'tempmean','heat','airpressure0','avgdewpt','precip0',
            'windspeed0','skycover','ozone','co','pm25'])
    # TexWriter.export_any_pandas_table(table_1, 'Table 1')





'''
to dos:    
    - matched data
    - paper lesenum zu wissen welche restuls noch replizieren
    - runden in summary stats
    - 

questions for balietti:
    - f-statisitc issue with subset regressors significance
    - do I explain deviations in my results?
    - I would like to do a real spatial regression
    - (fertig formattiert) formatting okay?
        - why formatting not as yours?
    - is it okay if I borrow parts of stata code for variable creation?
    - summary stats stata code is missing. can my stats differ in var choice?
        -> i would use most important vars from main regression
    - do you want to have a runnging version of the code at the end? (libraries
        and dataset size)
    - should I comment sdev in my summary table? and how?
    - maybe doublecheck together in stata that table 2 commands are pooled ols
    - do you have an idea why my effects have so different pvalues than paper?

questions in paper:
    - why in tbale 2 not same specifications in code?(doublecheck that aganin in dofile)   
        i think only (4) is different
'''    