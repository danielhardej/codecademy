#### Principal Components, or eigenvectors, determine:

- [x] the direction / rotation for a data space
- [ ] the behavior of new data coming in
- [ ] how much features vary in relation to one another
- [ ] the importance of a particular feature

#### Which of the following is not a good use case for PCA?

- [ ] Dimensionality Reduction
- [ ] Image Processing
- [ ] Cluster Analysis
- [x] Dimensionality Expansion

#### Which of these statistical concepts is the foundation for PCA?

- [ ] Correlation
- [x] Covariance
- [ ] Standard Deviation

#### For a given dataset, we can calculate the following Coefficients of Variance:

    price            1.034042
    units     2.216437
    unit_cost           1.040315
    unit_profit        1.608712

##### Determine the most important and least important features for PCA.

    Most important: units
    Least important: price

#### What is the main goal of PCA?

- [ ] To eliminate unnecessary features.
- [x] To get better features without losing information.
- [ ] To make datasets as small as possible.
- [ ] To transform the dataset as much as possible.

#### Which of the following shows the correct format for a covariant matrix for a dataset with three features: x, y, and z?

#### We have a dataset called data, and would like to perform PCA on it. Fill in the code to reduce our dataset down to 3 dimensions, and then have the PCA model modify the dataset.

    pca = PCA(n_components=3)
    new_data = pca.fit_transform(data)

#### When using PCA, you can only produce a resulting dataset with two dimensions.

- [ ] True
- [x] False
