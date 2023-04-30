# Variable Types for Data Science

## Variable Types Quiz

#### Which of the .head() outputs would be appropriate after applying One-Hot Encoding to the major variable in the cafe_survey dataframe with the following line of code?

`cafe_survey = pd.get_dummies(data=cafe_survey, columns = ['major'])`

| name      | major_business | major_law | major_art | cafe_frequency | food_rating | would_recommend | dormitory   |
|-----------|----------------|-----------|-----------|----------------|-------------|-----------------|-------------|
| Jim H.    | 1              | 0         | 0         | rarely         | 1           | neutral         | Brent Hall  |
| Monty P.  | 0              | 0         | 1         | sometimes      | 7           | neutral         | missing     |
| Joey B.   | 0              | 0         | 1         | rarely         | 3           | disagree        | Jacobs Hall |
| Rachel M. | 0              | 1         | 0         | often          | 9           | strongly_agree  | Jacobs Hall |


#### Which of the variables in the following table are not Binary?

| purchased_in_store | used_coupon | usage    | delivered |
|--------------------|-------------|----------|-----------|
| 1                  | False       | On       | Yes       |
| 0                  | True        | Returned | Yes       |
| 0                  | True        | Off      | No        |
| 1                  | False       | Returned | Yes       |

- [x] `usage`
- [ ] `used_coupon`
- [ ] `delivered`
- [ ] `purchased_in_store`

#### Which of the following data types would be most appropriate for ordinal categorical data?

- [ ] `int` & `float`
- [ ] `float`
- [x] `int` & `str`
- [ ] `bool` & `str`

#### You would like to know the overall sentiment of your peers in regard to the Campus Cafeteria, and have gathered data through a survey. Your dataset cafe_survey contains the following variables:

| name      | email_address     | major    | cafe_frequency | food_rating | would_recommend | dormitory     |
|-----------|-------------------|----------|----------------|-------------|-----------------|---------------|
| Jim H.    | jh12@cauni.edu    | business | rarely         | 1           | neutral         | Brent Hall    |
| Monty P.  | monty5@cauni.edu  | art      | sometimes      | 7           | neutral         | missing       |
| Joey B.   | leblanc@cauni.edu | art      | rarely         | 3           | disagree        | Jacobs Hall   |
| Rachel M. | missing           | law      | often          | 9           | strongly_agree  | Franklin Hall |

name: The first name and last initial of the respondent.
email_address: The email address of the respondent.
major: The major that the respondent studies at the university.
cafe_frequency: How often a respondent eats at the cafeteria per week.
food_rating: The rating the respondent gives the quality of food on a 0-10 scale.
would_recommend: If the respondent would recommend eating in the cafeteria.
dormitory: The name of the dormitory that the respondent lives in.
Match each variable to its correct type:

```
    name: Nominal
    email_address: Nominal
    major: Nominal
    cafe_frequency: Ordinal
    food_rating: Ordinal
    would_recommend: Ordinal
    dormitory: Nominal
```

#### Complete the Python code to alter the food_rating column in the cafe_survey dataframe by replacing the missing value with 5, then change the data type of food_rating from int to float.

```python
# Change the missing value to 5
cafe_survey['food_rating']  =  cafe_survey['food_rating'].replace(['missing'], 5)
 
# Change the data type of food_rating to float
cafe_survey['food_rating']  =  cafe_survey['food_rating'].astype('float')
```

#### Complete the Python code to print the first five rows of the Pandas dataframe df.

```python
print(df.head())
```

#### Fill in the following lines of code to change the datatype of the cafe_frequency from str to category with an order of rarely < sometimes < often.

```python
cafe_survey['cafe_frequency'] = pd.Categorical(cafe_survey['cafe_frequency'], ['rarely', 'sometimes', 'often'], ordered = True)
```

#### How are ordinal categorical variables different from discrete quantitative variables?

- [x] Ordinal categories are not necessarily evenly spaced, while discrete quantitative values are.
- [ ] Ordinal categorical variables may represent counts, while discrete quantitative variables cannot.
- [ ] Discrete quantitative variables can be stored as integers, whereas ordinal categories cannot.

#### Which of the following variables has been assigned an inappropriate datatype?

`print(product.head())`

| num_of_items | used_coupon | usage    | delivered |
|--------------|-------------|----------|-----------|
| 5            | False       | On       | Yes       |
| 2            | True        | Returned | Yes       |
| 1            | True        | Off      | No        |
| 1            | False       | Returned | Yes       |

`print(product.dtypes)`

| num_of_items   | object |
|----------------|--------|
| used_coupon    | bool   |
| usage          | object |
| delivered      | object |
| dtypes: object |        |

- [x] `num_of_items`
- [ ] `usage`
- [ ] `delivered`
- [ ] `used_coupon`

#### Which of the following would be the appropriate output of calling dtypes on the Cafeteria Survey dataframe?

| name            | object |
|-----------------|--------|
| email_address   | object |
| major           | object |
| cafe_frequency  | object |
| food_rating     | int64  |
| would_recommend | object |
| dormitory       | object |
| dtype: object   |        |

#### Which of the following quantitative variables is discrete?

| num_of_pets | weekly_food_costs |
|-------------|-------------------|
| 3           | 42.15             |
| 1           | 12.08             |
| 0           | 0.0               |
| 2           | 22.38             |
| 2           | 29.17             |

- [x] num_of_pets
- [ ] weekly_food_costs

