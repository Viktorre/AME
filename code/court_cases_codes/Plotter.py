# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class Plotter():

    def __init__(self, *args, **kwargs):
        pass

    def plot_long_lat(self,df):
        plt.figure(figsize = (10,8))
        plt.hist2d(df['longitude'], df['latitude'], bins=150,
                    cmap='hot')
        plt.colorbar().set_label('Number of properties')
        plt.xlabel('Longitude', fontsize=14)
        plt.ylabel('Latitude', fontsize=14)
        plt.title('Spatial Plot', fontsize=17)
        plt.show()
        plt.savefig('long_lat_plot.pdf')

        
