#### Underfitting happens when:

- [x] k is too big so larger trends in the dataset aren’t represented.
- [ ] k is too small so outliers dominate the result.
- [ ] k is too small so larger trends in the dataset aren’t represented.
- [ ] k is too big so outliers dominate the result.

#### True/False: K-Nearest Neighbors can work with data with 1000 features.

- [x] True
- [ ] False

#### Overfitting happens when:

- [ ] k is too big so outliers dominate the result.
- [ ] k is too small so larger trends in the dataset aren’t represented.
- [x] k is too small so outliers dominate the result.
- [ ] k is too big so larger trends in the dataset aren’t represented.

#### What is a potential problem if k is even?

- [ ] The distance formula will have to be adjusted.
- [x] There could be an equal number of nearest neighbors from both classes.
- [ ] You can’t find an even number of neighbors.
- [ ] You can’t compute validation accuracy.

#### Why is normalizing your data essential for K-Nearest Neighbors?

- [ ] It is not essential.
- [ ] So that unusual features are removed.
- [x] So a feature with a vastly different scale does not dominate other features.
- [ ] So the distance between points is positive.

#### What is the nearest neighbor to the point (1,2)?

- [ ] (1,0)
- [x] (1, 3)
- [ ] (3, 1)
- [ ] (0, 1)

#### What would you expect to happen to the validation accuracy of a K-Nearest Neighbors classifier as k increases from 1 to infinity?

- [ ] Validation accuracy goes up.
- [ ] Validation accuracy goes down.
- [ ] Validation accuracy goes down and then up.
- [x] Validation accuracy goes up and then down.

#### In the following image, K-Nearest Neighbors would classify the question mark point as a triangle for which k?

    https://content.codecademy.com/courses/learn-knn/quiz.svg

- [ ] k = 1 and k = 3.
- [ ] k = 3 and k = 5.
- [ ] k = 5 and k = 7.
- [x] k = 1 and k = 5.

#### How does K-Nearest Neighbors define what it means for two points to be close to each other?

- [ ] By counting the number of features the two points share.
- [ ] By using the distance formula using three features of the data.
- [x] By using the distance formula using all features of the data.
- [ ] By comparing the most important feature of each point.

#### The .predict() function in scikit-learn’s KNeighborClassifier class takes _____ as a parameter and returns _____.

- [ ] A single point to classify / a single prediction.
- [ ] A single training point / a single prediction.
- [ ] A list of training points / a list of predictions.
- [x] A list of points to classify / a list of predictions.
