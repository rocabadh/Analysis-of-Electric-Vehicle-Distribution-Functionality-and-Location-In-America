################################################
# Question 1
# ENGR 315
# Drew Cutright
# 
# Description:
#
# Question 1 states:
#
#   "Is there a relationship between the number of Battery Electric Vehicles and 
#   Plug-in Hybrid Electric Vehicles compared to population density?"
#
# We suspect that plug in hybrids will be more common in areas with lower population density, and 
# electric vehicles will be more common in areas with higher population density.
#
###############################################

# Import packages
import scipy as sp
import numpy as np
import pandas as pd

# Import population data and vehicle data

vehicle_data_source = '../Analysis-of-Electric-Vehicle-Distribution-Functionality-and-Location-In-America/data/car_data.csv'
population_data_source = '../Analysis-of-Electric-Vehicle-Distribution-Functionality-and-Location-In-America/data/pop_dens_county.csv'

# Create data frames for both data sets
vehicle_data_frame = pd.read_csv(vehicle_data_source)
population_data_frame = pd.read_csv(population_data_source)

### Find population desity per region

# Pull out density population data
population_density_2026 = population_data_frame[['County Name', 'Population Density 2026']]

# Make sure population density is in nummeric form and not text
population_density_2026['Population Density 2026'] = pd.to_numeric(population_density_2026['Population Density 2026'], errors='coerce')

# Get Rid of Washington State Data
population_density_2026 = population_density_2026.drop(0)

# Order region from largest to smallest wrt population density
population_density_2026.sort_values(by=['Population Density 2026'], ascending=False, inplace=True, ignore_index=True)

# Check if the code is correctly sorting
print(population_density_2026.iloc[:10, 0:2])

# Pull out county names
county_names = population_density_2026['County Name']
print('\n')
print(county_names.iloc[:10])

### Bin electric vehicles per region

# Consolidate electric vehicles
condensed_vehicle_data_frame = vehicle_data_frame[['County', 'Electric Vehicle Type']]

# Define data fame that will count bins
binned_data = county_names.copy()

# Ensure that the series is a data frame
binned_data = binned_data.to_frame()

# Add two more colums of zeros
binned_data[['Electric Vehicles', 'Hybrid Vehicles']] = 0

for names in county_names:

    for i in range(len(vehicle_data_frame)):

        county_data = vehicle_data_frame[
        vehicle_data_frame['County'] == names
        ]

        binned_data.loc[names, 'Electric Vehicles'] = (
            county_data['Electric Vehicle Type'] ==
            'Battery Electric Vehicle (BEV)'
        ).sum()

        binned_data.loc[names, 'Hybrid Vehicles'] = (
            county_data['Electric Vehicle Type'] ==
            'Plug-in Hybrid Electric Vehicle (PHEV)'
        ).sum()

print(binned_data)

### Bin plug-in hybrid vehicles per region

### Graph

