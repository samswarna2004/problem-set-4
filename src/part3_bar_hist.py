'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using the pre_universe data frame, create a bar plot for the fta column.

def bar_hist_plots(pred_universe):
    """
To create the bar plots and histogram 

Parametrs:
    pred_universe: a datafram that contains the arrest prediction data

Saves:
    PNG files to ./data/part3_plots/
    """

    # 1. Bar plot for fta
    plt.figure()
    sns.countplot(data=pred_universe, x='fta')
    plt.title('Counts of FTA')
    plt.savefig('./data/part3_plots/fta_barplot.png', bbox_inches='tight')
    plt.close()

    # 2. Hue the previous barplot by sex
    plt.figure()
    sns.countplot(data=pred_universe, x='fta', hue='sex')
    plt.title('Counts of FTA by Sex')
    plt.savefig('./data/part3_plots/fta_barplot_by_sex.png', bbox_inches='tight')
    plt.close()

    # 3. Plot a histogram of age_at_arrest
    plt.figure()
    sns.histplot(data=pred_universe, x='age_at_arrest')
    plt.title('Histogram of Age at Arrest')
    plt.savefig('./data/part3_plots/age_histogram.png', bbox_inches='tight')
    plt.close()

    # 4. Plot the same histogram with custom age bins
    plt.figure()
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=[18, 21, 30, 40, 100])
    plt.title('Histogram of Age at Arrest Custom Bins')
    plt.savefig('./data/part3_plots/age_histogram_custom_bins.png', bbox_inches='tight')
    plt.close()