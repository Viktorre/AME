# -*- coding: utf-8 -*-

from DataImporter import DataImporter
from Plotter import Plotter


if __name__ == '__main__':

    di = DataImporter()
    di.put_dta_into_df("matched.dta")
    df = di.data
    Plotter = Plotter()
    Plotter.plot_long_lat(df)
