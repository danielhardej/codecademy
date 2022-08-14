# In this project, you will use scikit-learn’s Naive Bayes implementation on several
# different datasets. By reporting the accuracy of the classifier, we can find
# which datasets are harder to distinguish.

from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

#### Make the test and training sets
train_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','sci.med', 'rec.autos', 'talk.religion.misc'], subset='train', shuffle = True, random_state = 108)

test_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','sci.med', 'rec.autos', 'talk.religion.misc'], subset='test', shuffle = True, random_state = 108)

### Count Words
counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

### Make a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(train_counts, train_emails.target)

print(classifier.score(test_counts, test_emails.target))
