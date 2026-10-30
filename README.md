# Electric Vehicle Population Data Analysis

- Team Name: KDD16
- Names of the Contributors: Diego Rocabado, Drew Cutright, Kieran Tennyson

## Objective and Motivation

### Dataset Information
The dataset that is selected is called “Electric Vehicle Population Data”. The dataset displays the battery electric vehicles and plug-in hybrid vehicles that are registered through the Washington State Department of Licensing. The dataset is consistently updated to show the current vehicle registration information, it has been updated as of 10/14/2026. The dataset includes information on the county and state of the registered vehicle, vehicle clean fuel eligibility, electric vehicle type, year, make, and model. 

### Question 1: EV Powertrain Type vs. Population Density
> **Is there a relationship between the number of Battery Electric Vehicles and Plug-in Hybrid Electric Vehicles compared to population density?**

* **Form of Expected Answer:**  
  This question can be answered by performing a two-sample t-test and a chi-squared test. These tests will compare the population density to the number of BEVs and PHEVs within that county. The results will state whether to reject our null hypothesis that there isn’t a relationship between different types of electric vehicles and population density.

* **Potential Benefits:**  
  Since BEVs require power from the grid to charge the battery, the results from the analysis could help policymakers determine which counties need more power to support the charging load of the BEVs.

### Question 2: Model Popularity vs. Rated Electric Range
> **Is there a relationship between the most popular EV models and EV models with higher electric range?**

* **Form of Expected Answer:**  
  The answer will utilize a one-sided, two-sample t-test and a chi-squared test. The t-test will find whether the top five EV models tend to have a higher electric range compared to other electric cars. The chi-squared test will group the vehicles into three mileage bins like a short range bin, medium range bin, and long range bin. Our null hypothesis will be that range is not related to how popular a model is. If the null hypothesis is rejected, it proves that there is a correlation between electric range and model popularity.

* **Potential Benefits:**  
  This could help EV companies to determine whether range is the main driving factor behind which EVs people are buying or if other factors are more important.

### Question 3: CAFV Eligibility Distribution Across Counties
> **How are vehicles with the Clean Alternative Fuel Vehicle (CAFV) eligibility status related to the county of registration across Washington State?**

* **Form of Expected Answer:**  
  The results will be shown by performing a two-sided, two-sample t-test and a chi-squared test. The chi-squared test will find whether vehicle CAFV is dependent on location by comparing the observed number of eligible and not eligible vehicles and comparing them to expected counts that are based on state rates. The two-sided t-test will check if CAFV eligible cars have a large difference in average model year compared to non-eligible cars. If the null hypothesis is rejected, then a vehicle's CAFV status and age are tied to the county of registration.

* **Potential Benefits:**  
  The results of this question could help policymakers determine which counties an alternative fuel program could have the most effect in increasing the amount of CAFVs.

## Introduction 

We are performing an analysis of electric vehicles in Washington in order to make larger determinations about general trends in electric vehicles in the United States. By analyzing this data we can better understand the reception of EVs in the US including adoption rates, the effect of charging capabilities, and the relative growth of hybrid and full EV vehicle populations. The methods in this study are generally simple and align with common statistical practices.


## Implementation 

To find the relationship between population density and electric vehicles per person, we will refer to both data sets. We expect that higher population densities will correlate with higher electric vehicle ownership. To study this, we will bin vehicles into their corresponding regions and then bin regions into population densities. There will be three curves: region vs population density, region vs hybrid vehicles, and region vs electric vehicles. We expect that two of these curves, after being normalized, will look very similar to each other. To examine their agreement, we will run a chi-squared analysis of the population density and hybrid vehicles plots, and the population density and electric vehicles plots, and then compare chi-square values. 

We also want to examine the relationship between electric range and popular vehicles, to see if range is a contributing factor to purchasing electric vehicles. We suspect a positive correlation between the two data sets. To examine this relationship, we will bin popularity based on purchases (i.e. the number of current models) for each model. We will also bin models according to their ranges. The two graphs will include models vs. popularity, and models vs. range. These two graphs will be compared with a chi-squared analysis to see their agreement. 

Our final point is to assess the relationship between the vehicle’s CAFV eligibility and the county of registration. We suspect that certain regions contain groups of people that may be more concerned about legal aspects or motives towards ending climate change, with CAFV eligibility being an indicator. We propose that environmental concern is more centralized rather than randomly distributed throughout Washington state. To test this hypothesis, we will compare a region vs. population density graph to a region vs. vehicles with CAFV eligibility. We will take a chi-square test to either accept or reject the null hypothesis.

### Execution Plans (Metrics, Tools, and Plots)

#### Plan for Q1: EV Powertrain Type vs. Population Density
- **Metrics:** Number of BEVs by county, Number of PHEVs by county, population density by county
- **Packages:** Will need `numpy` and `pandas` to sort the data, `scipy.stats` to perform statistical analysis, and `matplotlib.pyplot` for plotting.
- **Plots:** Two histograms of the number of BEVs by county vs. county population density and the number of PHEVs by county vs. county population density.

#### Plan for Q2: Model Popularity vs. Rated Electric Range
- **Metrics:** Number of owned EVs by model and year, EV model ranges
- **Packages:** `numpy` and `pandas` for data sorting, `scipy.stats` to perform statistical analysis, and `matplotlib.pyplot` for plotting.
- **Plots:** A histogram of popularity vs. range bins.

#### Plan for Q3: CAFV Eligibility vs. County of Registration
- **Metrics:** CAFV status, County registration
- **Packages:** `numpy` and `pandas` for data sorting, `scipy.stats` to perform statistical analysis, and `matplotlib.pyplot` for plotting.
- **Plots:** A histogram of number of vehicles with CAFV status vs. county of registration.

### Implementation Artifacts

## Results: 

## Conclusions: 

## Actions that need to be completed:

### Issues Faced by the Group

## References (IEEE)

[1] “State of Washington - Electric Vehicle Population Data,” Data.gov, 2026. https://catalog.data.gov/dataset/electric-vehicle-population-data?from_hint=eyJzb3J0IjoicG9wdWxhcml0eSJ9 (accessed Oct. 29, 2026).  
[2] “WAOFM - Census - Population Density by County by Decade, 1900 To 2020,” Data.gov, July 06, 2023. http://catalog.data.gov/dataset/waofm-census-population-density-by-county-by-decade-1900-to-2020 (accessed Oct. 29, 2026).
