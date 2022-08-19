#### What does it mean for a model to have an R² value of 0?

- [ ] R² cannot be 0.
- [x] A value of 0 would indicate that the model fails to accurately model the data at all.
- [ ] A value of 0 would indicate that the model is a perfect fit.

#### In the multiple linear regression equation, what are the m variables?

- [ ] The dependent variables.
- [ ] The intercept.
- [ ] The independent variables.
- [x] The coefficients.

#### Which of the following statements is true about Residual Analysis?

- [ ] A residual is the difference between the training set and the test set.
- [x] Residual Analysis allows you to assess the accuracy of a multiple linear regression model.
- [ ] Residual Analysis allows you to assess the accuracy of a classification model.

#### Given a regression line and four data points, which point has the largest residual?

- [x] Point C
- [ ] Point A
- [ ] Point B
- [ ] Point D

#### Which of the two coefficients will have a greater impact on the dependent variable — a coefficient of -1.5 or a coefficient of 1.5?

- [ ] Coefficient of -1.5.
- [x] They will have the same level of impact.
- [ ] Coefficient of 1.5.

#### Fill in the Blank: What is the module we are importing from?

    from _________ import LinearRegression

- [x] sklearn.linear_model
- [ ] sklearn.regression_model
- [ ] sklearn

#### True/False: The test set is the data that you partition away at the very start of your experiment (to provide an unbiased evaluation of the model).

- [ ] False
- [x] True

#### Find the Error: Which line would break the following code?

    from sklearn.linear_model import LinearRegression

    x_train = [[5], [10], [15], [20]]
    y_train = [30, 40, 50, 60]

    x_test = [[2], [6]]
    y_test = [20, 25]

    regr = LinearRegression()

    y_predict = regr.predict(x_test)

    regr.fit(x_train, y_train)

- [x] y_predict = regr.predict(x_test)
- [ ] from sklearn.linear_model import LinearRegression
- [ ] regr = LinearRegression()
