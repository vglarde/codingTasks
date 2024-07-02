# Handling Missing Data

The goal of this task was to create an in-depth EDA on the Titanic dataset provided.

This excerpt shows how I handled missing data for the column *Age*.

In this dataset (list of the Titanic passengers), the age was missing for 19.9% of the 891 passengers: 
* 30 in First class
* 11 in Second class
* 136 in Third class

In order to be as accurate as possible, I started by considering age distributions within specific passenger groups, based on class and gender, and then generating random ages within those distributions. By doing so, this solution maintains the integrity of the data while ensuring a realistic representation of age demographics. 

*Note: A special modification was necessary for the title "Master" (young boys), otherwise there could have been a discrepancy if the title "Master" was associated with an adult.*

Here is my methodology to populate the missing values for the *Age* variable:
1. Calculate the proportion of passengers for six age categories:
    * Under 10 years old (children)
    * 10-17 years old
    * 18-30 years old
    * 31-40 years old
    * 41-50 years old
    * Over 50 years old  
    
    *Note: Based on the demographic of early 20th century, and the demographic of the Titanic passengers, the "older" generation was actually those over 50, with very few passengers over 65 or 70 years old.*  
        
2. Subdivide these categories based on gender (male / female) and travel class, in order to have a more accurate estimation.
3. Then, based on this distribution, fill the missing values with random values **within** the respective age ranges.  

   
This notebook also contains a brief section showing how I handled the missing data for the Port of embarkation, as well as the section of the data analysis specifically related to age groups. 
