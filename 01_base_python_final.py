"""

====================================================================
                B A S E     P Y T H O N     R E F R E S H E R
====================================================================

"""

# ==================================================================
#                           D A T A  T Y P E S
# ==================================================================
"Hello World"
1.1
H
H=1
H="Hello World"

# Integer
type(1)

# Float (with the decimal)
type(1.1)

# String (either single ('') or double ("") quotes may be used)
type("Data Science")
type('Data Science')

# Boolean
type(False)
false 
# You can convert between datatypes

H = 2.0
H = int(H)

int(1.0)
float(1)
int("1")
str(1.0)

# ==================================================================
#                           O P E R A T I O N S
# ==================================================================

var1 = 3
var2 = 10

# Boolean Operators
var1 == var2            # EQUAL TO
var1 <  var2            # LESS THAN
var1 <= var2            # LESS THAN OR EQUAL TO        
(var1 == 1) | (var2 == 10)      # OR
(var1 == 1) or (var2 == 10)     # OR (alternative)
(var1 == 1) & (var2 == 10)      # AND
(var1 == 1) and (var2 == 10)    # AND (alternative)

# Addition
10 + 3

# Subtraction
10 - 3

# Multiplication
10 * 3

# Division
10 / 3          # returns 3 in Python 2.x
10 / 3.0        # returns 3.333...
10 / float(3)   # returns 3.333...

# Powers
10**3

# Remainders
10 % 3

# ==================================================================
#           L I S T S :  Mutable, Ordered Data Structures
# ==================================================================

# Lists are denoted by []
lis=[0, 'a', 2, 3, 4, 5, 6, 7]
type(lis)
lis[1]

# Specific elemnents can be accessed using [] as well
lis[6] # Returns the 7th element

# Multiple elements can be accessed using the ':' operator
# Returns the 1st number through one shy of the 5th number
lis[0:4]
# Returns the 5th element through the last element
lis[4:]

# Returns the first through the 4th element
lis[:4]

# Returns the last element
lis[-1]

# Returns the last 3 elements
lis[-3:]

# List elements are mutable
lis[4] = 100
lis[4:6] = [500, 600]

lis2 = ['cool', 'stuff']

# The type of list elements is also mutable
lis[0:3] = ["Guido", "Van", "Rossum"]
lis[3:7] = ["created", "python,", "programming", "language,"]

# Check if an element is in a list
"Van" in lis    # returns True

# Elements can be removed with the .remove method
lis.remove(7)

# Elements can be added with the .append method
lis.append(7)

# Another way to remove, by location not value
lis = lis[:-1]
lis.append("in 1991")

# Elements can be inserted into the middle of a list
lis.insert(5,'a')

# Learn more about a function by entering a ? infront of it
?lis.insert()

# Lists can be nested within each other
lis = [[1,2],[3,4]]

# We would use the following to access the 3
lis[1][0]

# List of three lists
lis = [[1,2,3],[4,5,6],[7,8,9]]

# Lets try to access a particular number, say 6
lis[1][2]

# A list within a list  within a list within a list within a list
lis = [1,2,[3,4,[5,6,[7,8]]]]

# Lets try to access a particular number, say 6 again
lis[2][2][1]

# ==================================================================
#                            S T R I N G S
# ==================================================================

# Example strings
s1 = "What is the air-speed velocity"
s2 = "of an unladen swallow?"

# Concatenate two strings
s = s1 + " " + s2
s = ' '.join([s1,s2])

# Replace an item within a string
s = s.replace("unladen", "unladen African")

# Return the index of the first instance of a string
s.find("swallow")

# Slice the string
s[53]
s[53:]
s[s.find("swallow"):]
s[-8:]

# Change to upper and lower case
s.upper()
"SWALLOW".lower()
"swallow".capitalize()

# Count the instances of a substring
s.count(" ")

# Find the length of a string
len(s)

# Split up a string (returns a list)
s.split()
s2 = s.split("an") # Same thing

list_words = s.split(' ')
word_count = len(list_words)

len(s.split(' '))

# Web scraping example

# Obama Fack News Example
# https://hackernoon.com/what-real-fake-news-says-about-obamas-presidency-4bf42be71ff1


# ==================================================================
#      D I C T: Unordered data structures with key-value pairs
#               Keys must be unique
# ==================================================================

dct = {"Name": "Monty Python and the Flying Circus",
       "Description": "British Comedy Group",
       "Known for": ["Irreverant Comedy", "Monty Python and the Holy Grail"],
       "Years Active" : 17,
       "# Members": 6}
       
# Access an element within the list
dct["Years Active"] = 18

# Add a new item to a list within the dictionary
dct["Known for"].append("Influencing SNL")

# Accessing a nested dictionary item - "Monty Python and the Holy Grail"
dct['Known for'][0][0]

# Returns the keys
dct.keys()

# Returns the values
dct.values()

# Create a dictionary within the 'dct' dictionary 
dct['Influence'] = 0
dct["Influence"] = { "Asteroids": [13681, 9618, 9619, 9620, 9621, 9622], 
                     "Technology": ["Spam", "Python", "IDLE (for Eric Idle)"],
                     "Food": ["Monty Python's Holy Ale", "Vermonty Python"]}

dct.keys()
dct['Influence'].keys()
                   
# Lets try to access a particular number again, say 9620
dct['Influence']['Asteroids'][3]

# GOOGLE API EXAMPLE


# ==================================================================
#                      D A T A   F R A M E S
# ==================================================================

# Example data frame
import pandas as pd

pd.

df = pd.DataFrame({'example1':[18,24,17,21,24,16,29,18],\
                   'example2':[75,87,49,68,75,84,98,92],\
                   'example3':[55,47,38,66,56,64,44,39]})

# Print the first/last X rows of data
df.head()
df.head(3)
df.tail()

# Get summary statistics for your dataset
df.describe()
df['example2'].describe()

# Identify a specific column / row of data
df['example2'] = df['example2'].astype('str')
df.loc[0,'example1'] = 19
df.loc[0:2,:]
df.loc[0:2,'example2']

# Write a dataset to a csv file
df.to_csv(r'C:\Users\jsokoll\Desktop\examples.csv', index=False)

# Import 
path = r'C:\Users\jsokoll\Desktop\examples.csv'

df2 = pd.read_csv(path)
pd.read
pd.read_table(path,sep='/t')


# ==================================================================
#           I F - S T A T E M E N T S   &   L O O P I N G
# ==================================================================

var1 = 0

# If elif else statement
# Whitespace is important
if var1 > 5:
    print("More than 5")
elif var1 < 5:
    if var1 > 3:
        print("Less than 5 but > 3")
    else:
        print("Less than 3")
else:
    print("5")

# While statement
var1=0
while var1 < 10:
    print(var1)
    var1 += 1   # This is commonly used shorthand for var1 = var1 + 1

    
# For loop
for x in list(range(0,10,1)):
    print(x**2)
    

# For loop in the list
fruit = ['apple', 'banana', 'cherry', 'plum']
upper = []

for i in fruit:
    upper.append(i.upper())
    

# List Comprehension
upper = [i.upper() for i in fruit]
    
# For loop with some complexity    
price = [3,1,.5,10]
color = ['red','yellow','red','purple']

for n,i in enumerate(fruit):
    print('The '+color[n]+' '+i+' costs '+str(price[n])+' dollars.')
    
# Throwback to data frames
import pandas as pd

d = pd.DataFrame(0.0,columns=['fruit','price','color'],\
                 index=list(range(len(fruit))))
d['fruit'] = fruit
d['price'] = price
d['color'] = color
d['origin'] = 0

# Try writing a for loop that fills the origin column with:
# 'Maryland' if the color is 'red' otherwise 'Virginia'


# ==================================================================
#           T H E   W O R K I N G    D I R E C T O R Y
# ==================================================================


import os

# Check the current working directory
os.getcwd()

# Change the current directory
os.chdir('..')
os.chdir('Desktop')

# List files in current directory
os.listdir()