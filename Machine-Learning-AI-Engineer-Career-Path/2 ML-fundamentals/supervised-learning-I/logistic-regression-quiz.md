#### Logistic Regression differs from Linear Regression because the output of a Logistic Regression model ranges from -∞ to +∞.

- [ ] True
- [x] False

#### You run a logistic regression model, and compare the predicted classifications with your test dataset and find the following results:

    True Positives: 25 True Negatives: 36 False Positives: 5 False Negatives: 4

    What would the resulting confusion_matrix look like?

- [ ] array([[25, 5], [4, 36]])
- [x] array([[36, 5], [4, 25]])
- [ ] array([[36, 5], [25, 4]])
- [ ] array([[36, 4], [5, 25]])

#### You have been studying public transportation in your area for the last few months, and have noticed that buses have been late 35% of the time at your stop. Calculate the odds and log-odds that a bus will be late.

- [x] Odds: 0.54; Log-Odds: -0.62
- [ ] Odds: 1.86; Log-Odds: -0.62
- [ ] Odds: 0.54; Log-Odds: 0.62
- [ ] Odds: 1.86; Log-Odds: 0.62

#### A Logistic Regression model that predicts if a credit card transaction is fraudulent is trained on a dataset with four features:

    charge_amount: the dollar amount for the charge
    international: 1 if the charge is made internationally and 0 if the charge is domestic
    recent_purchase: 1 if there was a charge on the account in the last 10 minutes, 0 otherwise
    previous_purchase: 1 if a charge at the same vendor was made previously, 0 otherwise

    The model’s coefficients for each feature are given below:

    charge_amount: 0.23 international: 0.14 recent_purchase: 0.36 previous_purchase: -0.60

##### Which feature has the greatest impact on a charge’s classification, and which feature has the least impact?

- [ ] Greatest impact: charge_amount Least impact: previous_purchase
- [ ] Greatest impact: previous_purchase Least impact: recent_purchase
- [ ] Greatest impact: recent_purchase Least impact: international
- [x] Greatest impact: previous_purchase Least impact: international

#### Which of the following circumstances would be the best candidate for decreasing the standard classification threshold of a Logistic Regression model from 0.5? A model that:

- [ ] detects credit card fraud, where “fraudulent” is the positive class.
- [x] predicts cancer diagnoses, where “has cancer” is the positive class.
- [ ] predicts customer conversion on a checkout page, where “converted” is the positive class.
- [ ] predicts flight delays, where “delayed” is the positive class.

#### Which of the following plots shows a Sigmoid function?

    https://content.codecademy.com/programs/data-science-path/logistic-regression/graphs.png

- [ ] D
- [x] C
- [ ] A
- [ ] B

#### You have a Logistic Regression model predicting if a customer will make a purchase or not. After running the .predict() method, you see the following output:

    [1 0 0 1 1]

##### Which of the following matrices could be the result of running .predict_proba() on the same dataset and model? Assume the standard classification threshold of 0.5.


- [x] [[0.2068119 0.7931881 ] [0.67934073 0.32065927] [0.94452517 0.05547483] [0.42252072 0.57747928] [0.12929566 0.87070434]]
- [ ] [[0.12929566 0.87070434] [0.67934073 0.32065927] [0.2068119 0.7931881 ] [0.94452517 0.05547483] [0.42252072 0.57747928]]
- [ ] [[0.67934073 0.32065927] [0.2068119 0.7931881 ] [0.94452517 0.05547483] [0.42252072 0.57747928] [0.12929566 0.87070434]]
- [ ] [[0.2068119 0.7931881 ] [0.67934073 0.32065927] [0.42252072 0.57747928] [0.94452517 0.05547483] [0.12929566 0.87070434]]

#### Using the same data from the previous model, you have the following elements to your confusion matrix:

    True Positives: 25 True Negatives: 36 False Positives: 5 False Negatives: 4

    What are the accuracy, precision, and recall metrics for this model?

- [ ] Accuracy = 0.83 Precision = 0.87 Recall = 0.86
- [ ] Accuracy = 0.87 Precision = 0.86 Recall = 0.83
- [ ] Accuracy = 0.83 Precision = 0.86 Recall = 0.87
- [x] Accuracy = 0.87 Precision = 0.83 Recall = 0.86

#### Which of the following describes the output of Logistic Regression?

- [ ] A Boolean value of either True or False for whether the outcome will happen.
- [ ] A value between 0 and 1, which indicates the probability of a particular outcome.
- [x] Either 0, indicating the event likely won’t happen, or 1, indicating that an outcome will likely occur.

#### Which function can we apply to a linear regression equation to solve classification problems?

- [ ] Probit
- [x] Logit Link
- [ ] Quadratic
- [ ] Exponential
