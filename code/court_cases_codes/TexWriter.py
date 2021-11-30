# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import statsmodels.api as sm
#from stargazer.stargazer import Stargazer
#from IPython.core.display import HTML

#from TexRession import texression
from linearmodels import OLS

from statsmodels.iolib.summary2 import summary_col

#class TexWriter():

#    def __init__(self, *args, **kwargs):
#        pass


def return_list_of_ascending_ints_in_brackets(how_many_ints):
    list_of_strings = []
    for w in range(1,how_many_ints+1):
        list_of_strings.append('('+str(w)+')')
    return list_of_strings

def asterisk_creator(pvalue):
    if pvalue < 0.01:
        return '***'
    if pvalue <0.05:
        return '**'
    if pvalue <0.1:
        return '*'
    return ''
    
def return_elements_for_result_table_from_reg(reg,title):
    dictionary = {}
    dictionary['     '] = title
    try:
        dictionary['Temperaturet/1000'] = str(reg.params['temp6t410']\
        .round(3))+asterisk_creator(reg.pvalues['temp6t410'])
    except:
        dictionary['Temperaturet/1000'] = str(reg.params['avgtemp10']\
        .round(3))+asterisk_creator(reg.pvalues['avgtemp10'])
    try:
        dictionary[' '] = '['+str(reg.std_errors['temp6t410']\
                   .round(3))+']'
    except:
        dictionary[' '] = '['+str(reg.std_errors['avgtemp10']\
                   .round(3))+']' 
    try:
        dictionary['Temperaturet-1/1000'] = str(reg.params\
                  ['ltemp6t410'].round(3))+asterisk_creator(\
                  reg.pvalues['ltemp6t410'])
    except:
        dictionary['Temperaturet-1/1000'] = '-'
    try:
        dictionary['  '] = '['+str(reg.std_errors['ltemp6t410']\
                   .round(3))+']'
    except:
        dictionary['  '] = '-'
    try:
        dictionary['Temperaturet+1/1000'] = str(reg.params\
                  ['letemp6t410'].round(3))+ asterisk_creator(reg.\
                  pvalues['letemp6t410'])
    except:
        dictionary['Temperaturet+1/1000'] = '-'
    try:
        dictionary['   '] = '['+str(reg.std_errors['lemp6t410']\
                   .round(3))+']'
    except:
        dictionary['   '] = '-'
    dictionary['F-statistic of joint significance'] = reg.\
        f_statistic.stat
    dictionary['of weather variables'] = ' '
    dictionary['P-value'] = reg.f_statistic.pval
    dictionary['Observations'] = reg.nobs
    return dictionary

def create_pandas_export_table_from_regs(reg_list,title_list=
                    ['Preferred','1-Day','lag','1-Day','lead','All']):
    '''
    this fct loops trough regression results and saves each one's 
    relevant numbers into a dictionary. Later these dicts are combined
    via pandas concat and transposed to match latex format
    '''
    export_table = pd.DataFrame([])
    for reg,index,title in zip(reg_list,
                         return_list_of_ascending_ints_in_brackets(
                                 len(reg_list)),title_list):
        export_table = pd.concat([export_table,pd.DataFrame(
                return_elements_for_result_table_from_reg(reg,title),
                index= [index])],sort=False)
    export_table = pd.DataFrame(export_table)
    return  export_table.T

def export_table_as_latex_code(reg_list,filename):
    table = create_pandas_export_table_from_regs(reg_list)
    print(table)
    raw_latex = table.to_latex()
    index = raw_latex.find('Observations')
    raw_latex = raw_latex[:index] + '\midrule\n' + raw_latex[index:]
    with open(filename+'.txt', 'a') as file:
        file.write(raw_latex)



#export_table_as_latex_code([base_6t4,lag_6t4,lead_6t4,all_6t4_one],\
#                           'Table 2')





#import string
#string.replace(our_str, 'you', 'me', 1)    





#class custom_ols3():
#    
#    def __init__(self, estimator):
#        self.estimator = estimator
#
#    def print_coefs(self):
#        print(self.estimator.coef_)
#
#    def fit(self,X_train,y_train):
#        X_train = X_train[['mvel1','b/m','mom1m']]
#        self.estimator.fit(X_train,y_train)          
#        
#    def score(self,X_test,y_test,sample_weight=None):
#        X_test = X_test[['mvel1','b/m','mom1m']]
#        return self.estimator.score(X_test,y_test)
#             
#    def predict(self,X_test):
#        X_test = X_test[['mvel1','b/m','mom1m']]
#        return self.estimator.predict(X_test)
