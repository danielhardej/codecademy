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


# ----------------------------------------------------

import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')


clicks_by_utm = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(clicks_by_utm)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head(10))

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  index='utm_source',
  columns='is_click',
  values='user_id'
).reset_index()
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

# The column experimental_group tells us whether the user was shown Ad A or Ad B.
# Were approximately the same number of people shown both adds?
print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']


# Using the column is_click, check to see if a greater percentage of users clicked on Ad A or Ad B.
ad_clicks.groupby(['is_click', 'experimental_group']).user_id.count().reset_index()


a_clicks_by_day = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
b_clicks_by_day = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()