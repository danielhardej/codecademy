# Portfolopio Optimization
## Mean Variance Optimization Quiz

#### Which of the following is true for a portfolio of assets that maximizes expected return?

- [ ] It is the riskiest portfolio option.
- [ ] All money is invested in the asset with the lowest variance.
- [ ] It does not fall on the efficient frontier.
- [x] Money is invested in only one asset.

#### You have a portfolio with 15 stocks and choose asset weights that minimize the risk of your portfolio. If you were to add 5 additional stocks to the portfolio and reallocate asset weights, how would you expect the risk of your new portfolio to compare to the original?

- [ ] More risk or stay close to the same
- [ ] Less risk
- [ ] More risk
- [x] Less risk or stay close to the same

#### This figure displays the efficient frontiers for portfolios with three different sets of assets. Which portfolio displays the best efficient frontier?

![efficient frontiers for portfolios with two different sets of assets][def]

- [ ] There is not enough information to determine which is the best efficient frontier.
- [ ] Bottom (Yellow)
- [x] Top (Black)
- [ ] Middle (Green)

*Nice work, this efficient frontier has a greater expected return for the same level of risk as portfolios on the other efficient frontiers. The top line also has portfolios with the lowest risk.*

#### A function called `optimal_portfolio()` returns values for a set of portfolios on the efficient frontier. Which of the following would you not expect this function to return?

- [x] A 2D array with the expected return of all assets from a randomly selected set of portfolios
- [ ] An array with the variance of each portfolio on the efficient frontier
- [ ] A 2D array with the weights of all assets in each portfolio on the efficient frontier
- [ ] An array with the expected return of each portfolio on the efficient frontier


#### The `quarterly_asset_values` variable is a seven-column data frame with quarterly asset values over the last 20 quarters. Which of the following will calculate the covariance matrix for these assets?


- [ ] covariance_matrix = pd.cov(quarterly_asset_values)
- [ ] covariance_matrix = quarterly_asset_values.cov()
- [x] returns_quarterly = quarterly_asset_values.pct_change()
      covariance_matrix = returns_quarterly.cov()
- [ ] covariance_matrix = quarterly_asset_values.diff().cov()


#### Which of the following is true for a portfolio of assets that minimizes risk?

- [ ] There is no investment in high-risk assets.
It is the portfolio with the lowest expected return.
There is investment in only one asset.
- [x] There is investment in more than one asset.

#### Why is it important to consider covariance when allocating money between multiple assets?

- [ ] Covariance measures the degree to which the expected returns of two assets change together. Covariance can be used to calculate the expected return of a portfolio.
- [ ] Covariance measures the degree to which the variance of two assets change together. The covariance of assets in a portfolio can be used to calculate the risk of a portfolio.
- [x] Covariance measures the degree to which the expected returns of two assets change together. The covariance of assets in a portfolio can be used to calculate the risk of a portfolio.
- [ ] Covariance matrices hold the standard deviation of each asset. The covariance matrix is used to calculate the spread of expected returns in a set of possible portfolios.

#### What are the asset weights for an airline portfolio with $1,000 in United Airlines, $1,500 in Delta Airlines, and $2,500 in Alaskan Airlines?

- [x] United: .2 Delta: .3 Alaskan: .5
- [ ] United: .1 Delta: .15 Alaskan: .25
- [ ] United: .1 Delta: .2 Alaskan: .7
- [ ] United: .1 Delta: .3 Alaskan: .6

#### You have a portfolio with $1,000 in asset A, $2,000 in asset B, and $2,000 in asset C. For each asset, the expected quarterly returns are: asset A = 3%, asset B = 2%, and asset C = 1%. What is the expected return of your portfolio over the next quarter?

- [ ] $150
- [x] $90
- [ ] $70
- [ ] $50

#### The quarterly_asset_values variable is a seven-column data frame with quarterly asset values over the last 20 quarters. Which of the following lines can be used to find the average percent return of each asset in quarterly_asset_values?

- [ ] `quarterly_asset_values.diff().mean()`
- [x] `quarterly_asset_values.pct_change().mean()`
- [ ] `quarterly_asset_values.mean().diff()`
- [ ] `quarterly_asset_values.mean()`



[def]: https://content.codecademy.com/programs/python-for-finance/portfolio-optimization/quiz_last_question.png