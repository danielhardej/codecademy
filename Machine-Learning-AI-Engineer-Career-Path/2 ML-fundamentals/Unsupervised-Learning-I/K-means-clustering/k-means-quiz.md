#### What is inertia in the context of clustering?

- [ ] Inertia is a property of matter by which it continues in its existing state of rest or uniform motion in a straight line unless that state is changed by an external force.
- [ ] Inertia is the distance from each sample to the centroid of its cluster. The higher the better.
- [ ] Inertia (noun) the tendency to do nothing or to remain unchanged.
- [x] Inertia is the distance from each sample to the centroid of its cluster. The lower the better.

#### Which of the following lines of code creates a K-means model where the k is 3?

- [ ] model = KMeans(n_clusters)
- [ ] None of them.
- [ ] model = KMeans.n_clusters(3)
- [x] model = KMeans(n_clusters=3)


#### How many clusters are likely in this dataset?

![](https://content.codecademy.com/programs/machine-learning/k-means/clustering-2-clusters.png)

- [ ] Just one!
- [ ] Probably three.
- [x] Probably two.
- [ ] Most likely four.

#### Find the error in the code below:

    import matplotlib.pyplot as plt
    from sklearn import datasets
    from sklearn.cluster import KMeans

    boston = datasets.load_boston()

    samples = boston.data

    model = KMeans(n_clusters=3)

    labels = model.predict(samples)

    model.fit(samples)

    print(labels)

- [ ] You need to import pandas.
- [ ] There are no errors.
- [x] You can’t use .predict() before fitting.
- [ ] It should be samples = boston instead.


#### Fill in the Blank: K-means algorithm stops when __________.

- [ ] the centroids are all gone
- [ ] the condition k == 0 is true
- [x] centroids stabilize (convergence)
- [ ] centroids become one

#### What is the purpose of the elbow method?

- [ ] To find convergence.
- [ ] To find the locations of the new centroids.
- [x] To find the best number of clusters.
- [ ] To slowly take over the airplane armrest.

#### For Step 1 of K-means, how do we place the k centroids for the initial clusters?

- [ ] Place k centroids at the centroid of the whole data sample.
- [x] Place k centroids at (0, 0).
- [ ] Place k centroids at the farthest distance from other centroids.
- [x] Place k random centroids.

#### The sklearn library comes with a breast cancer dataset with characteristics of breast cancer cell nuclei: mean radius, mean texture, mean perimeter, mean area, etc. What is a sample and what is a feature in this dataset?

    [[ 1.7990e+01  1.0380e+01  ...  2.6540e-01 ]
     [ 2.0570e+01  1.7770e+01  ...  8.9020e-02 ]

- [x] Each cell nuclei (row) is a sample and the mean radius (column) is a feature.
- [ ] Each cell nuclei (row) is a feature and the mean radius (column) is a sample.
