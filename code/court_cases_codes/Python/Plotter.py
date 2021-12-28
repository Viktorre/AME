# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class Plotter():

    def __init__(self, *args, **kwargs):
        pass

    def plot_year_dist_of_df(self,df):
        df.groupby(df["date"].dt.year).count()['id1'].plot(kind="bar")

    def plot_long_lat(self,df):
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
        