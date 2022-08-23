from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(movie_dataset, labels)

print(classifier.predict([[.45, .2, .5], [.25, .8, .9],[.1, .1, .9]]))
