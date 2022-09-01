import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()
# print(digits.DESCR)
# print(digits)
# print(digits.data)
# print(digits.target)

# plt.gray()
# plt.matshow(digits.images[100])
# plt.show()
# print(digits.target[100])

model = KMeans(n_clusters=10, random_state=42)
model.fit(digits.data)

fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')

for i in range(10):
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)
  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()

new_samples = np.array([
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,4.58,1.91,0.00,0.00,0.00,0.00,0.00,0.00,7.62,3.81,0.00,0.00,0.00,0.00,0.00,0.00,7.62,3.81,0.00,0.00,0.00,0.00,0.00,0.00,7.62,3.81,0.00,0.00,0.00,0.00,0.00,0.00,7.62,3.81,0.00,0.00,0.00,0.00,0.00,0.00,7.62,3.81,0.00,0.00,0.00,0.00,0.00,0.00,6.86,3.05,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.92,1.52,0.53,0.00,0.00,0.53,3.96,6.94,7.62,7.62,5.95,0.00,0.00,5.72,7.63,5.42,3.11,6.08,6.63,0.00,0.00,6.10,4.04,0.00,0.76,7.47,4.35,0.00,0.00,0.05,0.00,0.00,5.34,7.40,1.07,0.00,0.00,0.00,0.00,3.13,7.62,3.51,0.00,0.00,0.00,0.00,0.76,7.32,7.63,6.94,5.42,0.00,0.00,0.00,0.38,4.35,4.35,3.81,2.67,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.15,4.12,4.57,4.57,4.57,1.75,0.00,0.00,0.53,7.40,6.75,6.63,7.25,6.56,0.00,0.00,0.00,0.59,0.00,0.31,6.10,6.56,0.00,0.00,0.00,0.00,2.29,6.86,7.62,6.10,0.00,0.00,0.00,0.00,1.52,4.57,5.87,7.62,0.61,0.00,1.14,5.95,4.65,5.19,7.32,7.17,0.46,0.00],
[0.00,0.00,0.00,0.00,0.23,2.82,0.15,0.00,0.00,0.76,2.59,0.00,1.98,7.62,2.21,0.00,0.00,3.50,7.62,0.76,1.52,7.62,2.29,0.00,0.00,3.05,7.62,2.82,3.36,7.62,2.75,0.00,0.00,3.05,7.62,7.62,7.62,7.62,5.57,0.00,0.00,0.00,1.14,1.29,5.48,6.78,0.36,0.00,0.00,0.00,0.00,0.00,6.10,5.72,0.00,0.00,0.00,0.00,0.00,0.00,4.73,4.04,0.00,0.00]
])

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
