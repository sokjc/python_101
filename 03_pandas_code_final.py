'''
Python 101

Spyder Reference (Windows):
    Ctrl + Enter    (in the editor):        Runs the line of code
    Ctrl + L        (in the console):       Clears the console
    Up/Down-arrows  (in the console):       Retreives previous commands
    Ctrl + S        (in the editor):        Saves the file              
'''

'''
Reading, Summarizing data
'''



import pandas as pd  # This line imports  (already installed) python package


url = r'https://raw.githubusercontent.com/justmarkham/DAT7/master/data/drinks.csv'
drinks = pd.read_table(url, sep=',')


#BELOW ALSO WORKS
csv = r'C:\Users\jsokoll\Desktop\python_101\data\drinks_data.csv'
drinks = pd.read_table(csv, sep=',')


drinks                
drinks.head()          # Look at the top x observations
drinks.tail()            # Bottom x observations (defaults to 5)
drinks.describe()        # describe any numeric columns (unless all columns are non-numeric)
drinks.index             # "the index" (aka "the labels")
drinks.columns           # column names (which is "an index")
drinks.shape 			  # gives us a tuple of (# rows, # cols)
drinks.dtypes            # data types of each column
drinks.values            # underlying numpy array


drinks.columns[1]
drinks.shape[0]
drinks.values[0]
drinks.values[0][0]

# DataFrame vs Series, selecting a column
type(drinks)
drinks['country_of_origin']
drinks.country            # Must use the [''] notation if column name has a space
type(drinks.country)

'''
EXERCISE ONE
'''
# read iris_data.csv into a DataFrame called 'iris'
csv = r'C:\Users\jsokoll\Desktop\python_101\Data\iris_data.csv'
iris = pd.read_table(csv, sep=',')

# print thefirst and last 20 records
iris.head(20)
iris.tail(20)

# examine the shape of the data and the descriptive statistics for all columns
iris.shape
iris.describe()

# print the 'sepal_length' column
iris['sepal_length']

# ADVANCED: print the 'sepal_length' and 'sepal_width' columns at the same time
iris[['sepal_length','sepal_width']]

iris[:5]

'''
RESUME LESSON
'''
# summarizing a non-numeric column
drinks.continent.describe()        # Only works for non-numeric if you don't have any numeric data 
drinks.continent.value_counts()    # Valuable if you have numeric columns, which you often will
drinks.continent.value_counts() / drinks.shape[0] # Values divided by number of records

drinks['continent'].fillna(value='NA',inplace=True)

'''
Slicing / Filtering / Sorting
'''

drinks.head()				# Sanity check, nothing has changed!

# selecting multiple columns
drinks[['country', 'beer_servings','wine_servings']]
my_cols = ['country', 'beer_servings']
drinks[my_cols]
type(drinks[my_cols])

# loc: filter rows by LABEL, and select columns by LABEL
drinks.loc[0:9,'country']                            # row with label 1
drinks.loc[:3,:]                           # rows with labels 1 through 3
drinks.loc[0:3, 'country':'wine_servings']   # rows 1-3, columns 'country'through'wine_servings'
drinks.loc[:, 'country':'wine_servings']     # all rows, columns 'country' through 'wine_servings'
drinks.loc[[1,3], ['country','wine_servings']]  # rows 1 and 3, columns 'country' and 'wine_servings'

drinks[['country','wine_servings']][0:3]    #another option
    
1!=2
    
# logical filtering
len(drinks[drinks['continent'] == 'EU'])

country_EU = drinks[drinks['continent'] == 'EU']
country_EU['country']

drinks[drinks['continent'] == 'EU']['country']


drinks[(drinks['continent'] == 'EU') | (drinks['continent'] == 'AS')]
drinks_italy = drinks[(drinks['continent'] == 'EU') & (drinks['country'] == 'Italy')]
drinks[drinks['wine_servings']>300]
drinks[drinks['country'].isin(['Andorra','France','Portugal'])]

drinks[(drinks['continent']=='EU') & (drinks['beer_servings']<100)]



drinks['top_3'] = 0

count = 0

for n,item in enumerate([0,7,5,4]):    
    print(n)

if 5==5:
    print('success')

for n,item in enumerate(drinks['country']):
    if item in ['Andorra','France','Portugal']:        
        drinks.loc[n,'top_3'] = 1

drinks['wine_servings'].mean()
drinks[drinks['top_3']==1]['wine_servings'].mean()
drinks[drinks['top_3']==1]['wine_servings'].sum() / drinks['wine_servings'].sum()
drinks['wine_servings'].median()


drinks.groupby('continent')['beer_servings'].sum()
drinks.groupby('continent')['beer_servings'].mean()
drinks.groupby('continent')['beer_servings'].max()  # select the max
drinks.groupby('continent')['beer_servings'].min()  # select the group min
drinks.groupby('continent')['beer_servings'].agg(['mean','max', 'min']) # select several group metrics



'''
EXERCISE TWO
'''
# read iris_target.csv into a DataFrame called 'iris_target'
csv = r'C:\Users\araveret\Desktop\python_101\iris_target.csv'
iris_target = pd.read_table(csv, sep=',')
iris_target.head()

# create a new column in the iris dataset called 'species' set equal to the 
# species column in the iris_target dataset 
iris['species'] = 0
iris['species'] = iris_target['species']
iris.head()

# filter DataFrame to calculate the average of each sepal and petal measurement
# for each species type (hint there are many ways to do this)
iris.groupby('species')[['sepal_length','sepal_width','petal_width',\
'petal_length']].agg(['mean','max', 'min']) # select several group metrics

iris.groupby('species')[['sepal_length','sepal_width','petal_width',\
'petal_length']].describe()

# examine the data a little further by running a describe function for each
# species types
iris[iris['species']=='setosa'].describe()


# CREATE CSV
iris.to_csv(output_csv, index=False)  # create a csv, without an index series 



'''
IF TIME ALLOWS: EXERCISE 3
'''
### VISUALIZATION
import matplotlib.pyplot as plt

# increase default figure and font sizes for easier viewing
plt.rcParams['figure.figsize'] = (12, 9)
plt.rcParams['font.size'] = 10

# histogram of Beer Servings
?drinks.plot
drinks['beer_servings'].plot.hist(title='Histogram of beer servings')
plt.xlabel('Beer Servings')
plt.ylabel('Frequency')

# scatterplot of beer versus wine
drinks.plot.scatter(x='beer_servings', y='wine_servings')


# use group to compare drinks across continents
drinks.groupby('continent').mean().plot.bar()




'''
IF TIME ALLOWS: EXERCISE 4
'''

from sklearn.cluster import KMeans
import numpy as np

# ------------------------------------------
# EXERCISE: Compute the centoid of the following data
#           [2, 5], [4, 4], [3, 3]
# ------------------------------------------

d = np.array([[2, 5], [4, 4], [3, 3]])
x, y = d.mean(axis=0)

np.random.seed(0)

# Run KMeans
est = KMeans(n_clusters=3, init='random')
est.fit(iris[['sepal_length','sepal_width','petal_length','petal_width']])
y_kmeans = est.predict(iris[['sepal_length','sepal_width','petal_length','petal_width']])


# Create a scatter plot across two dimension
colors = np.array(['#FF0054','#FBD039','#23C2BC'])
plt.figure()
plt.scatter(np.array(iris['petal_length']), np.array(iris['sepal_length']), c=colors[y_kmeans], s=50)
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[0])

# ------------------------------------------
# EXERCISE: Find the centers and plot them 
#           on the same graph.
# ------------------------------------------

centers = est.cluster_centers_
plt.scatter(centers[:, 2], centers[:, 0], c='k', linewidths=3,
            marker='+', s=300)





