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

#dfoutput = summary_col([sm1,sm2],stars=True)
#print(dfoutput)
#dfoutput.as_latex()
#with open('latex_test.txt', 'a') as file:
#    file.write(dfoutput.as_latex())
#
#pd.DataFrame(dfoutput.tables[0])
def return_list_of_ascending_ints_in_brackets(how_many_ints):
    list_of_strings = []
    for w in range(1,how_many_ints+1):
        list_of_strings.append('('+str(w)+')')
    return list_of_strings

def return_result_table(results_array):
    table = pd.DataFrame(columns=
            return_list_of_ascending_ints_in_brackets(len(results_array)))
    table.loc[''] =  return_list_of_ascending_ints_in_brackets(len(\
                     results_array))#ka warum hier plain numbers...
#    for res in results_array:
#        print(res)
    table.loc['Temperaturet/1000'] = [1,2,3,4]
    table.loc[' '] = [1,2,3,4]
    table.loc['Temperaturet-1/1000'] = [1,2,3,4] 
    table.loc['  '] = [1,2,3,4]
    table.loc['Temperaturet+1/1000'] = [1,2,3,4]
    table.loc['   '] = [1,2,3,4]
    table.loc['F-statistic of joint significance'] = [1,2,3,4]
    table.loc['of weather variables'] = ['','','','']
    table.loc['P-value'] = [1,2,3,4]
    table.loc['Observations'] = [1,2,3,4]
    return table

def export_table_as_latex_code(table,filename,header=True):
    raw_latex = table.to_latex(header=header)
    index = raw_latex.find('Observations')
    raw_latex = raw_latex[:index] + '\midrule\n' + raw_latex[index:]
    with open(filename+'.txt', 'a') as file:
        file.write(raw_latex)

def asterisk_creator(pvalue):
    if pvalue < 0.01:
        return '***'
    if pvalue <0.05:
        return '**'
    if pvalue <0.1:
        return '*'
    
table = return_result_table([base_6t4,lag_6t4,lead_6t4,all_6t4_one])
export_table_as_latex_code(table,'Table 2',header=[
        '(1)\nPreferred','2','3','4' ])
dir(base_6t4.params)
dir(base_6t4)
    
[
str(base_6t4.params[0])+asterisk_creator(base_6t4.pvalues[0]),
'['+str(base_6t4.std_errors[0])+']',

]
 morgen überlegen wie das klug machen alles! morgen table fertig haben!!!
und anndere tables denken. und schauen welche ergebnisse ich repliieren will!!   
    
base_6t4
base_6t4.summary






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
#              
#
#


#diabetes = datasets.load_diabetes()
#df = pd.DataFrame(diabetes.data)
#df.columns = ['Age', 'Sex', 'BMI', 'ABP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']
#df['target'] = diabetes.target
#
#est = sm.OLS(endog=df['target'], exog=sm.add_constant(df[df.columns[0:4]])).fit()
#est2 = sm.OLS(endog=df['target'], exog=sm.add_constant(df[df.columns[0:6]])).fit()
#
#base_6t4
#
#stargazer = Stargazer(res)
#
#HTML(stargazer.render_html())
#
#
#https://github.com/mwburke/stargazer/blob/master/examples.ipynb
#

#schauen wie texressin da rein
