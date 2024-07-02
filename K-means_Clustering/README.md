# K-Means Clustering

HyperionDev - Data Science Skills Bootcamp (Task 23)

The objective of this task was to  group countries using socio-economic and health factors to determine the development status of the country.

### Data Source

Provided dataset: "Country-data.csv"

The data used in this task was originally sourced from Help.NGO. This international non-governmental organisation specialises in emergency response, preparedness, and risk mitigation.  

The dataset attributes include factors such as child mortality, life Expectation, health, number of children per woman in age of procreating, net income and GDP per capita, inflation rates, importations and exportations. 

### Preprocessing and Feature Selection

Using a heatmap and pairplots, we can have an idea of which features look promising for separating into clusters. 

The heatmap shows some expected correlations, such as: 
* Child mortality & Life expectancy
* Income & Life expectancy
* Income & GDPP
* Exports & GDPP
* Imports & Exports

There is also a strong correlation between *total_fer* (i.e. the number of children born to each woman with the current age-fertility rates) and child mortality. A high child mortality is accompanied by a greater number of births for these mothers, indicating the sad reality of needing to have more children, in the hope that some of them reach adulthood.

[Heatmap](https://github.com/vglarde/codingTasks/blob/master/K-means_Clustering/images/heatmap.png)

**Child mortality**
When plotting independant features against Child mortality, the following plots seem to show a strong correlation: 
* GDPP vs Child mortality

* Income vs Child mortality  
  *These two plots have an extremely similar shape.*  

* Exportations vs Child mortality  
  *There is a visible pattern with this plot, and it could be an indicator of child labour.* 

*Note: "Life expectation vs Child mortality" also shows a strong correlation, but it is probably not worth investigating as it is merely stating the obvious: high child mortality is correlated with low lifespan expectation. *

[images/plot_child_mort.png](images/plot_child_mort.png) 

**GDPP**
When plotting independant features against GDPP, the following plots seem to show a strong correlation: 
* Child mortality vs GDPP  
  *This plot shows that high Child mortality is correlated with low GDPP*

* Life expectancy vs GDPP  
  *This plot has a similar shape, but mirrored, indicating a high Life expectancy with a high GDPP.*  

* Health vs GDPP

[images/plot_gdpp.png](images/plot_gdpp.png) 

### K-means clustering

After normalising the data, I used the elbow and silhouette score method in order to find the optimal number of clusters, which appears to be 3. 

[images/elbow_silhouette.png](images/elbow_silhouette.png)

### Visualisation of clusters

The task instructions asked to label the groups of countries based on child mortality, GDPP and inflation. The following [following terms](https://en.wikipedia.org/wiki/Developing_country#Terms_used_to_classify_countries) may be used: "least developed, developing and developed", or "low, low-middle, upper-middle and high income". Alternatively, we could simply rank them from highest to lowest.

With the elements provided in the dataset, we cannot classify them as "least developed, developing, and developed" because we would need more information to refine these criteria.  
(Information such as: access to driking water, sanitation and hygiene, levels of pollution, infrastructures, malnutrition, crime rates, etc.) 

We could classify the groups of countries from highest to lowest, but it may be too vague. 

Since we have access to the average income per capita in the dataset, I used this information to classify our three clusters based on the income (Low, Medium, High).

| Cluster | Count | Average income | Median income | Notes |
|:-------:|:-----:|:--------------:|:-------------:|:-----:|
| Low income | 45 countries | 3,555 | 1,850 | low to low-middle income |
| Medium income | 87 countries | 12,644 | 12,500| middle income |
| High income | 35 countries | 45,800 | 40,400| high-middle to high income |

**Child mortality vs GDPP**

[images/gdpp_n_child_mort.png](images/gdpp_n_child_mort.png) 

This plot shows a strong correlation between Child mortality and GDPP. The higher the GDPP, the less Child mortality per country. As we have already seen, the same trends apply to Income levels. 

We also see that most countries on a low income are concentrated in a small GDPP range (less than £10k), and experience the highest levels of Child mortality. 

Countries on a medium income are more disparate, although still concentrated in a small GDPP range (less than £20k). However, some of them experience the same low level of Child mortality as countries on a high income, whilst others suffer a much higher Child mortality. It could be due to access (or lack of access) to healthcare, sanitation, drinking water, etc.

Most countries on a high income are spread on a broader GDPP range (£20k to £55k), with only four countries over £60k. All these countries experience a low Child mortality.

**Inflation vs GDPP**

[images/gdpp_n_inflation.png](images/gdpp_n_inflation.png) 

This plot shows that countries with a low GDPP (GDP per capita) are more prone to experience higher inflation rates, but GDPP appears to be only one factor among many others, not the main factor explaining inflation rated. We see for example that a significant number of high income countries (around the £40k-mark) experience a similar level of inflation as countries with low and medium income levels.  

The higher inflation rates (including outliers) can often be explained by factors such as wars, civil wars, political turmoil, global oil markets, etc.

A quick look at the 20 countries with the highest inflation rates (see below) corroborates this observation.  
For example:
* Political turmoil (Venezuela, Argentina…)
* Global oil markets (Timor-Leste, Saudia Arabia, Brunei…)
* Civil wars (Sudan, Nigeria, Yemen…)

## Conclusion

As shown on the pairplot below, our model (dividing the countries into three groups, which we have roughly classified as low, medium, and high income) allows us to visualise strong socio-economic trends when the features are plotted against factors on a personal/individual level, such as child mortality, life expectancy, number of children per mother, individual income, and GDPP.

Health is a good example of that. It is strongly correlated with death data (life expectancy and child mortality), as well as personal wealth (income or GDPP), but does not show much valuable trends when analysing economic factors at the national level, such as imports, exports or inflation rates.

Economic-oriented data at the national level (e.g. imports, exports, or inflation rates) also display some interesting trends, but  need to be refined with additional factors in order to become significative.
