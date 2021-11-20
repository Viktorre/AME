# -*- coding: utf-8 -*-

import pandas as pd
# from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

class RegressionExecuter():

    def __init__(self, data, *args, **kwargs):
        self.df = data
        self.weatherdaily = ['avgtemp10','skycover',
                             'pressureavgsealevel','windspeed',
                             'precipitationwaterequiv','avgdewpt'] 
        self.weatherdailyt = ['skycover','avgdewpt',
                              'pressureavgsealevel','windspeed',
                              'precipitationwaterequiv']
        self.weathertemp = ['press6t4','dew6t4','prcp6t4','wind6t4',
                            'skycover']
        self.weather6t4  = ['temp6t410','press6t4','dew6t4','prcp6t4',
                            'wind6t4','skycover']
        self.heat = ['heat10','press6t4','','prcp6t4','wind6t4',
                     'skycover']
        self.dailyheat = ['dailyheat','skycover','pressureavgsealevel'
                          ,'windspeed','precipitationwaterequiv']
        self.dummies = ['i.dayofweek','','i.nati','i.type','i.year'
                        ,'i.cm','i.chair']
        self.pollutants = ['ozone','co','pm25']


    def reg_base_6t4_nothing(self):
        # return self.df
        
        ###base regression
        mod = sm.OLS(self.df['res'],
                      self.df[self.weatherdaily])
        return mod.fit().summary()
        
        ### panel regression
        
        

        
        
        
    
    # def reg_base_6t4_nothing(self,df):
        # return df







# http://darribas.org/gds_scipy16/ipynb_md/07_spatial_clustering.html


# from arcgis.features import GeoAccessor
# import pandas as pd
# from numpy.random import rand

# lats = rand(5) * 45 + 30
# lons = rand(5) * 45 + 30

# df = pd.DataFrame({'lat':lats, 'lon':lons})


# check do file and comment it