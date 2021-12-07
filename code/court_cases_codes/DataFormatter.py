# -*- coding: utf-8 -*-

class DataFormatter():

    def __init__(self, *args, **kwargs):
        pass
    
    def add_dummies_to_df(self,df,dummy_name):
        for unique_val in df[dummy_name].unique():
            temp_column = []
            for row in df[dummy_name]:
                if row == unique_val:
                    temp_column.append(1)
                else:
                    temp_column.append(0)
            df[dummy_name+str(int(unique_val))] = temp_column
        return df
    
    def create_missing_vars(self,df):
        pass 
    
    def drop_na_by_col_names(self, df, var_list):
        df = df.dropna(subset=var_list)
        return df
    
    def slice_df_by_date(self,df,start,end):
        return df.loc[(df['date'] >= start) & (df['date'] < end)]