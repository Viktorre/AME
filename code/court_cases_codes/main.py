# -*- coding: utf-8 -*-

from DataImporter import DataImporter
from DataFormatter import DataFormatter
from RegressionSettings import RegressionSettings
from Plotter import Plotter
from RegressionExecuter import RegressionExecuter
from TexWriter import TexWriter
from SummaryStats import SummaryStats
import pandas as pd

if __name__ == '__main__':

    DataImporter = DataImporter()
#    DataImporter.put_dta_into_df('C:/Users/fx236/Documents/AME_files/court_cases_data/my_exports/final_dataset_stata_output.dta')
    DataImporter.put_dta_into_df('C:/Users/user/Documents/B.A. Governance Sem.6/Heidelberg Master/Applied Methods Enviornment/dataset/paper_data_line_192.dta')
    df = DataImporter.data#[pd.Timestamp('2000-01-01'):pd.Timestamp('2001-01-01')] 
    RegressionSettings = RegressionSettings()
    DataFormatter = DataFormatter()
    df = DataFormatter.add_dummies_to_df(df,'dayofweek') #wäre gut mit settings hier
    df = DataFormatter.drop_na_by_col_names(df, 
                    RegressionSettings.return_vars_as_flat_list())
    Plotter = Plotter()
    Plotter.plot_long_lat(df)    
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


    TexWriter = TexWriter()
    TexWriter.export_reg_results_as_latex_code(table_2_regs, 'Table 2')

    
    
#    SummaryStats = SummaryStats()
#    
#    table_1 = SummaryStats.return_summary_of_varlist(df,['res',
#            'tempmean','heat','airpressure0','avgdewpt','precip0',
#            'windspeed0','skycover','ozone','co','pm25'])
#    TexWriter.export_any_pandas_table(table_1, 'Table 1')


'''
to dos before tuesday evenig:
    - 1. korrekturlesen intro und lit review
    - 1.5 ein chapter ganz oder zumindest stickpunkte überall schreiben
    - 2. test timeframe robustness (fun)
    - 3. fragen ausformulieren + email text
    - 4. alles abend abschicken
    - write shitty abstract
    - data Empirical strategy schnelles draft tippen
    - data results schnelles draft tippen
    - data summary schnelles draft tippen
to dos:    
    - summary stats var doppelchck
    - in stata ohne qui reg summaries vgl
    - runden in summary stats
    - cool: in stata schritt für schritt schauen was mein do file für data prep
        macht und das aufschreiben, egal ob ichs dann noch in py mach ode rnicht

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
    

questions in paper:
    - why in tbale 2 not same specifications in code?(doublecheck that aganin in dofile)   

'''    