# Probability For Data Science

## Probability Distributions Quiz

#### Fill in the blanks to create code that will calculate the probability of observing more than 3 and fewer than 7 heads from 10 fair coin flips.

``` python
import scipy.stats as st
 
st.binom.cdf(6, n=10, p=0.5) - st.binom.cdf(3, n=10, p=0.5)
```

#### Let’s say we want to know how hot it will be at the beach on a given day in the summer. We know that temperatures on this beach are normally distributed and that the average temperature is 35 degrees Celsius. Using the probability density function, what is the probability that the temperature will be exactly 35 degrees?

 - [ ] 1
 - [ ] 0.5
 - [x] 0

#### Fill in the blanks to make the following statements true.

For a continuous random variable, the probability density function (PDF) is such that the area under the curve in a given range is equal to the probability of the random variable equalling a value in that range.

#### Which of the following statements about random variables is FALSE?

 - [ ] A random variable can be either discrete or continuous.
 - [ ] Even when a specific outcome is very likely, there is still the possibility that a random variable takes on a different value.
 - [x] Random variables are the actual numbers you get when you run experiments.
 - [ ] Random variables are functions with numerical outcomes.

#### Fill in the code to produce the probability of observing exactly 3 heads in 10 fair coin flips.

```python 
import scipy.stats as st
 
st.binom.pmf(3, n=10, p=.5)
```

#### Fill in the correct vocabulary in the following statements:

A discrete random variable has a countable number of possible values. These random variables are often observed when counting something such as the number on a die roll or number of people in a room.
 
A continuous random variable has an uncountable number of possible values. These random variables are often measurements of some kind. For example time, distance, or temperature. 

#### Which of the following is the correct way to interpret the parameters n and p of the binomial distribution?

 - [ ] n is the number of successes we expect to see from all of the trials, and p is the probability of success over all trials.
 - [x] n is the number of trials, and p is the probability of success in each trial.
 - [ ] n is the number of successes we expect to see from all of the trials, and p is the probability of success in each trial.
 - [ ] n is the number of trials, and p is the probability of success over all trials.

#### Let’s say we are drawing a random card from a regular 52-card deck and replacing it back to the deck and shuffling after each observation. We repeat this experiment 7 times and are interested in how many of the 7 cards are hearts.

What would n and p equal in this situation?

 - [x] n = 7, p = 0.25
 - [ ] n = 52, p = 0.25
 - [ ] n = 364 (52*7), p = 0.25
 - [ ] n = 7, p = 0.5

#### Which of the following is the correct way to interpret the probability mass function?

 - [ ] The probability mass function only works for random variables that have a 50% chance of success, such as observing heads on a fair coin flip.
 - [ ] The probability mass function defines what value we will see in a random event.
 - [x] The probability mass function defines the probability that a random variable equals a specific value.
 - [ ] The probability mass function defines the probability that a random variable equals a specific value or less.

#### Which of the following is TRUE about cumulative density functions?

 - [x] The cumulative density function of a random variable defines the probability of observing a value less than or equal to a specific number.
 - [ ] Cumulative density functions are only for discrete random variables.
 - [ ] When graphed, cumulative density functions are always a smooth, continuous curve.
 - [ ] Cumulative density functions calculate the probability of observing an exact number.
