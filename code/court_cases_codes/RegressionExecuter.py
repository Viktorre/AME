# -*- coding: utf-8 -*-

import pandas as pd
# from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from linearmodels.panel import PooledOLS

class RegressionExecuter():

    def __init__(self, data, *args, **kwargs):
        self.var_dictionary = \
            {'weatherdaily':['avgtemp10','skycover',
                             'pressureavgsealevel','windspeed',
                             'precipitationwaterequiv','avgdewpt'] ,
            'weatherdailyt':['skycover','avgdewpt',
                             'pressureavgsealevel','windspeed',
                             'precipitationwaterequiv'],
            'weathertemp':['press6t4','dew6t4',
                           'prcp6t4','wind6t4','skycover'],
            'weather6t4' :['temp6t410','press6t4','dew6t4',
                           'prcp6t4','wind6t4','skycover'],
            'heat':['heat10','press6t4','prcp6t4','wind6t4',
                          'skycover'],
            'dailyheat':['dailyheat','skycover','pressureavgsealevel',
                         'windspeed','precipitationwaterequiv'],
            'dummies':['dayofweek1','dayofweek3', 'dayofweek2', 
                       'dayofweek5', 'dayofweek4'],
            'pollutants' : ['ozone','co','pm25']}
        self.df = data
        self.df = self.drop_na_col_names()

    def flatten_dict_of_lists(self, dictionary, keys='all keys'):
        '''in default, this fct will return elements of the entire
        dictionary. keys=... lets you specify certain parts if needed
        '''
        list_of_all_elements = []
        if keys == 'all keys':
            for key in dictionary.keys():
                for element in dictionary[key]:
                    list_of_all_elements.append(element)
        else:
            for key in keys:
                for element in dictionary[key]:
                    list_of_all_elements.append(element)            
        return list_of_all_elements

    def drop_na_col_names(self):
        '''Dropping NA values in variables due to missing value 
        sensitivity of regression module. This changed version of df 
        is only saved as attribute.'''
        self.df = self.df.dropna(subset=self.\
                        flatten_dict_of_lists(self.var_dictionary))
        return self.df
                
    def reg_base_6t4_nothing(self, wanted_regressors):
        '''base regression'''
        regressor_list = self.\
                    flatten_dict_of_lists(self.var_dictionary,keys=
                                          wanted_regressors)
        mod = sm.OLS(self.df['res'], self.df[regressor_list])
        return mod.fit().summary()
                
    
    def reg_panel(self, wanted_regressors):
        '''panel regression'''
        regressor_list = self.\
                    flatten_dict_of_lists(self.var_dictionary,keys=
                                          wanted_regressors)    
        df = self.df.set_index(['id1','date'])
        mod = PooledOLS(df['res'],df[regressor_list] )
        pooled_res = mod.fit()
        # print(dir(pooled_res))
        return pooled_res
        
        
        # https://bashtage.github.io/linearmodels/panel/examples/examples.html
        






### geo stuff###
# http://darribas.org/gds_scipy16/ipynb_md/07_spatial_clustering.html


# from arcgis.features import GeoAccessor
# import pandas as pd
# from numpy.random import rand

# lats = rand(5) * 45 + 30
# lons = rand(5) * 45 + 30

# df = pd.DataFrame({'lat':lats, 'lon':lons})


# check do file and comment it