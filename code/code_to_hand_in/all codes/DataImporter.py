# -*- coding: utf-8 -*-

import pandas as pd


class DataImporter:

    def __init__(self, *args, **kwargs):
        self.data = pd.DataFrame(None)

    def put_dta_into_df(self, path_and_file_name):
        self.data = pd.read_stata(path_and_file_name)
