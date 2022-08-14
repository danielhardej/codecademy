import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

fig, ax = plt.subplots()


def prepare_data(player_name):
  player_name['type'] = player_name['type'].map({'S':1, 'B':0})
  player_name = player_name.dropna(subset = ['plate_x', 'plate_z', 'type'])
  training_set, validation_set = train_test_split(player_name, random_state = 1)

  plt.scatter(x = player_name['plate_x'], y = player_name['plate_z'], c = player_name['type'], cmap = plt.cm.coolwarm, alpha = 0.5)

  return training_set, validation_set

training_set, validation_set = prepare_data(jose_altuve)

current_best_score = 0
best_gamma = 0
best_c = 0

for g in range(1, 10):
  print("testing gamma value: {}".format(g))
  for c in range(1, 20):
    print("  testing C value: {}".format(c))
    classifier = SVC(kernel = 'rbf', gamma = g, C = c)
    classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])
    acc_score = classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type'])
    if acc_score > current_best_score:
      current_best_score = acc_score
      best_gamma = g
      best_c = c

print("Accuracy: {}%".format(current_best_score*100))
print("Gamma: {}".format(best_gamma))
print("C val: {}".format(best_c))

best_classifier = SVC(kernel = 'rbf', gamma = best_gamma, C = best_c)
best_classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])
acc_score = best_classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type'])
draw_boundary(ax, best_classifier)
plt.show()
