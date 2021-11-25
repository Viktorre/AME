# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import statsmodels.api as sm
#from stargazer.stargazer import Stargazer
#from IPython.core.display import HTML

from TexRession import texression
from linearmodels import OLS

from statsmodels.iolib.summary2 import summary_col

#class TexWriter():

#    def __init__(self, *args, **kwargs):
#        pass

dfoutput = summary_col([sm1,sm2],stars=True)
print(dfoutput)
dfoutput.as_latex()
pd.DataFrame(dfoutput.tables[0])

\\begin{table}\n\\caption{}\n\\label{}\n\\begin{center}\n\\begin{tabular}{lll}\n\\hline\n               & res I      & res II      \\\\\n\\hline\ntemp6t410      & -1.3630*** & -1.3630***  \\\\\n               & (0.1553)   & (0.1553)    \\\\\npress6t4       & -0.0041*** & -0.0041***  \\\\\n               & (0.0011)   & (0.0011)    \\\\\ndew6t4         & 0.0004***  & 0.0004***   \\\\\n               & (0.0001)   & (0.0001)    \\\\\nprcp6t4        & 0.1282*    & 0.1282*     \\\\\n               & (0.0657)   & (0.0657)    \\\\\nwind6t4        & 0.0014***  & 0.0014***   \\\\\n               & (0.0003)   & (0.0003)    \\\\\nskycover       & 0.0208***  & 0.0208***   \\\\\n               & (0.0035)   & (0.0035)    \\\\\nozone          & 1.1201***  & 1.1201***   \\\\\n               & (0.0873)   & (0.0873)    \\\\\nco             & 0.0275***  & 0.0275***   \\\\\n               & (0.0020)   & (0.0020)    \\\\\npm25           & -0.0011*** & -0.0011***  \\\\\n               & (0.0001)   & (0.0001)    \\\\\ndayofweek1     & 0.2988***  & 0.2988***   \\\\\n               & (0.0321)   & (0.0321)    \\\\\ndayofweek3     & 0.2884***  & 0.2884***   \\\\\n               & (0.0321)   & (0.0321)    \\\\\ndayofweek2     & 0.2797***  & 0.2797***   \\\\\n               & (0.0321)   & (0.0321)    \\\\\ndayofweek5     & 0.3004***  & 0.3004***   \\\\\n               & (0.0321)   & (0.0321)    \\\\\ndayofweek4     & 0.2930***  & 0.2930***   \\\\\n               & (0.0321)   & (0.0321)    \\\\\nR-squared      & 0.1669     & 0.1669      \\\\\nR-squared Adj. & 0.1668     & 0.1668      \\\\\n\\hline\n\\end{tabular}\n\\end{center}\n\\end{table}

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
