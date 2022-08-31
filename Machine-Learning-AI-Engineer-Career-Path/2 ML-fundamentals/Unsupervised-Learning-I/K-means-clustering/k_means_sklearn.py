# Implementaion of K-Means Clustering using Scikit-Learn.

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans


### Implementation
iris = datasets.load_iris()
samples = iris.data

# Use KMeans() to create a model that finds 3 clusters
model = KMeans(n_clusters = 3)

# Use .fit() to fit the model to samples
model.fit(samples)

# Use .predict() to determine the labels of samples
labels = model.predict(samples)

# Print the labels
print(labels)


### Classifying new data
# Store the new Iris measurements
new_samples = np.array([[5.7, 4.4, 1.5, 0.4],
   [6.5, 3. , 5.5, 0.4],
   [5.8, 2.7, 5.1, 1.9]])

print(new_samples)

# Predict labels for the new_samples
new_labels = model.predict(new_samples)
print(new_labels)

new_names = [iris.target_names[label] for label in new_labels]

print(new_names)


### Visualizing
# Make a scatter plot of x and y and using labels to define the colors
x = samples[:,0]
y = samples[:,1]

plt.scatter(x, y, c=labels, alpha=0.5)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

### Evaluating
labels = [iris.target_names[s] for s in model.predict(samples)]

# Code starts here:
species = [iris.target_names[t] for t in list(target)]

df = pd.DataFrame({'labels': labels, 'species': species})

print(df)

ct = pd.crosstab(df['labels'], df['species'])
print(ct)

### Finding the number of n_clusters

# At this point, we have grouped the Iris plants into 3 clusters. But suppose we
# didn’t know there are three species of Iris in the dataset, what is the best
# number of clusters? And how do we determine that?
# Before we answer that, we need to define what is a good cluster?
# Good clustering results in tight clusters, meaning that the samples in each
# cluster are bunched together. How spread out the clusters are is measured by
# inertia. Inertia is the distance from each sample to the centroid of its cluster.
# The lower the inertia is, the better our model has done.
#
# Ultimately, this will always be a trade-off. If the inertia is too large, then
# the clusters probably aren’t clumped close together. On the other hand, if there
# are too many clusters, the individual clusters might not be different enough from
# each other. The goal is to have low inertia and a small number of clusters.
#
# One of the ways to interpret this graph is to use the elbow method: choose an
# “elbow” in the inertia plot - when inertia begins to decrease more slowly.

num_clusters = list(range(1, 9))
inertias = []

for k in num_clusters:
  model = KMeans(n_clusters=k)
  model.fit(samples)
  inertia = model.inertia_
  inertias.append(inertia)


plt.plot(num_clusters, inertias, '-o')

plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')

plt.show()
