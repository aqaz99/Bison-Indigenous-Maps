# Get geoid
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt

reservations = gpd.read_file('reservation_shapes/tl_2018_us_aiannh.shp')
# Get reservations we want to plot
reservations_df = reservations.to_crs("EPSG:4326")
f = open("reservations.txt", "r")
for line in f.readlines():
    name_grab = line.split(' ')[1]
    print(line)
    for index, row in reservations_df.iterrows():
        if(name_grab in row['NAME']):
            print("     ",row['NAME'], row['NAMELSAD'], row['GEOID'])
            print()