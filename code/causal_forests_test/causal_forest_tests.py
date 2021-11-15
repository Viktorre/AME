# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:28:23 2021

@author: fx236
"""


import pandas as pd
from dowhy import CausalModel
from IPython.display import Image, display
from sklearn.model_selection import train_test_split

from econml.dml import CausalForestDML
from sklearn.linear_model import MultiTaskLassoCV, LassoCV

# code adapted from https://github.com/microsoft/EconML
import shap
from econml.dml import CausalForestDML

# read Stata .dta file 
df = pd.read_stata("data_rep.dta")

# set variables 
treatment = 'treatment'
outcome = 'loansamt_total'
covariates = ["members_resid_bl", "nadults_resid_bl", "head_age_bl", "act_livestock_bl", "act_business_bl",
              "borrowed_total_bl", "members_resid_d_bl", "nadults_resid_d_bl", "head_age_d_bl",
              "act_livestock_d_bl", "act_business_d_bl", "borrowed_total_d_bl", "ccm_resp_activ",
              "other_resp_activ", "ccm_resp_activ_d", "other_resp_activ_d", "head_educ_1", "nmember_age6_16"]

# build causal graph with dowhy 
model = CausalModel(
    data=df,
    treatment=treatment, 
    outcome=outcome, 
    common_causes=covariates, 
    instruments=None, 
    effect_modifiers=None)

model.view_model()
display(Image(filename="causal_model.png"))




# drop missing data 
all_variables = covariates
all_variables.append(treatment)
all_variables.append(outcome)

df = df.dropna(axis=0, subset=all_variables)

# split data into train and test sets 
train, test = train_test_split(df, test_size=0.2)


# set variables for causal forest Y=outcome, T=treatment, X=covariates, W=effect_modifiers 
Y = train[outcome]
T = train[treatment]
X = train[covariates]
W = None
X_test = test[covariates]



# set parameters for causal forest 
causal_forest = CausalForestDML(criterion='het', 
                                n_estimators=10000,       
                                min_samples_leaf=10, 
                                max_depth=None, 
                                max_samples=0.5,
                                discrete_treatment=False,
                                honest=True,
                                inference=True,
                                cv=10,
                                model_t=LassoCV(), 
                                model_y=LassoCV(),
                                )
                      
# fit train data to causal forest model 
causal_forest.fit(Y, T, X=X, W=W)
# estimate the CATE with the test set 
causal_forest.const_marginal_ate(X_test)





# fit causal forest with default parameters 
causal_forest = CausalForestDML()
causal_forest.fit(Y, T, X=X, W=W)

# calculate shap values of causal forest model 
shap_values = causal_forest.shap_values(X)
# plot shap values 
# shap.summary_plot(shap_values['Y0']['T0'])
# shap.summary_plot(shap_values.value[instance,feature])
# shap.plots.beeswarm(shap_values, order=shap_values.abs.max(0))


schauen wo das problem ist, evtl kleiners bsp; einmal weniger daten
einmal anderer predictor https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/beeswarm.html

