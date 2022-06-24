# There are some different strategies for automated hyperparameter tuning.
# Grid search, or exhaustive search, tries every combination of desired hyperparameter values.
# Random Search goes through random combinations of hyperparameters and doesn’t try them all.

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint as sp_randint
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer
from model import design_model, features_train, labels_train

#------------- GRID SEARCH --------------
def do_grid_search():
    # we need to setup the desired hyperparameters grid
    batch_size = [6, 64]
    epochs = [10, 50]
    # we need to first wrap our neural network model into a KerasRegressor
    model = KerasRegressor(build_fn=design_model)
    param_grid = dict(batch_size=batch_size, epochs=epochs)
    # we initialize a GridSearchCV object and fit our model to the data:
    grid = GridSearchCV(estimator = model, param_grid=param_grid, scoring = make_scorer(mean_squared_error, greater_is_better=False),return_train_score = True)
    grid_result = grid.fit(features_train, labels_train, verbose = 0)
    print(grid_result)
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
      print("%f (%f) with: %r" % (mean, stdev, param))

    print("Traininig")
    means = grid_result.cv_results_['mean_train_score']
    stds = grid_result.cv_results_['std_train_score']
    for mean, stdev, param in zip(means, stds, params):
      print("%f (%f) with: %r" % (mean, stdev, param))

#------------- RANDOMIZED SEARCH --------------
def do_randomized_search():
    # change our hyperparameter grid specification for the randomized search in order to have more options
    param_grid = {'batch_size': sp_randint(2, 16), 'nb_epoch': sp_randint(10, 100)}
    model = KerasRegressor(build_fn=design_model)
    # Randomized search will sample values for batch_size and nb_epoch from uniform distributions in the interval [2, 16] and [10, 100], respectively, for a fixed number of iterations
    grid = RandomizedSearchCV(estimator = model, param_distributions=param_grid, scoring = make_scorer(mean_squared_error, greater_is_better=False), n_iter = 12)
    grid_result = grid.fit(features_train, labels_train, verbose = 0)
    print(grid_result)
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
      print("%f (%f) with: %r" % (mean, stdev, param))

print("-------------- GRID SEARCH --------------------")
do_grid_search()
print("-------------- RANDOMIZED SEARCH --------------------")
do_randomized_search()
