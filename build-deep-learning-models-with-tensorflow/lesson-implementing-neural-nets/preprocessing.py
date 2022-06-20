import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer

#load the dataset
dataset = pd.read_csv('insurance.csv')
#choose first 7 columns as features
features = dataset.iloc[:,0:6]
#choose the final column for prediction
labels = dataset.iloc[:,-1]

#one-hot encoding for categorical variables
features = pd.get_dummies(features)
#split the data into training and test data
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42)

#normalize the numeric columns using ColumnTransformer
ct = ColumnTransformer([('normalize', Normalizer(), ['age', 'bmi', 'children'])], remainder='passthrough')
#fit the normalizer to the training data and convert from numpy arrays to pandas frame
features_train_norm = ct.fit_transform(features_train)
#applied the trained normalizer on the test data and convert from numpy arrays to pandas frame
features_test_norm = ct.transform(features_test)

#ColumnTransformer returns numpy arrays. Convert the features to dataframes
features_train_norm = pd.DataFrame(features_train_norm, columns = features_train.columns)
features_test_norm = pd.DataFrame(features_test_norm, columns = features_test.columns)

# Create a new ColumnTransformer instance called my_ct that uses StandardScaler() and 'scale'
# (instead of Normalizer() and 'normalize') with the same numerical features (age, bmi, children)
my_ct = ColumnTransformer([('scale', StandardScaler(), ['age', 'bmi', 'children'])], remainder='passthrough')

# Use the .fit_transform() method of my_ct to fit the column transformer to the features_train DataFrame and at the same time transform it
features_train_scale = my_ct.fit_transform(features_train)
# Use the .transform() method to transform the trained column transformer my_ct to the features_test DataFrame.
features_test_scale = my_ct.transform(features_test)

# Transform the features_train_scale NumPy array back to a DataFrame using pd.DataFrame()
features_train_scale = pd.DataFrame(features_train_scale, columns=features_train.columns)
# Transform the features_test_scale NumPy array back to DataFrame using pd.DataFrame()
features_test_scale = pd.DataFrame(features_test_scale, columns=features_test.columns)

# Print the statistics summary of the resulting train and test DataFrames
print(features_train_scale.describe())
print(features_test_scale.describe())
