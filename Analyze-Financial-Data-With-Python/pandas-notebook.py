import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

# compare purchases of different shoe colors of the same shoe type by creating a pivot table
shoe_counts_pivot = shoe_counts.pivot(
  columns = 'shoe_color',
  index = 'shoe_type',
  values = 'id'
).reset_index()


# ----------------------------------------------------
# Exercise 8/8

user_visits = pd.read_csv('page_visits.csv')

print(user_visits.head(10))

click_source = user_visits.groupby('utm_source').id.count().reset_index()

# calculate the number of visits to our site from each utm_source for each month
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

# create a pivot table where the columns are the utm_source and the rows are the month
click_source_by_month_pivot = click_source_by_month.pivot(
  columns = 'month',
  index = 'utm_source',
  values = 'id'
).reset_index()

print(click_source_by_month_pivot)
