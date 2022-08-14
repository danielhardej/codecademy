# Intermediate Machine Learning
## Support Vector Machines Quiz

#### What are the support vectors in an SVM?

- [ ] All of the points in the training set on one side of the decision boundary.
- [ ] All of the points in the training set.
- [ ] Points in the training set that fall directly on the decision boundary.
- [x] The points in the training set closest to the decision boundary.

#### Which of the following SVMs has an optimal decision boundary?

    https://content.codecademy.com/programs/machine-learning/svm/quiz_image.png

- [x] A
- [ ] D
- [ ] C
- [ ] B

#### If your data is in three dimensions, the decision boundary will be a:

- [x] Plane.
- [ ] Hyperplane.
- [ ] Point.
- [ ] Line.

#### Which of the following SVMs with an rbf kernel has the largest gamma parameter?

    https://content.codecademy.com/programs/machine-learning/svm/svm_quiz.png

- [ ] B
- [ ] A
- [x] C
- [ ] D

#### What is the role of a kernel in an SVM?

- [x] A kernel transforms the data into a higher dimension so it can be linearly separable.
- [ ] A kernel helps find the support vectors quicker.
- [ ] A kernel chooses which data points should be in the training set and which should be in the validation set.
- [ ] A kernel sets the margin of an SVM to be either a hard margin or a soft margin.

#### An SVM has a soft margin when:

- [ ] The support vectors are the points farthest away from the decision boundary.
- [ ] The margin is small and the decision boundary allows few errors
- [ ] The support vectors are the closest points from one class — not both.
- [x] The margin is large and the decision boundary allows for many errors.

#### What are the inputs of the .fit() method in scikit-learn’s SVC class?

- [ ] A list of training points.
- [ ] A list of training points and the parameter C.
- [x] A list of training points and a list of labels associated with those points.
- [ ] The parameter C and the kernel the SVC will be using.

#### Why is it important for an SVM to maximize the size of its margin?

- [ ] A small margin would result in underfitting.
- [ ] A large margin makes more of the training points relevant.
- [x] A large margin prevents points in the training set from being close to the decision boundary.
- [ ] The size of the margin doesn’t matter as long as the data is linearly separable.

#### What happens to a Support Vector Machine if C is too large?

- [ ] Underfitting will occur due to the margin becoming too small.
- [x] Overfitting will occur due to the margin becoming too small.
- [ ] Overfitting will occur due to the margin becoming too large.
- [ ] Underfitting will occur due to the margin becoming too large.
