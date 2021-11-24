# -*- coding: utf-8 -*-

from DataImporter import DataImporter
from DataFormatter import DataFormatter
from RegressionSettings import RegressionSettings

if __name__ == '__main__':

    DataImporter = DataImporter()
#    DataImporter.put_dta_into_df('C:/Users/fx236/Documents/AME_files/court_cases_data/my_exports/final_dataset_stata_output.dta')
    DataImporter.put_dta_into_df('C:/Users/user/Documents/B.A. Governance Sem.6/Heidelberg Master/Applied Methods Enviornment/dataset/paper_data_line_192.dta')
    df = DataImporter.data
    RegressionSettings = RegressionSettings()

    DataFormatter = DataFormatter()
    # df = DataFormatter.clean_dataset(df)
    df = DataFormatter.add_dummies_to_df(df,'dayofweek')
    df = DataFormatter.drop_na_by_col_names(df, 
                    RegressionSettings.return_vars_as_flat_list())

    from Plotter import Plotter
    Plotter = Plotter()
    Plotter.plot_long_lat(df)
    
    from RegressionExecuter import RegressionExecuter
    RegressionExecuter = RegressionExecuter(df)
    
#    print(RegressionExecuter.reg_cross_section(regressor_list=
#                    RegressionSettings.return_vars_as_flat_list(
#                    ['weatherdaily','pollutants','dummies'])))
#    print(5*'\n')
#    print(RegressionExecuter.reg_panel(regressor_list=
#                    RegressionSettings.return_vars_as_flat_list(
#                    ['weatherdaily','pollutants','dummies']),
#                    dimensions=['id1','date']))
   

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
    

    for res in [base_6t4,lag_6t4,lead_6t4,all_6t4_one]:
        print(res)

'''
to dos:    
    - 1. table nachmachen, erstmal händisch
'''


'''
questions for balietti:
    - do I explain deviations in my results?
    - I would like to do a real spatial regression
    
'''    