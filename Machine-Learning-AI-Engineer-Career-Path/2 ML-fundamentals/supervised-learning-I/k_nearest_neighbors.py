from movies import training_set, training_labels, validation_set, validation_labels

def normalize_point(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []
  for value in lst:
    normalized.append((value-minimum)/(maximum-minimum))
  return normalized

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0

def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
  num_correct = 0.0
  for movie in validation_set:
    guess = classify(validation_set[movie], training_set, training_labels, k)
    if guess == validation_labels[movie]:
      num_correct += 1
  return num_correct/len(validation_set)

my_movie = [35000, 132, 2017]
normalized_my_movie = normalize_point(my_movie)
print(normalized_my_movie)
print(classify(normalized_my_movie,movie_dataset,movie_labels,5))

print(validation_set["Bee Movie"])
guess = classify(validation_set["Bee Movie"],training_set,training_labels,5)
print(guess)
if guess == validation_labels["Bee Movie"]:
  print("Correct!")
else:
  print("Wrong!")

print(find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, 3))
