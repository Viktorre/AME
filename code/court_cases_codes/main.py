# -*- coding: utf-8 -*-

from DataImporter import DataImporter
from Plotter import Plotter
from DataFormatter import DataFormatter

if __name__ == '__main__':

    DataImporter = DataImporter()
    # DataImporter.put_dta_into_df("matched.dta")
    DataImporter.put_dta_into_df('C:/Users/fx236/Documents/AME_files/court_cases_data/my_exports/paper_data_line_192.dta')
    df = DataImporter.data
    DataFormatter = DataFormatter()
    df = DataFormatter.clean_dataset(df)

    # Plotter = Plotter()
    # Plotter.plot_long_lat(df)
    
    from RegressionExecuter import RegressionExecuter
    RegressionExecuter = RegressionExecuter(df)
    RegressionExecuter.reg_base_6t4_nothing()
