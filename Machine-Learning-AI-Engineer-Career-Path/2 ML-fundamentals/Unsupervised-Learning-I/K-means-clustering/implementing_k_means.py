# Implementing K-Means
# The K-Means algorithm:
#
# Place k random centroids for the initial clusters.
# Assign data samples to the nearest centroid.
# Update centroids based on the above-assigned data samples.
# Repeat Steps 2 and 3 until convergence.

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()

samples = iris.data

x = samples[:,0]
y = samples[:,1]

sepal_length_width = np.array(list(zip(x, y)))

# Step 1: Place K random centroids
# Number of clusters
k = 3
# Create x coordinates of k random centroids
centroids_x = np.random.uniform(min(x), max(x), size=k)
# Create y coordinates of k random centroids
centroids_y = np.random.uniform(min(y), max(y), size=k)
# Create centroids array
centroids = np.array(list(zip(centroids_x, centroids_y)))
print(centroids)
# Make a scatter plot of x, y
plt.scatter(x, y, alpha=0.5)
# Make a scatter plot of the centroids
plt.scatter(centroids_x, centroids_y, alpha=0.5)
# Display plot
plt.show()

# Step 2: Assign samples to nearest centroid
# Distance formula
def distance(a, b):
  d1 = (a[0] - b[0])**2
  d2 = (a[1] - b[1])**2
  distance = (d1 + d2)**0.5
  return distance

# Cluster labels for each point (either 0, 1, or 2)
labels = np.zeros(len(samples))

# A function that assigns the nearest centroid to a sample
def assign_to_centroid(sample, centroids):
  k = len(centroids)
  distances = np.zeros(k)
  for i in range(k):
    distances[i] = distance(sample, centroids[i])
  closest_centroid = np.argmin(distances)
  return closest_centroid

# Assign the nearest centroid to each sample
for i in range(len(samples)):
  labels[i] = assign_to_centroid(samples[i], centroids)

# Print labels
print(labels)

# Distances to each centroid
distances = np.zeros(k)

for i in range(len(samples)):
  distances[0] = distance(sepal_length_width[i], centroids[0])
  distances[1] = distance(sepal_length_width[i], centroids[1])
  distances[2] = distance(sepal_length_width[i], centroids[2])
  cluster = np.argmin(distances)
  labels[i] = cluster

# Step 3: Update centroids
centroids_old = deepcopy(centroids)

for i in range(k):
  points = []
  for j in range(len(sepal_length_width)):
    if labels[j] == i:
      points.append(sepal_length_width[j])
  centroids[i] = np.mean(points, axis=0)

print(centroids_old)
print(centroids)
