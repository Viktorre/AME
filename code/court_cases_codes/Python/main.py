# -*- coding: utf-8 -*-

from DataImporter import DataImporter
from DataFormatter import DataFormatter
from TexWriter import TexWriter
import pandas as pd
from RegressionSettings import RegressionSettings
from Plotter import Plotter
from SummaryStats import SummaryStats
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 12)

if __name__ == '__main__':
    data_source_path = 'C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final/matched.dta'

    DataImporter = DataImporter()
    DataFormatter = DataFormatter()
    RegressionSettings = RegressionSettings()
    
    DataImporter.put_dta_into_df(data_source_path)
    df = DataFormatter.return_formatted_df(DataImporter.data,
                                           "table1", RegressionSettings)

    Plotter.double_plot_year_dist_with_and_whithout_co(df)
    Plotter.plot_na_dist_of_n_cols_with_most_na(df,RegressionSettings)
    
    table_1 = SummaryStats.return_summary_of_varlist(df,['res',
            'tempmean','heat','airpressure0','avgdewpt','precip0',
            'windspeed0','skycover','ozone','co','pm25'])
    TexWriter = TexWriter()
    TexWriter.export_any_pandas_table(table_1, 'Table 1')
