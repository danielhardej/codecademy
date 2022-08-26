#### In the image below, the circle with the solid line represents the true label of points. Points that fall in the circle have the label 1 and points outside the circle have the label 0. The circle with the dotted line represents the classification’s guess — if the point is inside the dotted circle, it has been classified as a 1, otherwise, it is classified as a 0. What is the equation for recall?

![](https://content.codecademy.com/programs/data-science-path/accuracy_venn.svg =200x200)

- [ ] $A/A+B$
- [x] $B/B+A$
- [ ] $A/A+D$
- [ ] $B/B+D$

#### In the image below, the circle with the solid line represents the true label of points. Points that fall in the circle have the label 1 and points outside the circle have the label 0. The circle with the dotted line represents the classification’s guess — if the point is inside the dotted circle, it has been classified as a 1, otherwise, it is classified as a 0. What is the equation for accuracy?

![](https://content.codecademy.com/programs/data-science-path/accuracy_venn.svg =200x200)

- [ ] $A+C/A+B+C+D$
- [x] $B+D/A+B+C+D$
- [ ]  $A+B/A+B+C+D$
- [ ]  $B+C/A+B+C+D$

​

#### Given the following values, what is the recall of the classifier?

    true_positives = 2
    true_negatives = 3
    false_positives = 1
    false_negatives = 4

- [ ] 0.666
- [ ] 0.1
- [x] 0.333
- [ ] 0.5

#### Precision is defined as:

- [ ] The harmonic mean of accuracy and recall.
- [ ] The number of correct classifications out of all classifications.
- [x] The number of relevant items out of all items selected.
- [ ] The number of relevant items selected out of all relevant items.

#### A false positive is when:

- [x] The true label is a 0 and the prediction is a 1.
- [ ] The true label is a 0 and the prediction is a 0.
- [ ] The true label is a 1 and the prediction is a 0.
- [ ] The true label is a 1 and the prediction is a 1.

#### Why is the F1 score calculated using the harmonic mean?

- [ ] The F1 score is calculated using the arithmetic mean.
- [x] The harmonic mean makes the F1 score low when either precision or recall is low.
- [ ] The harmonic mean will consider precision and recall equally.
- [ ] The harmonic mean takes less time to compute than the arithmetic mean.

#### What are the parameter(s) of scikit-learn’s f1_score function?

- [x] A list of true labels followed by a list of predictions.
- [ ] A prediction followed by a true label.
- [ ] A true label followed by a prediction.
- [ ] A list of predictions followed by a list of true labels.

#### If the true labels of your data are [1, 0, 1, 1] and the prediction from the classifier are [1, 1, 1, 0], then the prediction at index 3 is a:

- [x] False negative.
- [ ] True positive.
- [ ] False positive.
- [ ] True negative.
