import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv("tennis_stats.csv")
#print(df.shape)
#print(df.head(10))

# perform exploratory analysis here:
# x = df['FirstServeReturnPointsWon']
x = df['BreakPointsOpportunities']
x = x.values.reshape(-1, 1)
y = df['Winnings']
# plt.scatter(x, y, alpha=0.4)
# plt.show()

## perform single feature linear regressions here:
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

lrm = LinearRegression()
lrm.fit(x_train, y_train)
y_pred = lrm.predict(x_test)

plt.scatter(y_test, y_pred, alpha=0.4)
plt.show()
print("Single feature test score:")
print(lrm.score(x_test, y_test))

## Residual Analysis
# residuals = y_pred - y_test
# plt.scatter(y_pred, residuals, alpha=0.4)
# plt.title('Residual Analysis')
# plt.show()

## perform two feature linear regressions here:
x = df[['BreakPointsOpportunities', 'FirstServePointsWon']]
y = df['Winnings']
# plt.scatter(x, y, alpha=0.4)
# plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

lrm = LinearRegression()
lrm.fit(x_train, y_train)
y_pred = lrm.predict(x_test)

plt.scatter(y_test, y_pred, alpha=0.4)
plt.show()
print("Two feature test score:")
print(lrm.score(x_test, y_test))


## perform multiple feature linear regressions here:
x = df[['FirstServe','FirstServePointsWon','FirstServeReturnPointsWon',
'SecondServePointsWon','SecondServeReturnPointsWon','Aces',
'BreakPointsConverted','BreakPointsFaced','BreakPointsOpportunities',
'BreakPointsSaved','DoubleFaults','ReturnGamesPlayed','ReturnGamesWon',
'ReturnPointsWon','ServiceGamesPlayed','ServiceGamesWon','TotalPointsWon',
'TotalServicePointsWon']]
y = df[['Winnings']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

lrm = LinearRegression()
lrm.fit(x_train, y_train)
y_pred = lrm.predict(x_test)

plt.scatter(y_test, y_pred, alpha=0.4)
plt.show()
print("Test score:")
print(lrm.score(x_test, y_test))
