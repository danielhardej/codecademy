# Create a DataFrame I

import codecademylib3
import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  "Product Name" : ["t-shirt", "t-shirt", "skirt", "skirt"],
  "Color" : ["blue", "green", "red", "black"]

})

print(df1)

# Create a DataFrame II

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3,	'San Francisco',	90],
  [4,	'Sacramento',	115]
  ],
  columns=["Store ID",	"Location",	"Number of Employees"])

print(df2)

# Comma Separated Variables (CSV)
# Loading and Saving CSVs: When you have data in a CSV, you can load it into a DataFrame in Pandas using .read_csv()
df = pd.read_csv('sample.csv')
print(df)

# Inspect a DataFrame
df = pd.read_csv('imdb.csv')
print(df.head())
print("\n-----\n")
print(df.info())

# Selecting a Column
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df['clinic_north']
print(type(clinic_north))           # <class 'pandas.core.series.Series'>
print(type(df))                     # <class 'pandas.core.frame.DataFrame'>

# Selecting Multiple Columns

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north_south = df[['clinic_north', 'clinic_south']]

print(type(clinic_north_south))        # <class 'pandas.core.frame.DataFrame'>

# Select Rows

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march = df.iloc[2]


# Output:
# month           March
# clinic_east        81
# clinic_north       96
# clinic_south       65
# clinic_west        96
# Name: 2, dtype: object

# Selecting Multiple Rows

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

april_may_june = df.iloc[3:6]
print(april_may_june)

# Select Rows with Logic I
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

january = df[df.month == 'January']
print(january)

	# month	clinic_east	clinic_north	clinic_south	clinic_west
	# January	100	        100	            23	            100

# Select Rows with Logic II
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march_april = df[(df.month == 'March') | (df.month == 'April')]
print(march_april)

# output:
# month	clinic_east	clinic_north	clinic_south	clinic_west
# March	81	        96	            65	            96
# April	80	        80	            54	            180

# Select Rows with Logic III
df = pd.DataFrame([
    ['January', 100, 100, 23, 100],
    ['February', 51, 45, 145, 45],
    ['March', 81, 96, 65, 96],
    ['April', 80, 80, 54, 180],
    ['May', 51, 54, 54, 154],
    ['June', 112, 109, 79, 129]],
    columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

january_february_march = df[df.month.isin(['January', 'February', 'March'])]

print(january_february_march)

# output:
# month	    clinic_east	clinic_north	clinic_south	clinic_west
# January	100	        100	            23	            100
# February  51	        45	            145	            45
# March	    81	        96	            65	            96

# Setting indices  
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

df2 = df.loc[[1, 3, 5]]
print(df2.reset_index(drop=True))
# Output:
# month	    clinic_east	clinic_north	clinic_south	clinic_west
# February	51	        45	            145	            45
# April	    80	        80	            54	            180
# June	    112	        109	            79	            129

df3 = df2.reset_index()
print(df3)
# Output:
# index	month	    clinic_east	clinic_north	clinic_south	clinic_west
# 	1	February	51	        45	            145	            45
# 	3	April	    80	        80	            54	            180
# 	5	June	    112	        109	            79	            129

# Review
orders = pd.read_csv('shoefly.csv')     # Load the data from shoefly.csv into the variable orders.
print(orders.head(5))                   # Inspect the first 5 rows of the data.

emails = orders['email']                # Select the email column from orders and save it to the variable emails.
print(emails)

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]  # Select all orders from Frances Palmer and save it to the variable frances_palmer.
print(frances_palmer)

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]             # Select all orders for shoes of type 'clogs', 'boots', or 'ballet flats' and save it to the variable comfy_shoes.
print(comfy_shoes)