#### A decision tree classifier with default parameters was shown to be overfit to the data. The final depth of the tree was 8. Fill in the code to train a new decision tree model with appropriate hyperparameters to reduce the overfitting and plot the tree with feature labels.

    from sklearn.tree import DecisionTreeClassifier
    from sklearn import tree

    dtree = DecisionTreeClassifier(max_depth='5', min_impurity_decrease='0.05')
    dtree.fit(x_train,y_train)

    tree.plot_tree(dtree, feature_names = 'x_train.columns',  
                class_names = 'y_train.values',filled=True);

#### Which of the following datasets has the smallest Gini impurity?

- [ ] A set of 100 objects — 20 label A, 80 have label B.
- [ ] A set of 100 objects — 50 label A, 50 have label B.
- [x] A set of 100 objects — 5 label A, 95 have label B.
- [ ] A set of 100 objects — 10 label A, 90 have label B

#### Why is the algorithm used to construct decision trees considered a greedy algorithm?

- [ ] The algorithm takes as much time as it needs to find the globally optimal solution.
- [x] The algorithm doesn’t look ahead. It chooses to split the data based on the best possible feature given the current dataset.
- [ ] Because the algorithm is recursive, it requires more processing power.
- [ ] The algorithm is difficult to implement.

#### Which of the following statements about the decision tree implementation in scikit-learn is TRUE?

- [ ] Setting min_impurity_decrease=0 will mean the tree will never stop be built.
- [ ] Using max_depth=None always results in the best tree.
- [x] max_depth, criterion, min_impurity_decrease, and min_samples_leaf can all be tuned which can result in better tree performance.
- [ ] The default criterion is entropy.

#### Suppose the following binary features are available in a dataset to predict employee attrition. The information gain for each is computed in the table on the initial dataset.

    Index	Feature	                          info_gain
    0	    BusinessTravel_Non-Travel	        0.004418
    1	    BusinessTravel_Travel_Frequently	0.004921
    2	    BusinessTravel_Travel_Rarely	    0.000490
    3	    Department_Human Resources	      0.000060
    4	    Department_Research & Development	0.004516
    5	    Department_Sales	                0.004347
    6	    Gender_Female	                    0.000541
    7	    Gender_Male	                      0.000541

##### What is the first split in the tree?

- [ ] Department_Human Resources
- [ ] BusinessTravel_Non-Travel
- [x] BusinessTravel_Travel_Frequently
- [ ] Gender_Female or Gender_Male

#### The following tree was built on the IBM attrition data set, predicting what employees will stay or leave within the year. What is the information gain when slitting at the node Age<=24?

- [x] 0.125
- [ ] 0.375
- [ ] 0.366
- [ ] 0.134

#### The following tree was built on the IBM attrition data set, predicting what employees will stay or leave within the year. What is the predicted value for an employee with NumCompaniesWorked=5, TotalWorkingYears = 2, DistanceFromHome = 5, and Age=22 and what is the Gini impurity of the final leaf?

- [ ] Stay, 0.423
- [ ] Quit, 0.153
- [x] Quit, 0.305
- [ ] Quit, 0.399

#### The following tree was built on the IBM attrition data set, predicting what employees will stay or leave within the year. What is the initial Gini impurity of the dataset (stay vs quit) and what split maximizes the information gain on this set?

- [ ] 0.415, DistanceFromHome
- [x] 0.454, TotalWorkingYears
- [ ] 0.423, NumCompaniesWorked
- [ ] 0.468, TotalWorkingYears

#### Fill in the code to fit a DecisionTreeClassifier with max_depth=5 on the training data (x_train, y_train) and score on the test data (x_test, y_test).

    from sklearn.tree import DecisionTreeClassifier

    dtree = DecisionTreeClassifier('max_depth=5')
    dtree.fit('x_train', 'y_train')
    dtree.score('x_test', 'y_test')

#### What does scikit-learn’s DecisionTreeClassifier‘s .fit() method do?

- [ ] The .fit() method creates a DecisionTreeClassifier object.
- [ ] The .fit() method returns the accuracy of the tree according to the testing data and testing labels.
- [ ] The .fit() method creates a random forest of DecisionTreeClassifiers.
- [x] The .fit() method creates the tree according to the training data and training labels.
