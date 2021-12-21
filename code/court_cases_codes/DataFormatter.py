# -*- coding: utf-8 -*-
import pandas as pd

class DataFormatter():

    def __init__(self, *args, **kwargs):
        pass
    
    def return_formatted_df(self,df,setting_name,RegressionSettings):
        if setting_name == "table1":
            print("formatted dataframe for "+setting_name)
            print(RegressionSettings.return_vars_as_flat_list(
                                             keys=['weather6t4','pollutants']))
            df = self.add_promil_vars_to_df(df,['avgtemp', 'temp6t4', 
                    'heat', 'ltemp6t4', 'letemp6t4'])
            
            df = self.drop_na_by_col_names(df,RegressionSettings.\
                    return_vars_as_flat_list(keys=['weather6t4','pollutants']))
            df = self.add_dimension_vars_to_df(df)
            
            for var in ['dayofweek','nat_name','c_asy_type','year','citymonth','chair']:                
                df = self.add_dummies_to_df_numeric(df,var) #wäre gut mit settings hier
        return df
        

    def add_dummies_to_df(self,df,dummy_name):
        for unique_val in df[dummy_name].unique():
            temp_column = []
            for row in df[dummy_name]:
                if row == unique_val:
                    temp_column.append(1)
                else:
                    temp_column.append(0)
            df[dummy_name+str(int(unique_val))] = temp_column
            print("'"+dummy_name+str(int(unique_val))+"',")
        return df
    
    def add_dummies_to_df_numeric(self,df,dummy_name):
        """ this fct loops through all unique values (in no specific
        order) and creates new dummy column identfied by asending 
        numbers."""
        dummy_counter = 0 
        for unique_val in df[dummy_name].unique():
            temp_column = []
            for row in df[dummy_name]:
                if row == unique_val:
                    temp_column.append(1)
                else:
                    temp_column.append(0)
            df[dummy_name+str(dummy_counter)] = temp_column#changes order!
            print("'"+dummy_name+str(dummy_counter)+"',")
            dummy_counter+=1
        return df
    
    
    def create_missing_vars(self,df):
        pass 
    
    def drop_na_by_col_names(self, df, var_list):
        df = df.dropna(subset=var_list)
        return df
    
    def slice_df_by_date(self,df,start,end):
        return df.loc[(df['date'] >= start) & (df['date'] < end)]

    def add_promil_vars_to_df(self, df, var_list):
        '''
        This fct takes all var from var list, divides them by 1000 and
        adds them to df with column names '<columnname>10'
        '''
        column_names = []
        for var in var_list:
            column_names.append(var+'10')
        new_columns = df[var_list]/1000
        new_columns.columns = column_names
        return pd.concat([df,new_columns],axis=1)
    
    def add_dimension_vars_to_df(self,df):
        '''
        This fct adds all kinds of time variables to the dataframe. Due
        to a lot of manual coding, this prone to errors which might 
        influence the regression'
        '''
        df['year'] = df['date'].dt.year.astype(float)
        df['month'] = df['date'].dt.month.astype(float)
        df['week'] = df['date'].dt.week.astype(float)
        df['cityweek'] = df['city'] + df['week'].astype(str)
        df['citymonth'] = df['city'] + df['month'].astype(str)
        df['cityyear'] = df['city'] + df['year'].astype(str)
        df['yearweek'] = df['week']+df['year'].astype(float)
        df['cityyearmonth'] = df['city'] + df['month'].astype(str) +\
                                df['year'].astype(str)
        df['judgemonth'] = df['ij_name'] + df['month'].astype(str)
        df['judgemonthyear'] = df['ij_name'] + df['year'].astype(str)\
                                + df['month'].astype(str)
        df['dayofweek'] = df['date'].dt.dayofweek.astype(float)
        return df

