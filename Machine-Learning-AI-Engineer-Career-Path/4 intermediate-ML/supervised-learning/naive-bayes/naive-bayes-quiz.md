#### Given the following word counts for positive and negative reviews, what is P(“great”)?

    pos = {
      "great" : 2,
      "crib": 1,
      "this": 3,
      "is": 2
    }

    neg = {
      "great" : 1,
      "horrible": 7,
      "this": 2,
      "is": 2
    }

- [ ] 0.1.
- [ ] 0.05.
- [x] 0.15.
- [ ] 0.2.

#### Given the following word counts for positive and negative reviews, what is P(“great”|positive)?

    pos = {
      "great" : 2,
      "crib": 1,
      "this": 3,
      "is": 2
    }

    neg = {
      "great" : 1,
      "horrible": 7,
      "this": 2,
      "is": 2
    }

- [ ] 0.1.
- [ ] 0.15.
- [ ] 0.2.
- [x] 0.25.


#### Why is a Naive Bayes Classifier a supervised machine learning algorithm?

- [x] You need labeled data in order to calculate the probabilities used in Bayes Theorem.
- [ ] The algorithm learns from a reward function.
- [ ] The algorithm uses smoothing to prevent probabilities from becoming 0.
- [ ] The algorithm learns from unlabeled data in order to make classifications.


#### The .predict() method in the MultinomialNB class takes _____ as a parameter and returns _____

- [x] A list of data points, a list of classifications.
- [ ] A list of data points, a single classification.
- [ ] A single data point, a list of classifications.
- [ ] A single data point, a single classification.


#### What is the purpose of smoothing in a Naive Bayes Classifier?

- [ ] To make the probability of each feature close to 1.
- [ ] To make the probability of each feature more similar to each other.
- [ ] To remove outliers from your dataset.
- [x] To prevent a feature with a probability of 0 from ruining the total probability.


#### If the target_names of a Naive Bayes classifier are [B, A, D, C], and the predict_proba function returns the list [.3, .1, .5, .1] for a given datapoint, what is the predicted class for that datapoint?

- [ ] A
- [ ] C
- [ ] B
- [x] D

#### Which of the following is not a Natural Language Processing technique that can improve performance of a Naive Bayes Classifier?

- [x] Smoothing.
- [ ] Making all capital letters lowercase.
- [ ] Removing punctuation from your text.
- [ ] Using bigrams or trigrams.

#### Why can we ignore the denominator of Bayes Theorem when calculating the probabilities of each class?

- [x] The denominator is the same for every class.
- [ ] The denominator can’t be ignored!
- [ ] Bayes Theorem doesn’t have a denominator.
- [ ] The denominator will add error to the final probability of every class.
