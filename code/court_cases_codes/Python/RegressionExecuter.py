# -*- coding: utf-8 -*-

import pandas as pd
import geopandas
# from sklearn.linear_model import LinearRegression
#import statsmodels.api as sm
from linearmodels.panel import PooledOLS
from linearmodels import OLS

class RegressionExecuter():

    def __init__(self, data, *args, **kwargs):           
        self.df = data
                
#    def reg_cross_section(self, regressor_list):
#        '''base regression'''
#        mod = sm.OLS(self.df['res'], self.df[regressor_list])
#        return mod.fit()#.summary()
    
    def reg_panel(self, regressor_list, dimensions):
        '''panel regression'''   
        df = self.df.set_index(dimensions)
        regressor_list = self.\
        private_function_exclude_regressors_that_are_not_int_df(
                self.df,regressor_list)
        mod = PooledOLS(df['res'],df[regressor_list])
        return mod.fit()
        
    def reg_linear_model(self, regressor_list):
        '''base regression'''
        mod = OLS(self.df['res'], self.df[regressor_list])
        return mod.fit()#.summary()
    # https://bashtage.github.io/linearmodels/panel/examples/examples.html
        
        
    def private_function_exclude_regressors_that_are_not_int_df(self,
                                                    df, regressors):
        for reg in regressors:
            if not reg in df.columns:
                print(reg,'dropped from regression due to no data')
                regressors.remove(reg)
        return regressors






### geo stuff###
# http://darribas.org/gds_scipy16/ipynb_md/07_spatial_clustering.html


# from arcgis.features import GeoAccessor
# import pandas as pd
# from numpy.random import rand

# lats = rand(5) * 45 + 30
# lons = rand(5) * 45 + 30

# df = pd.DataFrame({'lat':lats, 'lon':lons})


# check do file and comment it