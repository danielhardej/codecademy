# Codecademy Intermediate Machine Learning
## Regularization Quiz

#### Consider the following three-parameter linear regression model: The Ridge regularization term for this model would be:

- [x] b_1^2 + b_2^2 + b_3^2

#### Fill in the following paragraph about loss functions.

Regularization for linear regression is implemented by modifying the loss function by adding a term to it. This term is the product of a hyperparameter that controls the strength of the regularization and the regularization term. The regularization term is the sum of the squared values of the coefficients in the case of L2 regularization and the absolute values of the coefficients in the case of L1 regularization. Minimizing this loss function means that the value of the old loss goes up and that's the reason this additive term is also referred to as a penalty term.

#### The following piece of code has three functions to implement ridge regularization with a two-parameter linear regression model. Fill in the code:

    # Imagine the data is already centered and the intercept b0 is thus zero.
    # The linear regression equation here is given by: y = b1*x1 + b2*x2 + error
    import numpy as np

    def loss_function(b1,b2,y,x1,x2):
      error  = y - b1*x1 - b2*x2
      loss = np.mean(error**2)
      return loss

    def regularization_term(b1,b2):
      ridge_regularization_term = b1**2 + b2**2
      return ridge_regularization_term

    def ridge_loss_function(b1,b2,y,x1,x2, alpha):
      modified_loss = loss_function(b1,b2,y,x1,x2) + alpha*regularization_term(b1,b2)
      return modified_loss


#### Which of the following statements about regularization is FALSE?

- [x] It is executed before implementing a machine learning model.
- [ ] L1 regularization is also known as LASSO regularization.
- [ ] L2 regularization imposes a constraint on the size of the coefficients.
- [ ] It corrects for overfitting.

#### Which one of the following statements is TRUE?

- [x] L1 regularization can also function as a feature selection method.
- [ ] L2 regularization preferentially sets some of the coefficients to zero.
- [ ] L2 regularization can also function as a feature elimination method.
- [ ] Both L1 and L2 regularization methods transform the features to become linear combinations of the original features.

#### Which of the following statements is FALSE?

- [ ] Increasing the bias in a machine learning model lowers the variance.
- [ ] A model that performs well on training data but poorly on test data is said to have high variance.
- [ ] The regularization hyperparameter needs to be tuned to find the sweet spot in the bias-variance tradeoff.
- [x] Hyperparameters are learned from the data during the model training step.

#### Complete the following piece of code that implements L1 regularization on a dataset (X,y) and calculates the mean-squared error of the fit on test data:

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import Lasso
    from sklearn.metrics import mean_squared_error

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    model = Lasso(alpha = 0.1)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)

#### Increasing the value of hyperparameter alpha in regularization is the same as:

- [ ] decreasing the strength of regularization
- [ ] decreasing bias
- [ ] increasing the size of the regularization constraint surface
- [x] increasing the training error
