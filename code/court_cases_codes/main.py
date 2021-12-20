# -*- coding: utf-8 -*-

from DataImporter import DataImporter
from DataFormatter import DataFormatter
from RegressionSettings import RegressionSettings
from Plotter import Plotter
from RegressionExecuter import RegressionExecuter
from TexWriter import TexWriter
from SummaryStats import SummaryStats
import pandas as pd
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 12)

if __name__ == '__main__':

    DataImporter = DataImporter()
    RegressionSettings = RegressionSettings()
    DataFormatter = DataFormatter()
    Plotter = Plotter()
    TexWriter = TexWriter()

    DataImporter.put_dta_into_df('C:/Users/user/Documents/B.A. Governance Sem.6/Heidelberg Master/Applied Methods Enviornment/data_court decisions/Data/final/matched.dta')
#    DataImporter.put_dta_into_df('C:/Users/user/Documents/B.A. Governance Sem.6/Heidelberg Master/Applied Methods Enviornment/dataset/paper_data_line_192.dta')
#    DataImporter.put_dta_into_df('C:/Users/user/Documents/B.A. Governance Sem.6/Heidelberg Master/Applied Methods Enviornment/data_court decisions/Data/data_before_table1.dta')

#    df = DataFormatter.slice_df_by_date(DataImporter.data,'2000-01-01'
#                                                        ,'2001-01-01')
#    df = DataFormatter.slice_df_by_date(DataImporter.data,'2001-01-01'
#                                                        ,'2002-01-01')
#    df = DataFormatter.slice_df_by_date(DataImporter.data,'2002-01-01'
#                                                        ,'2003-01-01')
#    df = DataFormatter.slice_df_by_date(DataImporter.data,'2003-01-01'
#                                                        ,'2004-01-01')
    
    df = DataFormatter.return_formatted_df(DataImporter.data,"table1",
                                           RegressionSettings)
    do dummy problem tomorrow
    Plotter.plot_year_dist_of_df(df)
#    Plotter.plot_long_lat(df)    
    RegressionExecuter = RegressionExecuter(df)  
    
    base_6t4 = RegressionExecuter.reg_panel(regressor_list=
                    RegressionSettings.return_vars_as_flat_list(
                    ['weather6t4','pollutants','dummies']),
                    dimensions=['city','month'])

    lag_6t4 = RegressionExecuter.reg_panel(regressor_list=
                    RegressionSettings.return_vars_as_flat_list(
                    ['ltemp6t410','weatherdaily','pollutants',
                     'dummies']), dimensions=['city','month'])
    
    lead_6t4 = RegressionExecuter.reg_panel(regressor_list=
                    RegressionSettings.return_vars_as_flat_list(
                    ['letemp6t410','weather6t4','pollutants',
                     'dummies']), dimensions=['city','month'])
    
    all_6t4_one = RegressionExecuter.reg_panel(regressor_list=
                    RegressionSettings.return_vars_as_flat_list(
                    ['ltemp6t410','temp6t410','letemp6t410','press6t4',
                     'dew6t4','prcp6t4','wind6t4','skycover','dummies',
                     'pollutants']), dimensions=['city','month'])
    
    table_2_regs = [base_6t4,lag_6t4,lead_6t4,all_6t4_one]


    TexWriter.export_reg_results_as_latex_code(table_2_regs, 'Table 2')

    
    
#    SummaryStats = SummaryStats()
#    
#    table_1 = SummaryStats.return_summary_of_varlist(df,['res',
#            'tempmean','heat','airpressure0','avgdewpt','precip0',
#            'windspeed0','skycover','ozone','co','pm25'])
#    TexWriter.export_any_pandas_table(table_1, 'Table 1')





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