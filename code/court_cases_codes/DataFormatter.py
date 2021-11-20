# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

class DataFormatter():

    def __init__(self, *args, **kwargs):
        pass

    def clean_dataset(self,df):
        assert isinstance(df, pd.DataFrame), \
        "df needs to be pd.DataFrame"
        df.dropna(inplace=True)
        # indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
        # return df[indices_to_keep].astype(np.float64)
        return df