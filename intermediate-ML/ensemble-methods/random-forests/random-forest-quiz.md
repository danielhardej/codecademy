#### A decision tree regressor was built to predict the selling price of a house and was shown to be overfit. The data has 100 features and 10,000 rows. Fill in the code to train the best new model with appropriate hyperparameters to reduce the overfitting and evaluate the model on the test set.

    from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
    from sklearn import tree
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor


    model = RandomForestRegressor(n_estimators=100, max_features=10)
    model.fit(x_train,y_train)
    model.score(x_test, y_test)


#### Which statement best describes a bootstrapped sample and how is it used in creating a random forest model?

- [ ] Bootstrapped samples are obtained by taking samples without replacement. Each decision tree is built on the full dataset.
- [x] Bootstrapped samples are obtained by taking samples with replacement. Each decision tree is built on a bootstrapped sample.
- [ ] Bootstrapped samples are obtained by taking samples with replacement. Each decision tree is built on the full dataset.
- [ ] Bootstrapped samples are obtained by taking samples without replacement. Each decision tree is built on a bootstrapped sample.

#### How does a random forest regressor make predictions?

- [ ] A random forest regressor uses the most common result from its decision trees as the final prediction.
- [ ] A random forest regressor uses the least common result from its decision trees as the final prediction.
- [x] A random forest regressor uses the average prediction from its decision trees as the final predictions.
- [ ] A random forest regressor uses a random result from its decision trees as the final predictions.

#### What does scikit-learn’s RandomForestClassifier‘s .fit() method do?

- [ ] The .fit() method creates a single DecisionTreeClassifier.
- [x] The .fit() method creates the model according to the training data and training labels.
- [ ] The .fit() method returns the accuracy of the model according to the testing data and testing labels.
- [ ] The .fit() method creates a RandomForestClassifier object.

#### Fill in the code to fit a RandomForestClassifier with n_estimators=50 on the training data (x_train, y_train) and score on the test data (x_test, y_test).

    from sklearn.ensemble import RandomForestClassifier

    rf = RandomForestClassifier(n_estimators=50)
    rf.fit(x_train, y_train)
    rf.score(x_test, y_test)

#### How does a random forest classifier make predictions?

- [ ] A random forest classifier uses the least common classification from its decision trees as the final classification.
- [x] A random forest classifier uses the most common classification from its decision trees as the final classification.
- [ ] A random forest classifier uses the average classification from its decision trees as the final classification.
- [ ] A random forest classifier uses a random classification from its decision trees as the final classifier.

#### How is a random forest model related to a decision tree model?

- [ ] A random forest is a single decision tree that has been trained on a bootstrapped sample of data.
- [ ] A random forest makes a classification by randomly picking one tree from a group of decision trees to make the classification.
- [ ] A random forest is not related to a decision tree model.
- [x] A random forest is an ensemble model that makes a classification by aggregating the results of multiple decision trees.

#### When creating a RandomForestClassifier from scikit-learn, what does the n_estimators parameter represent and what is it’s default value?

- [ ] The number of rows to randomly select when implementing bagging.
- [x] The number of trees in the forest, and the default value is 100.
- [ ] The maximum depth of the trees in the forest.
- [ ] The number of features to consider when implementing feature bagging.

#### If your dataset has n features, what is the default value for the number of features considered at each split in scikit-learn’s RandomForestClassifier?

- [ ] n/3
- [ ] n/2
- [x] sqrt(n)
- [ ] n
