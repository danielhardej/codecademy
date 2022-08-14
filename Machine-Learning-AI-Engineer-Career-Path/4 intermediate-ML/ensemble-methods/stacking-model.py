import pandas as pd

df = pd.read_csv('water_potability')
print(df.columns, df.shape)

# We’ll take a train-test split of our data to handle the training process.

X = water_potability.drop(['Potability'], axis=1)
y = water_potability['Potability']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=rand_state)

# To assemble our ensemble, we’ll make a dictionary of base estimators. This will
# be contained within the level_0_estimators dict. Also, our final estimator will
# be a Random Forest as represented with level_1_estimator. Notice also how we
# prepare to add new features to our training dataset (as columns) in level_0_columns.

level_0_estimators = dict()
level_0_estimators["logreg"] = LogisticRegression(random_state=rand_state)
level_0_estimators["forest"] = RandomForestClassifier(random_state=rand_state)

level_0_columns = [f"{name}_prediction" for name in level_0_estimators.keys()]

level_1_estimator = RandomForestClassifier(random_state=rand_state)

# Handling our k-fold cross-validation is fairly straightforward using
# sklearn.model_selection.StratifiedKFold
# from the Scikit-learn library. The kfold is then given to the instantiated StackingClassifier.

kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=rand_state)
stacking_clf = StackingClassifier(estimators=list(level_0_estimators.items()),
                                    final_estimator=level_1_estimator,
                                    passthrough=True, cv=kfold, stack_method="predict_proba")

# Calling fit_transform on our classifier manages a lot of the heavy lifting.
# It will handle the training of our level_0 base estimators along with the
# level_1_estimator, make cross-validated predictions on the training set, and
# augment the training set with predictions from each estimator. Let’s see how
# the resulting training dataset looks:

df = pd.DataFrame(stacking_clf.fit_transform(X_train, y_train), columns=level_0_columns + list(X_train.columns))

y_val_pred = stacking_clf.predict(X_test)
stacking_accuracy = accuracy_score(y_test, y_val_pred)

vanilla_logistic_regression = LogisticRegression(random_state=rand_state).fit(X_train, y_train)
lr_accuracy = accuracy_score(y_test, vanilla_logistic_regression.predict(X_test))

vanilla_decision_tree = RandomForestClassifier(random_state=rand_state).fit(X_train, y_train)
dt_accuracy =  accuracy_score(y_test, vanilla_decision_tree.predict(X_test))

print(f'Stacking accuracy: {stacking_accuracy:.4f}')
print(f'Logistic Regression accuracy: {lr_accuracy:.4f}')
print(f'Decision Tree accuracy: {dt_accuracy:.4f}')
