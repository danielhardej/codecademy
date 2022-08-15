#### Fill in the code to perform a bin transformation on the following array:

    #array of numbers
    awesome_nums = [9,  5, 46, 18,  8, 33,  9, 26, 11, 31, 45, 29,  1, 35, 11,  5, 36,
           34, 33, 19, 25,  8, 20, 38, 35, 24, 37, 34, 41, 24, 33, 11,  4, 14,
           18, 17, 26, 46, 48,  1]

    #set bin limits
    bins = [10, 20, 30, 40, 50]
    awesome_binned = pd.cut(awesome_nums, bins)

#### When we center our data, we are centering around what metric?

- [ ] Mode
- [ ] Median
- [ ] Range
- [x] Mean

#### Fill in the code to perform a standard scaler on the following array:

    awesome_nums = [18602, 92442, 41, 56794, 107, 96188, 12, 43, 676, 43263, 631, 72368, 226, 83426, 986, 364, 1669, 95154, 19, 790, 562, 186, 44, 60, 73556, 68587, 184, 44, 15]

    import numpy as np

    awesome_nums_mean = np.mean(awesome_nums)
    awesome_nums_std_dev = np.std(awesome_nums)
    awesome_nums_standardized = (awesome_nums - awesome_nums_mean) /  awesome_nums_std_dev


#### Fill in the code to perform a min/max scaler on the following array:

    awesome_nums = [18602, 92442, 41, 56794, 107, 96188, 12, 43, 676, 43263, 631, 72368, 226, 83426, 986, 364, 1669, 95154, 19, 790, 562, 186, 44, 60, 73556, 68587, 184, 44, 15]
    import numpy as np

    array_minimum = np.min(awesome_nums)
    array_maximum = np.max(awesome_nums)
    array_range = array_maximum - array_minimum

    awesome_minmax = (awesome_nums - array_minimum) / array_range  


#### What NumPy method would you use to perform a logarithmic transformation?

    log_car = np.____(cars['odometer'])

- [ ] natural_log
- [ ] logs
- [ ] logarithmic
- [x] log

#### After we perform a standard scaler, we expect our Mean and Standard Deviation to have what values?

- [ ] Mean = minimum value, Standard Deviation = maximum value
- [x] Mean = 0, Standard Deviation = 1
- [ ] Mean = 1, Standard Deviation = 0

#### Logarithms are an essential tool in statistical analysis and machine learning preparation. This transformation works well with what type of data?

- [ ] Left-skewed
- [x] Right-skewed
