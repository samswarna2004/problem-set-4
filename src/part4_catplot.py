'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.


# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# 
# In a print statement, answer the following question: What might explain the difference between the plots?


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?


def build_felony_charge_df(arrest_events):
    """
    Creates a dataframe showing whether each arrest_id had at least one felony charge.

    Parameters:
        arrest_events (pd.DataFrame): charge-level arrest dataframe

    Returns:
        pd.DataFrame: dataframe with columns ['arrest_id', 'has_felony_charge']
    """

    felony_charge = (
        arrest_events.groupby('arrest_id')['charge_degree']
        .apply(lambda x: (x == 'felony').any())
        .reset_index(name='has_felony_charge')
    )

    return felony_charge


def cat_plots(pred_universe, arrest_events):
    """
    Creates the categorical plots

    Parameters:
        pred_universe (pd.DataFrame): prediction-level dataframe
        arrest_events (pd.DataFrame): charge-level arrest dataframe

    Returns:
        pd.DataFrame: merged dataframe containing felony charge indicator
    """

    # arrest-level felony indicator
    felony_charge = build_felony_charge_df(arrest_events)

    # merge that new dataframe into pred_universe
    merged_df = pred_universe.merge(felony_charge, on='arrest_id', how='left')

    # y-axis is predicted felony rearrest
    g1 = sns.catplot(
        data=merged_df,
        x='has_felony_charge',
        y='prediction_felony',
        kind='bar'
    )
    g1.fig.suptitle('Predicted Felony Rearrest by Current Charge Type', y=1.03)
    g1.savefig('./data/part4_plots/catplot1.png')
    plt.close('all')

    # y-axis is predicted nonfelony rearrest
    g2 = sns.catplot(
        data=merged_df,
        x='has_felony_charge',
        y='prediction_nonfelony',
        kind='bar'
    )
    g2.fig.suptitle('Predicted Nonfelony Rearrest by Current Charge Type', y=1.03)
    g2.savefig('./data/part4_plots/catplot2.png')
    plt.close('all')

    # Print interpretation
    print("Question:")
    print("The difference between the plots may show that current felony charges are more strongly associated")
    print("with higher predicted felony rearrest than with predicted nonfelony rearrest.")
    print()

    # hue by whether person actually got rearrested for a felony
    g3 = sns.catplot(
        data=merged_df,
        x='has_felony_charge',
        y='prediction_felony',
        hue='y_felony',
        kind='bar'
    )
    g3.fig.suptitle('Predicted Felony Rearrest by Charge Type and Actual Felony Rearrest', y=1.03)
    g3.savefig('./data/part4_plots/catplot3.png')
    plt.close('all')

    # Print interpretation 
    print("Question:")
    print("This plot compares predicted felony rearrest with both current charge type and actual felony rearrest outcome.")
    print("It may show that people with a current felony charge tend to receive higher felony-risk predictions,")
    print("but the people who actually did get rearrested for a felony are the ones with y_felony = 1.")
    print()

    return merged_df