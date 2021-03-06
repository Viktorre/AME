# -*- coding: utf-8 -*-
import pandas as pd

class SummaryStats():

    def __init__(self, *args, **kwargs):
        pass
    
    def return_summary_of_varlist(df,varlist):
        summary = pd.concat([df[varlist].mean(),df[varlist].std()],
                             axis=1)
        summary.columns = ['Mean','Std. Dev.']
        return summary.round(3)
        
