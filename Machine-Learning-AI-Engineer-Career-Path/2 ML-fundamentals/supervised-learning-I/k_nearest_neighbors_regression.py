from movies import movie_dataset, movie_ratings

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def predict(unknown, dataset, movie_ratings, k):
  distances = []
  numerator = 0
  denominator = 0
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  for neighbor in neighbors:
    rating = movie_ratings[neighbor[1]]
    distance_to_neighbor = neighbor[0]
    numerator += rating/distance_to_neighbor
    denominator += 1/distance_to_neighbor
  return numerator/denominator

print(predict([0.016, 0.300, 1.022], movie_dataset, movie_ratings, k=5))



### Sklearn implementation:

from sklearn.neighbors import KNeighborsRegressor

regressor = KNeighborsRegressor(n_neighbors = 5, weights = "distance")
regressor.fit(movie_dataset, movie_ratings)

test_points = [[0.016, 0.300, 1.022],
              [0.0004092981, 0.283, 1.0112],
              [0.00687649, 0.235, 1.0112]]

print(regressor.predict(test_points))
