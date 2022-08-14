#### Fill in the code to create a dictionary called search_spaces for use with BayesSearchCV(). Use a categorical distribution for penalty. For C, use a uniform distribution between 1 and 5.

    from skopt.space import Categorical, Real

    search_spaces = {'penalty': Categorical(['l1', 'l2']), 'C': Real(1, 5, prior='uniform')}

#### Which of the following options best describes the grid search algorithm?

- [ ] Grid search tests a machine learning algorithm on randomly chosen hyperparameters.
- [ ] Grid search works by guessing how hyperparameters affect model performance. It then iterates through several hyperparameters values, testing them and updating its guess at every step.
- [x] Grid search tests a machine learning algorithm on a specific list of hyperparameters.

#### Below is some code and an output.

    parameters = {'kernel': ['linear', 'poly', 'rbf'], 'C': [1, 10, 100]}
    svc = SVC()

    clf = GridSearchCV(svc, parameters)
    clf.fit(X_train, y_train)

    print(clf.best_estimator_)
    SVC(kernel='poly', C=10)

#### Based on the code and the output, which of the following statements is FALSE?

- [x] Hyperparameters were tested by choosing random values for kernel and C.
- [ ] Of the hyperparameter values that were tested, the SVC() model performed best with kernel=’poly’ and C=10.
- [ ] Nine different hyperparameter combinations were tested: three different values for kernel times three different values for C.

#### Fill in the code that will print the model’s score on cross-validation data.

    clf = BayesSearchCV(estimator=model, search_spaces=search_spaces)
    clf.fit(X_train, y_train)

    print(clf.best_score_)

#### Fill in the code to create a RandomizedSearchCV model called rand_search that uses the model clf and the dictionary distributions.

    clf = svm.SVC(kernel='linear')
    distributions = {'C': uniform(1, 10)}

    rand_search = RandomizedSearchCV(clf, distributions)

#### Fill in the code that will print the estimator chosen by the random search algorithm.

    clf = RandomSearchCV(model, distributions)
    clf.fit(X_train, y_train)

    print(clf.best_estimator_)
