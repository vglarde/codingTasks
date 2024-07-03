'''
This script is designed to fill the missing values for the column "Age" in the
Titanic dataset.

Missing ages represent a significative amount of values (19.9%):
    • 30 in 1st class
    • 11 in 2nd class
    • 136 in 3rd class

Methodology used to populate the missing values for the Age variable:
1. Calculate the proportion of passengers for six age categories:
    • Under 10 years old (children)
    • 10-17 years old (teenagers)
    • 18-30 years old
    • 31-40 years old
    • 41-50 years old
    • Over 50 years old

    Note: Based on the demographic of early 20th century, and the demographic
    of the Titanic passengers, the "older" generation was actually those
    over 50, with very few passengers over 65 or 70 years old.

2. In order to have a more accurate estimation, we will subdivide these
categories based on sex (male/female) and travel class.

3. Based on this distribution, the script will fill the missing values with
random ages within the respective age ranges described above.

==========

Special modification for title "Master" (young boys), otherwise there would be
a discrepancy if the title "Master" was attributed to an adult.

In the dataset, most passengers with the title "Master" are aged 2-8 years old.
Therefore, we will generate random ages between 2-8 years old to fill the
missing Age values for "Master".
'''

# Import library
import pandas as pd
import numpy as np
from numpy.random import randint

# Import dataset 'titanic.csv'
titanic_df = pd.read_csv('Titanic.csv')


'''
Filling missing Age value for category "Master"
'''
# Select passengers with title "Master" and unknown "Age"
ag_master_condition = titanic_df[titanic_df['Name'].str.contains('Master') &
                                 titanic_df['Age'].isna()]
ag_master_condition = ag_master_condition.index.tolist()

# Number of entries
ag_master_len = len(ag_master_condition)

# Generate "Age" randomly (values between 2-8)
ag_master_rand = randint(2, 8, size=ag_master_len).tolist()

# Create dictionary
ag_master_dict = dict(zip(ag_master_condition, ag_master_rand))

# Update Dataframe
titanic_df.update({'Age': ag_master_dict})


'''
Function to add/update "AgeGroup" columns
'''
def age_group_column():
    # Age groups conditions
    ag_conditions = [titanic_df['Age'] < 10,
                     titanic_df['Age'].between(10, 17),
                     titanic_df['Age'].between(18, 30),
                     titanic_df['Age'].between(31, 40),
                     titanic_df['Age'].between(41, 50),
                     titanic_df['Age'] > 50]

    ag_values = ['under10', '10to17', '18to30', '31to40', '41to50', 'over50']

    # Add column "AgeGroup"
    titanic_df['AgeGroup'] = np.select(ag_conditions, ag_values)


# Add column "AgeGroup"
age_group_column()

'''
Function filling missing values for passengers
'''
# Get Total number of passengers
total_passengers = titanic_df.shape[0]


# Function Fill missing values
def fill_missing_age(pclass, sex):
    '''
    This function uses two arguments "pclass" (passenger class),
    and "sex" to select a specific group of passengers.
    It then calculates the percentage of each age category within this group.
    Finally, it generates random ages within each age category in order to
    fill the missing values, in correlation with the age distribution of
    passengers with known age within this group.
    '''

    # Run the function if there are still missing values for column "Age",
    # otherwise, exit the function
    if titanic_df['Age'].isnull().sum() > 0:
        # Select passengers for specific group (based on Pclass and Sex)
        filter = np.where((titanic_df['Pclass'] == pclass) &
                         (titanic_df['Sex'] == sex))
        values = titanic_df.loc[filter]
        total = values['PassengerId'].count()  # Total passengers
        subtotal = values.groupby(['AgeGroup']).size()  # Passengers by age group
        age_missing = subtotal.iloc[0]  # Passengers with missing age
        age_known = total - age_missing  # Passengers with known age

        # Calculate percentage of each age category
        a_10to17 = subtotal.iloc[1] / age_known
        a_18to30 = subtotal.iloc[2] / age_known
        a_31to40 = subtotal.iloc[3] / age_known
        a_41to50 = subtotal.iloc[4] / age_known
        a_over50 = subtotal.iloc[5] / age_known
        a_under10 = subtotal.iloc[6] / age_known

        # Determine the distribution of passengers with missing Age
        m_10to17 = round(age_missing * a_10to17)
        m_18to30 = round(age_missing * a_18to30)
        m_31to40 = round(age_missing * a_31to40)
        m_41to50 = round(age_missing * a_41to50)
        m_over50 = round(age_missing * a_over50)
        m_under10 = round(age_missing * a_under10)

        # Check all missing values have been filled,
        # otherwise attribute the missing value to the "31 to 40" category
        # This problem can only appears for very low number of passengers
        # with missing age, so it would only affect 1 or 2 passenger names. 
        total_missing = (m_10to17
                         + m_18to30
                         + m_31to40
                         + m_41to50
                         + m_over50
                         + m_under10)
        check = age_missing - total_missing
        if check != 0:
            m_31to40 = m_31to40 + check

        # Lists of ID (index) for missing age
        condition = values[values['Age'].isna()]
        to_fill = condition.index.tolist()

        # Generate random ages
        random_ages = randint(10, 18, size=m_10to17).tolist()
        random_ages.extend(randint(18, 31, size=m_18to30).tolist())
        random_ages.extend(randint(31, 41, size=m_31to40).tolist())
        random_ages.extend(randint(41, 51, size=m_41to50).tolist())
        random_ages.extend(randint(51, 70, size=m_over50).tolist())
        random_ages.extend(randint(1, 10, size=m_under10).tolist())

        # Create dictionary
        fill_dict = dict(zip(to_fill, random_ages))

        # Update Dataframe
        titanic_df.update({'Age': fill_dict})

        # Check if all missing values have been replaced
        if (pclass == 3) & (sex == 'male'):  # Last call of the function
            if titanic_df['Age'].isnull().sum() == 0:
                print('Python script: All missing values for column "Age"',
                      'have now been filled.')
            else:
                print('Python script: Some values are still missing for ',
                      'column "Age".\nPlease run the function again.')

    else:
        # Display notification if all missing values for "Age" have been filled 
        if (pclass == 3) & (sex == 'male'):  # Last call of the function
            print('Python script: All missing values for column "Age" have ',
                  'now been filled.')


# Call the "fill_missing_age" function for each passenger group
# Arguments: "passenger class" and "sex"
fill_missing_age(1, 'female')
fill_missing_age(2, 'female')
fill_missing_age(3, 'female')
fill_missing_age(1, 'male')
fill_missing_age(2, 'male')
fill_missing_age(3, 'male')

# Update column "AgeGroup"
age_group_column()
