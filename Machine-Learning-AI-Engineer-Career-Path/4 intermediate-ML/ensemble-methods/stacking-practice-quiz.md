# Codecademy Intermediate Machine Learning
## Ensemble Methods: Stacking

#### How is stacking different from other ensemble methods like bagging or boosting?

- [ ] Bagging and boosting models can only be used with decision trees, while Stacking can be used with other classifiers like logistic regression.
- [ ] Stacking models cannot reduce variance in predictions but only bias. Boosting and bagging models can reduce both bias and variance.
- [ ] Bagging and boosting models can only be used for regression problems and not for classification problems. Stacking models can be used for either.
- [x] A Stacking model can combine the predictive strengths of different types of estimators whereas bagging and boosting models typically use one estimator.

##### Note: Bagging and boosting are homogenous techniques in that they reuse the same learning algorithms in the ensemble. Stacking creates an ensemble of an arbitrary number of learning algorithms and estimators.

#### For Stacking, our first step was to augment the training set by training the base estimators individually to make predictions on the training data. Making predictions on data used in the training set is a common recipe for overfitting. How did we avoid this?

- [ ] By modifying our base estimators to use bagging techniques.
- [ ] By carefully selecting base estimators that are resilient to overfitting.
- [x] By using a k-fold cross-validation.
- [ ] By implementing our model using the scikit-learn Python package.

##### Note: This is the correct answer. The K-fold cross validation allows up to train our estimators without being biased on data seen previously. Nice work!

#### In what way(s) can we fine-tune a Stacking model?

- [ ] Varying the parameters of our final estimator (the model that combines the results of the base estimators).
- [ ] Selecting a variety of level-0 estimator combinations (e.g. logistic regression. Decision trees, K-nearest neighbors).
- [ ] Experimenting with data pre-processing (e.g. using different values of k in k-fold cross-validation).
- [ ] Using different parameters in base estimators.
- [x] All techniques mentioned can be used in fine-tuning a Stacking model.

##### Note: A stacking model setup provides a lot of open-endedness in the pursuit of finding the best performance. We have the freedom to make adjustments on any model in our setup as well as the data being used.
