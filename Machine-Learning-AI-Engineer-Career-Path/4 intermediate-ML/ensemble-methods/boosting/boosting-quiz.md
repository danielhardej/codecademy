#### How many leaf nodes are there in a decision stump?

- [x] 2
- [ ] 1
- [ ] 4
- [ ] 3

#### Which of the following statements about ensembling is FALSE?

- [ ] High diversity among base estimators leads to a stronger ensemble.
- [x] Base models should be correlated and that improves the ensembled model.
- [ ] Base models can be weak learners.
- [ ] Base models for boosting are chosen to be simple and have high bias.

*Base models need to be uncorrelated and independent for otherwise the ensembled model will perform worse than them.*

#### For the GradientBoostingClassifier(), the default value for the max_depth parameter is 3. What is the maximum number of leaf nodes a decision tree of that depth can have?

- [x] 8
- [ ] 4
- [ ] log(2)
- [ ] 3

*Since a decision tree is a binary tree, each node splits into 2. So the maximum number of leaf nodes for a tree of depth 3 would be 2^3 = 8.*

#### Fill in the missing text in the following paragraph about boosting:

**Boosting** is an ensemble learning technique where the weak learners are too **simple** and tend to suffer from high **bias**. Decision **stumps** are a common choice for this as can only make a decision based off of one feature at a time, causing them to **underfit** the data substantially.

#### Fill in text in the following paragraph about bagging:

Bagging methods use **weak learners**  as base models that are **complex** and tend to suffer from high **variance**. Their weakness as models is due to the fact that they are built with only a subset of the available features and on a subset of the training data due to **bootstrapping**.
