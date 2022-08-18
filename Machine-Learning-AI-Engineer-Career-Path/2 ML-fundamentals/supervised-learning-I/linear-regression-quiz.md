#### What is the sum of squared error between the points described by x_values and y_values and the line described by m and b?

    y_values_of_points = [1, -4, -7, -6]
    y_values_of_line = [1, -3, -6, -8]

- [ ] 0
- [ ] 3
- [x] 6
- [ ] 16

#### If the algorithm is taking too long to converge, should you move the learning rate up or down?

- [ ] Don’t change it!
- [ ] Down.
- [x] Up.

#### When does the linear regression algorithm stop?

- [ ] It never stops.
- [x] When the parameters stop changing (or change very slowly).
- [ ] When the line goes through all of the points.
- [ ] After 100 iterations.

#### Let’s say we have 3 lines that produce the following average loss on our dataset. Which one is the line of best fit?

    Line A: 17
    Line B: 11.5
    Line C: 13

- [x] B
- [ ] C
- [ ] Impossible to tell!
- [ ] A

#### If the model worked correctly, what should y_new represent in the code below?

    regr = LinearRegression()

    regr.fit(X, y)

    y_new = regr.predict(X)

- [ ] The predicted y-values from a new set of x-values.
- [ ] The same as y.
- [x] The y-values that X would produce on the line of best fit.
- [ ] The slope and intercept values of the line of best fit.

#### What is the purpose of performing gradient descent?

- [ ] To decrease the slope of the loss curve
- [ ] To maximize loss.
- [x] To move parameters in the direction that minimizes loss.
- [ ] To decrease parameter values.

#### The goal of a linear regression algorithm is to find the _____ and _____ that minimize average loss.

- [x] slope; intercept
- [ ] input; output
- [ ] line; points
- [ ] learning rate; convergence
