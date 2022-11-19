# Learn SQL
## SQL Queries Quiz

#### Which operator would you use to query values that meet all conditions in a WHERE clause?

![Venn Diagram](https://content.codecademy.com/courses/learn-sql/queries/and-quiz.svg)

- [ ] OR
- [x] AND
- [ ] LIKE
- [ ] BETWEEN

#### What is the correct query to select only the cities with temperatures less than 35?

- [ ]
    SELECT *
    FROM cities
    WHERE temperature = 35;
- [x]
    SELECT *
    FROM cities
    WHERE temperature < 35;
- [ ]
    SELECT *
    FROM cities
    WHERE temperature != 35;
- [ ]
    SELECT *
    FROM cities;

#### Find the error in this code:

    SELECT name,
     CASE
      WHEN imdb_rating > 8 THEN 'Oscar'
      WHEN imdb_rating > 7 THEN 'Good'
      WHEN imdb_rating > 6 THEN 'Fair'
    FROM movies;

- [ ] Not enough WHEN/THEN statements.
- [ ] The column was not renamed.
- [x] Missing END statement.
- [ ] Missing ELSE statement.

#### How would you query all the unique genres from the books table?

- [ ]
  SELECT UNIQUE genres
  FROM books;

- [x]
  SELECT DISTINCT genres
  FROM books;
- [ ]
  FROM books
  SELECT DISTINCT genres;
- [ ]
  SELECT genres
  FROM books;

#### What code would you add to this query to order colors by name alphabetically (Z to A)?

    SELECT *
    FROM colors
    _________________;

- [ ] ORDER BY name ASC
- [x] ORDER BY name DESC
- [ ] ORDER BY name
- [ ] GROUP BY name ASC

#### Which of the following is NOT a comparison operator in SQL?

- [ ] !=
- [x] ~
- [ ] <
- [ ] >=

#### What is LIKE?

- [ ] A clause used to bookmark columns that are frequently queried.
- [x] A special operator that can be used with the WHERE clause to search for a pattern.
- [ ] A clause used to select unique values from a table.
- [ ] A statement that allows us to create different outputs.

#### What does the wildcard character % in the following SQL statement do?

    SELECT *
    FROM sports
    WHERE name LIKE '%ball';

- [ ] It matches all sports that have a pattern like ‘ball’, such as ‘b3ll’ and ‘b@ll’.
- [ ] It matches all sports that contain ‘ball’.
- [x] It matches all sports that end with ‘ball’.
- [ ] It matches all sports that begin with ‘ball’.

#### What is ORDER BY?

- [ ] An operator used with the WHERE clause.
- [ ] A clause that allows you to select unique values.
- [x] A clause that sorts the result set alphabetically or numerically.
- [ ] A clause that sorts the result set in alphabetical order only.

#### What is the correct syntax to query both the name and date columns from the database?

    SELECT __________
    FROM album;

- [ ] name + date
- [x] name, date
- [ ] name; date
- [ ] name & date

#### IS NULL condition returns true if the field is empty.

- [ ] False
- [x] True

#### What is LIMIT?

- [ ] A clause that lets you specify the maximum number of columns the result set will have.
- [ ] A clause that is used to return unique values in the output.
- [ ] A clause that restricts our query results in order to obtain only the information we want.
- [x] A clause that lets you specify the maximum number of rows the result set will have.
