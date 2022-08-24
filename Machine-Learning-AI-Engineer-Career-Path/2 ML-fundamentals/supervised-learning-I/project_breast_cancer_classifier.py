import codecademylib3_seaborn
import operator
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

dataset = load_breast_cancer()
# print(dataset.keys())
# print(dataset.DESCR)
# print(dataset.data[0])
# print(dataset.feature_names)
# print(dataset.target_names)
# print(dataset.target) # 0 corresponds to malignant

X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target,  test_size=0.2, random_state = 100)

# print(len(X_train), len(y_train))
# print(len(X_test), len(y_test))

k_vals = {}
for k in range(1, 101):
  kn_clf = KNeighborsClassifier(n_neighbors = k)
  kn_clf.fit(X_train, y_train)
  acc_score = kn_clf.score(X_test, y_test)
  print("K = ", k, "  Accuracy score: ", acc_score)
  k_vals[k] = acc_score

# print(k_vals.values())
max_acc = max(k_vals.items(), key=operator.itemgetter(1))[1]
best_k = max(k_vals.items(), key=operator.itemgetter(1))[0]
print("Best K =", best_k, "  Best accuracy:", max_acc)

k_list = list(k_vals.keys())
accuracies = list(k_vals.values())
plt.plot(k_list, accuracies)
plt.xlabel("K")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.show()
