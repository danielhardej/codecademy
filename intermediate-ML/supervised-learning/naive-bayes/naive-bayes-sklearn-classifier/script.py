from reviews import counter, training_counts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from reviews import neg_list, pos_list
from sklearn.feature_extraction.text import CountVectorizer

review = "This crib was great amazing and wonderful"

counter =  CountVectorizer()
counter.fit(neg_list + pos_list)
print(counter.vocabulary_)

review_counts = counter.transform([review])
print(review_counts.toarray())
training_counts = counter.transform(neg_list + pos_list)

classifier = MultinomialNB()

training_labels = [0] * 1000 + [1] * 1000

classifier.fit(training_counts, training_labels)
prediction = classifier.predict(review_counts)
print(prediction)
print(classifier.predict_proba(review_counts)[0])

if prediction == [1]:
  print("The review is positive")
else:
  print("The review is negative")
