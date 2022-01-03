# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class Plotter():

    def __init__(self, *args, **kwargs):
        pass

    def plot_year_dist_of_df(df):
        df.groupby(df["date"].dt.year).count()['id1'].plot(kind="bar")

    def plot_year_dist_of_df_with_co_missing_vals_dropped(df):
        df = df.dropna(subset=['co'])
        df.groupby(df["date"].dt.year).count()['id1'].plot(kind="bar")

    def double_plot_year_dist_with_and_whithout_co(df):
        no_co = df.dropna(subset=['co'])
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,4))      
        axes[0].bar(df.groupby(df["date"].dt.year).count()['id1'].\
                     index,df.groupby(df["date"].dt.year).count()\
                         ['id1'].values)
        axes[1].bar(no_co.groupby(no_co["date"].dt.year).count()['id1'].\
                     index,no_co.groupby(no_co["date"].dt.year).count()\
                         ['id1'].values)   
        axes[0].set_title('co NA values included')
        axes[0].set_ylabel('N')
        axes[0].set_xlabel('Year')             
        axes[1].set_title('co NA values dropped (Heyes and Saberian)')
        axes[1].set_ylabel('N')
        axes[1].set_xlabel('Year')                              
        fig.tight_layout()
        fig.savefig('double_plot_year_dist_with_and_whithout_co.png')
        plt.show()
        plt.clf() 
                      
    def plot_na_dist_of_n_cols_with_most_na(df,RegressionSettings):
        cols = RegressionSettings.return_vars_as_flat_list(keys=\
                        ['weatherdaily','pollutants'])
        cols.insert(0, "res")
        df[cols].rename(columns={'pressureavgsealevel': 'pressurevg...', 
                           'precipitationwaterequiv': 'precipitation...'})\
        .isnull().sum(axis=0).plot(kind='bar',figsize=(8,4))
        plt.ylabel('NA values')
        plt.title('Distribution of NA values for relevant variables')
        plt.tight_layout()
        plt.savefig('plot_na_dist_of_n_cols_with_most_na.png')

                                 
    def plot_long_lat(df):
        plt.figure(figsize = (10,8))
        plt.hist2d(df['longitude'], df['latitude'], bins=95,
                    cmap='nipy_spectral')
        plt.colorbar().set_label('Number of properties')
        plt.xlabel('Longitude', fontsize=14)
        plt.ylabel('Latitude', fontsize=14)
        plt.title('Spatial Plot', fontsize=17)
        plt.show()
        plt.savefig('long_lat_plot.pdf')
#https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972
# or try to get long lat into shape file or usa shp into long lat...        
        