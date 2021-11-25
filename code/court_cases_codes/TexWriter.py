# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import statsmodels.api as sm
#from stargazer.stargazer import Stargazer
#from IPython.core.display import HTML

from TexRession import texression

class TexWriter():

    def __init__(self, *args, **kwargs):
        pass
    
varnames = {'t1' : '$Russell 2000_{t}$',
            't0' : '$Russell 2000_{t-1}$',
            'banded' : 'Banded state',
            'banded_t1' : 'Banded state $\\times Russell 2000_{t}$'
           }

varorder = ['t1', 't0', 'banded', 'banded_t1',
           {'name' : 'Firm controls', 'type' : 'controls',
            'vars' :['NonIndxOwn', 'ISSrec_For', 'log_atq', 'roa', 'bm_ratio', 'firm_leverage']},
           {'name' : 'Year controls', 'type' : 'controls',
            'vars' : ['y_2010', 'y_2011', 'y_2012', 'y_2013', 'y_2014', 'y_2015', 'y_2016']},
           {'name' : 'Float and mk.cap. controls', 'type' : 'controls',
            'vars' : ['mkcap', 'float_value_t1']},
           {'type' : 'silent', 'vars' : ['const']}]


tx = texression(varnames, varorder, ltcaption = """First stage of 2SLS regression.""")

tx.add_regression(OLS(...).fit(), 'Similarity measure')
tx.add_regression(OLS(...).fit(), '\% owned by index funds')

#teste ob ohne wrapper roh möglich.... einfahc dne tbale bekommen

#
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
