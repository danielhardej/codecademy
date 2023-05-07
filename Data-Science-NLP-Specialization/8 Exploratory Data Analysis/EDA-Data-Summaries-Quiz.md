# EDA: Data Summaries Quiz

## Exploratory Data Analysis with Python

#### A pandas dataframe named students has a column named subject that contains information about what subject each student is studying. Fill in the code to create a bar chart of the number of students who are studying each subject.

``` python
import matplotlib.pyplot as plt
import seaborn as sns
 
# create bar chart
sns.countplot(x = 'subject', data = students)
plt.show()
```

#### Fill in the code to simultaneously calculate summary statistics for all columns (features) in a pandas dataframe named df.

``` python 
df.describe(include = 'all')
```

#### A pandas dataframe named students has a column named subject that contains information about what subject each student is studying. Fill in the code to calculate the proportion of students who are studying each subject.

``` python
students.subject.value_counts(normalize = True)
```

#### Which of the following visualizations is used to inspect the distribution of a continuous quantitative variable?

 - [x] histogram
 - [ ] bar chart
 - [ ] pie chart

#### A dataframe named births contains a column named weight, which contains the birth weight (to the nearest half-pound) of babies. Fill in the code below to calculate the variance, standard deviation, and mean absolute deviation of birth weight.

``` python
# calculate variance
births.weight.var()
 
# calculate standard deviation
births.weight.std()
 
# calculate MAD
births.weight.mad()
```

#### A dataframe named survey has a column named income that contains income data for a sample of adults. Fill in the code to create a boxplot for income.

``` python
import matplotlib.pyplot as plt
import seaborn as sns
 
# create boxplot
sns.boxplot(x = 'income', data = survey)
plt.show()
```

#### Which of the following can be used to summarize the spread of a quantitative feature?

 - [ ] mean
 - [x] standard deviation
 - [ ] median
 - [ ] trimmed mean

#### A pandas dataframe named students has a column named score that contains test scores for a sample of students. Fill in the code below to calculate the range and interquartile range of test scores.

``` python
range = students.score.max() - students.score.min()
 
iqr = students.score.quantile(0.75) - students.score.quantile(0.25)
```

#### A dataframe named births contains a column named weight, which contains the birth weight (to the nearest half-pound) of babies. Fill in the code below to calculate the mean, median, and mode birth weight of babies in this dataset.

``` python
# calculate mean
births.weight.mean()
 
# calculate median
births.weight.median()
 
# calculate mode
births.weight.mode()
```
