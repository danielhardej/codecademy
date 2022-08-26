import codecademylib3
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

#https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data
cols = ['name','landmass','zone', 'area', 'population', 'language','religion','bars','stripes','colours',
'red','green','blue','gold','white','black','orange','mainhue','circles',
'crosses','saltires','quarters','sunstars','crescent','triangle','icon','animate','text','topleft','botright']
df= pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data", names = cols)

#variable names to use as predictors
var = [ 'red', 'green', 'blue','gold', 'white', 'black', 'orange', 'mainhue','bars','stripes', 'circles','crosses', 'saltires','quarters','sunstars','triangle','animate']

#Print number of countries by landmass, or continent
print(df.landmass.value_counts())

#Create a new dataframe with only flags from Europe and Oceania
df_36 = df[df["landmass"].isin([3,6])]

#Print the average vales of the predictors for Europe and Oceania
print(df_36.groupby('landmass')[var].mean().T)

#Create labels for only Europe and Oceania
df_36 = df[df["landmass"].isin([3,6])]
labels = df_36["landmass"]

#Print the variable types for the predictors
print(df[var].dtypes)

#Create dummy variables for categorical predictors
data = pd.get_dummies(df_36[var])

#Split data into a train and test set
x_train, x_test, y_train, y_test = train_test_split(data, labels, random_state=1, test_size=.4)

#Fit a decision tree for max_depth values 1-20; save the accuracy score in acc_depth
depths = range(1, 21)
acc_depth = []
for depth in depths:
  dt = DecisionTreeClassifier(max_depth=depth)
  dt.fit(x_train, y_train)
  dt_score = dt.score(x_test, y_test)
  acc_depth.append(dt_score)

#Plot the accuracy vs depth
plt.scatter(depths, acc_depth)
plt.xlabel("Tree Depth")
plt.ylabel("Accuracy")
plt.show()

#Find the largest accuracy and the depth this occurs
best_acc = np.max(acc_depth)
best_acc_idx = acc_depth.index(best_acc)
best_depth = depths[best_acc_idx]
print(best_acc, best_depth)

#Refit decision tree model with the highest accuracy and plot the decision tree
dt_best = DecisionTreeClassifier(max_depth=best_depth, random_state = 1)
dt_best.fit(x_train, y_train)
plt.figure()
tree.plot_tree(dt_best, feature_names=x_train.columns, class_names=['Europe', 'Oceania'], filled=True)
plt.show()

#Create a new list for the accuracy values of a pruned decision tree.  Loop through
acc_pruned = []
ccp = np.logspace(-3, 0, num=20)
for c in ccp:
  dt_pruned = DecisionTreeClassifier(random_state=1, max_depth=best_depth, ccp_alpha=c)
  dt_pruned.fit(x_train, y_train)
  dt_pruned_score = dt_pruned.score(x_test, y_test)
  acc_pruned.append(dt_pruned_score)

#Plot the accuracy vs ccp_alpha
plt.figure()
plt.plot(ccp, acc_pruned)
plt.xscale('log')
plt.xlabel('ccp alpha')
plt.ylabel('accuracy')
plt.show()

#Find the largest accuracy and the ccp value this occurs
best_acc_pruned = np.max(acc_pruned)
best_acc_pruned_idx = acc_pruned.index(best_acc_pruned)
best_ccp_alpha = ccp[best_acc_pruned_idx]
print(best_acc_pruned, best_ccp_alpha)

#Fit a decision tree model with the values for max_depth and ccp_alpha found above
dt_best_pruned = DecisionTreeClassifier(random_state=1, max_depth=best_depth, ccp_alpha=best_ccp_alpha)
dt_best_pruned.fit(x_train, y_train)

#Plot the final decision tree
plt.figure(figsize=(10,5))
tree.plot_tree(dt_best_pruned, feature_names=x_train.columns, class_names=['Europe', 'Oceania'], filled=True)
plt.show()
