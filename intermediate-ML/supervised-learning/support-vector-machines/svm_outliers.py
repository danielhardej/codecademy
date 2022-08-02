# SVMs try to maximize the size of the margin while still correctly separating the
# points of each class. As a result, outliers can be a problem.
#
# The size of the margin decreases when a single outlier is present, and as a
# result, the decision boundary changes as well. However, if we allowed the
# decision boundary to have some error, we could still use the original line.
#
# SVMs have a parameter C that determines how much error the SVM will allow for.
# If C is large, then the SVM has a hard margin — it won’t allow for many
# misclassifications, and as a result, the margin could be fairly small. If C is
# too large, the model runs the risk of overfitting. It relies too heavily on the
# training data, including the outliers.
#
# On the other hand, if C is small, the SVM has a soft margin. Some points might
# fall on the wrong side of the line, but the margin will be large. This is
# resistant to outliers, but if C gets too small, you run the risk of underfitting.
# The SVM will allow for so much error that the training data won’t be represented.
#
# The optimal value of C will depend on your data. Don’t always maximize margin
# size at the expense of error. Don’t always minimize error at the expense of
# margin size. The best strategy is to validate your model by testing many
# different values for C.

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from graph import points, labels, draw_points, draw_margin

classifier = SVC(kernel='linear', C = 0.02)
points.append([3,3])
labels.append(0)
points.append([1,8])
labels.append(1)
points.append([10,4])
labels.append(0)
classifier.fit(points, labels)

draw_points(points, labels)
draw_margin(classifier)

plt.show()
