# -*- coding: utf-8 -*-

class RegressionSettings():

    def __init__(self, *args, **kwargs):
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
            'pollutants' : ['ozone','co','pm25'],
            'ltemp6t410' : ['ltemp6t410'],
            'letemp6t410' : ['letemp6t410'],
            'temp6t410' : ['temp6t410'],
            'press6t4' : ['press6t4'],
            'dew6t4' : ['dew6t4'],
            'prcp6t4' : ['prcp6t4'],
            'wind6t4' : ['wind6t4'],
            'skycover' : ['skycover'],}

    def return_vars_as_flat_list(self, keys='all keys'):
        '''in default, this fct will return elements of the entire
        dictionary. keys=... lets you specify certain parts if needed
        '''
        list_of_all_elements = []
        if keys == 'all keys':
            for key in self.var_dictionary.keys():
                for element in self.var_dictionary[key]:
                    list_of_all_elements.append(element)
        else:
            for key in keys:
                for element in self.var_dictionary[key]:
                    list_of_all_elements.append(element)            
        return list_of_all_elements