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
