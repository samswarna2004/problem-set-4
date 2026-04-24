'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?


# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?

import seaborn as sns
import matplotlib.pyplot as plt


def scatter_plots(pred_universe, arrest_events):
    """
    Creates the scatter plots

    Parameters:
        pred_universe (pd.DataFrame): prediction-level dataframe
        arrest_events (pd.DataFrame): charge-level arrest dataframe
    """

    # Build the arrest-level felony indicator
    felony_charge = (
        arrest_events.groupby('arrest_id')['charge_degree']
        .apply(lambda x: (x == 'felony').any())
        .reset_index(name='has_felony_charge')
    )

    # Merge into prediction dataframe
    merged_df = pred_universe.merge(felony_charge, on='arrest_id', how='left')

    # Scatterplot 1
    plt.figure()
    sns.scatterplot(
        data=merged_df,
        x='prediction_felony',
        y='prediction_nonfelony',
        hue='has_felony_charge'
    )
    plt.title('Felony vs Nonfelony Predictions')
    plt.savefig('./data/part5_plots/scatterplot1.png', bbox_inches='tight')
    plt.close()

    print("Question:")
    print("The dots on the right side of the plot represent people with higher predicted felony rearrest risk.")
    print("If those dots cluster differently by color, that suggests current felony charge status may relate to prediction patterns.")
    print()

    # Scatterplot 2
    plt.figure()
    sns.scatterplot(
        data=merged_df,
        x='prediction_felony',
        y='y_felony'
    )
    plt.title('Predicted Felony Rearrest vs Actual Felony Rearrest')
    plt.savefig('./data/part5_plots/scatterplot2.png', bbox_inches='tight')
    plt.close()

    print("Question 2:")
    print("This plot can help assess calibration by checking whether higher predicted felony probabilities")
    print("tend to line up more often with actual felony rearrest outcomes of 1.")
    print()