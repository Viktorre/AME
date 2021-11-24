# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import statsmodels.api as sm
from stargazer.stargazer import Stargazer
from IPython.core.display import HTML

class DataFormatter():

    def __init__(self, *args, **kwargs):


diabetes = datasets.load_diabetes()
df = pd.DataFrame(diabetes.data)
df.columns = ['Age', 'Sex', 'BMI', 'ABP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']
df['target'] = diabetes.target

est = sm.OLS(endog=df['target'], exog=sm.add_constant(df[df.columns[0:4]])).fit()
est2 = sm.OLS(endog=df['target'], exog=sm.add_constant(df[df.columns[0:6]])).fit()

stargazer = Stargazer([est, est2])

HTML(stargazer.render_html())


https://github.com/mwburke/stargazer/blob/master/examples.ipynb