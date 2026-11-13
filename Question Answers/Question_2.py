#Importing necessary packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import chisquare, ttest_ind 



def main():

    #Relative file path
    path="../Data/export.csv"

    #Load dataset into a dataframe
    df=pd.read_csv(path)

    #Exculeds 0-mile entries 
    df_valid=df[df["Electric Range"]>0]

    #Find top 5 most popular models 
    model_count=df["Model"].value_counts()    
    top_5_models=model_count.head(5).index.tolist()

    #All unique models in a list
    all_models=df_valid["Model"].unique().tolist()

    #Generate lists to hold top 5 models and other models 
    top_5_list=[]
    other_list=[]

    #Loop through all unique models
    for model in all_models:
        model_rows=df_valid[df_valid["Model"]==model]
        model_range=model_rows["Electric Range"].tolist()

        #Check if model is in top 5 list
        if model in top_5_models:
            top_5_list.extend(model_range)
        else:
            other_list.extend(model_range)

    #Convert lists into arrays
    top_5_range=np.array(top_5_list)
    other_range=np.array(other_list)

    #Overall mean and std for both arrays
    top_5_mean=np.mean(top_5_range)
    top_5_std=np.std(top_5_range, ddof=1)
    other_mean=np.mean(other_range)
    other_std=np.std(other_range, ddof=1)

    #One-sided two sample t-test
    alpha=0.05
    (t_stat,t_p_value)=ttest_ind(top_5_range, other_range, equal_var=False, alternative="greater")

    #Prove or reject null hypothesis
    if t_p_value < alpha:
        t_decision="Reject Null Hypothesis: Top 5 Models have a significantly higher electric range."
    else:
        t_decision="Fail to Reject Null Hypothesis: There is not a signifcantly higher electric range for top 5 models."

    #Generate bins for Chi-Square Test
    bins=np.array([0,50,200, np.inf])
    bin_labels=["Short (<50 miles)", "Medium (50-199 miles)", "Long (>=200 miles)"]

    #Oberved counts for top 5 models and other models 
    observed_count, bin_edges=np.histogram(top_5_range, bins=bins)
    other_counts, _ =np.histogram(other_range, bins=bins)

    #Expected counts based on overall dataset 
    all_range=df_valid["Electric Range"].to_numpy()
    total_counts, _ =np.histogram(all_range, bins=bins)
    expected_prob= total_counts/len(all_range)
    expected_counts=expected_prob*len(top_5_range)
   
    #Chi-Square Test
    (chi_stat, chi_p_value) = chisquare(f_obs=observed_count, f_exp=expected_counts)

    if chi_p_value<alpha:
        c_decision=("Reject Null Hypothesis: Bin counts for top 5 models differ from expected")
    else:
        c_decision=("Fail to Reject Null Hypothesis: The bin counts don't differ")

    #Plot Histogram of Electric Range with a normal distribution
    plt.figure(figsize=(8, 5))
    plt.hist(top_5_range, bins=25, alpha=0.6, density=True, label="Top 5 Models Range")
    plt.hist(other_range, bins=25, alpha=0.6, density=True, label="Other Models Range")
    plt.axvline(top_5_mean, color="blue", linestyle="--", label="Top 5 Mean("+str(round(top_5_mean,1))+"mi)",)
    plt.axvline(other_mean, color="red", linestyle="--", label="Other Mean("+str(round(other_mean,1))+"mi)",)
    plt.xlabel("Rated Electric Range (Miles)")
    plt.ylabel("Probability Density")
    plt.title("Normalized Distribution of Rated Electric Range")
    plt.legend()
    plt.savefig("q2_range_histogram.png")

    #plot Group Bar Chart of Range Bins
    top_5_pct=(observed_count/len(top_5_range))*100
    other_pct=(other_counts/len(other_range))*100
    x_pos=np.arange(len(bin_labels))
    width=0.35
    plt.figure(figsize=(8, 5))
    plt.bar(x_pos - width / 2, top_5_pct, width, label="Top 5 Models")
    plt.bar(x_pos + width / 2, other_pct, width, label="Other Models")
    plt.xticks(x_pos, bin_labels)
    plt.xlabel("Rated Electric Range Bin (Miles)")
    plt.ylabel("Percentage of Vehicles (%)")
    plt.title("EV Range Bin Distribution: Top 5 Models vs. Other Models")
    plt.legend()
    plt.savefig("q2_range_bins_bar.png")

    #Print values from the analysis 
    print("----Top 5 Most Popular EV Models----")
    print(f"Top 5 Models: {top_5_models}")
    print("----Overall Group Statistics----")
    print(f"Top 5 Models: Mean={top_5_mean}, STD={top_5_std}")
    print(f"Other Models: Mean={other_mean}, STD={other_std}")
    print("----One-Sided Two Sample T-Test----")
    print(f"Significance Level (Alpha): {alpha}")
    print(f"T-Statistic: {t_stat}")
    print(f"T-Test P-Value: {t_p_value}")
    print(f"T-Test Decision: {t_decision}")
    print("----Chi-Square Test on Electric Range Bins---")
    print(f"Range Bins: {bin_labels}")
    print(f"Observed (Top 5): {observed_count}")
    print(f"Observed (Other): {other_counts}")
    print(f"Expected(Top 5): {expected_counts}")
    print(f"Chi-Square Statistic: {chi_stat}")
    print(f"Chi-Square P-Value: {chi_p_value}")
    print(f"Chi-Square Decision: {c_decision}")
    plt.show()

    #Executes the function
if __name__== "__main__":
    main()







   