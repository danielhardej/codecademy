#### How does recursive feature selection (RFE) select features?

- [ ] RFE removes one feature at a time by testing a model on every possible feature removal.
- [ ] RFE either adds or removes one feature at a time by evaluating feature importance.
- [ ] RFE ranks features by variance and removes features with low variance.
- [x] RFE uses an importance metric to rank features and removes the least important feature at every step.

#### Fill in the code to create an RFE object that selects 3 features and fits it to data. Here X contains the predictor variables, y is the outcome variable, and ‘lr' is a machine learning model.

    rfe = RFE(estimator=lr, n_features_to_select=3)
    rfe.fit(X, y)

#### Fill in the code so that it will implement sequential backward selection. Here lr is a logistic regression model with several features.

    from mlxtend.feature_selection import SequentialFeatureSelector as SFS
    model = SFS(lr, forward=False, floating=False)

#### Say that you have used the mlxtend library to implement a sequential forward selection model called sfs. Here is the output of the line print(sfs.subsets_).

    {1: {'feature_idx': (2,),
    'cv_scores': array([0.70343714]),
    'avg_score': 0.7034371491671395
    'feature_names': ('GPA',)},
    2: {'feature_idx': (2, 5)
    'cv_scores': array([0.89500705]),
    'avg_score': 0.8950070465228014,
    'feature_names': ('GPA', 'SAT score')}}

#### Which of the following statements is FALSE?

- [ ] SAT score was the second feature chosen by sequential forward selection.
- [ ] GPA was the first feature chosen by sequential forward selection.
- [ ] The accuracy of the model with the first two features is about 89.5%.
- [x] Sequential forward selection chose 5 features in total.

#### True or false: It is sometimes necessary to standardize data before using recursive feature selection.

- [x] True.
- [ ] False.

#### True or false: Sequential backward floating selection works mainly by adding features, but it can sometimes remove features at intermediate steps.

- [ ] True.
- [x] False.

#### Why are wrapper methods sometimes preferable to filter methods?

- [ ] Wrapper methods do NOT detect relationships between features.
- [ ] Wrapper methods are usually more efficient than filter methods.
- [x] Wrapper methods evaluate features based on how they perform in a specific machine learning model.
- [ ] Wrapper methods are greedy algorithms.

#### Which of the following statements about sequential forward floating selection (SFFS) is FALSE?

- [ ] SFFS is a greedy algorithm.
- [ ] SFFS can add a feature.
- [x] SFFS starts with all available features.
- [ ] SFFS can remove a feature.

#### Which of the following statements about sequential backward selection (SBS) is FALSE?

- [ ] SBS tests the performance of a machine learning model on different feature subsets.
- [ ] SBS is a greedy algorithm.
- [ ] SBS removes one feature at a time.
- [x] SBS works by removing features with the smallest regression coefficients.

#### Which of the following statements is FALSE?

- [ ] Sequential selection algorithms (e.g., sequential forward selection) can be used to select features for logistic regression models.
- [x] Logistic regression models automatically incorporate feature selection.
- [ ] Recursive feature elimination can be used to select features for logistic regression models.
- [ ] Logistic regression models predict the probability that observations belong to a specific class.

#### Which of the following statements is true?

- [x] Wrapper methods choose features by evaluating the performance of a machine learning model on different feature subsets.
- [ ] Wrapper methods choose features by “wrapping” each feature in an array of numbers.
- [ ] Wrapper methods choose features by evaluating the features directly, independent of any machine learning model.
- [ ] Wrapper methods choose features automatically as a machine learning model is trained.

#### Say that you have used the scikit-learn library to implement a recursive feature elimination model called rfe. You also have a list of features:

    [“Games Played”, “Goals”, “Assists”, “Points”, “+/-”, “Penalty Minutes”]

#### Here is the output of the line print(rfe.support_).

    [False True False True False True]

#### What feature set did the recursive feature selection algorithm choose?

- [ ] There is not enough information to tell.
- [ ] [“Games Played”, “Assists”, “+/-”]
- [ ] [“Games Played”, “Goals”, “Assists”, “Points”, “+/-”, “Penalty Minutes”]
- [x] [“Goals”, “Points”, “Penalty Minutes”]

#### How many features does the sequential forward selection algorithm start with?

- [ ] All available features.
- [x] Zero features.
- [ ] One feature.
- [ ] k features, where k is a variable that you set before implementing the algorithm.

#### Fill in the code that will fit a logistic regression regression model and print its accuracy. Here X contains the predictor variables and y is the outcome variable.

    lr = LogisticRegression()
    lr.fit(X, y)
    print(lr.score(X, y))
