# Learn SQL
## Aggregate Functions Quiz

#### Aggregate functions …

- [ ] return the total sum of the values in a numeric column.
- [ ] count the number of rows where the value(s) is not NULL.
- [ ] round the values of a column.
- [x] compute a single result set from a set of values.

#### What does the ROUND function take as argument(s)?

- [x] The column name, and the number of decimal places to round the values in the column to.
- [ ] The table name.
- [ ] The column name, and a + or - sign to indicate rounding up or rounding down.
- [ ] It does not take an argument.


#### Which function takes a column and returns the total sum of the numeric values in that column?

- [x] SUM()
- [ ] AVG()
- [ ] COUNT()
- [ ] MAX()


#### How would you calculate the minimum number of stops from the train table?

- [ ]
    SELECT MAX(stops)
    FROM train;

- [ ]
    SELECT AVG(stops)
    FROM train;

- [x]
    SELECT MIN(stops)
    FROM train;

- [ ]
    SELECT SUM(stops)
    FROM train;


#### What does the COUNT() function take as argument(s)?

- [ ] The name of a database.
- [ ] The name of a table.
- [ ] The name of a row.
- [x] The name of a column or *.


#### What does the following query do?

    SELECT neighborhood,
       AVG(price)
    FROM apartments
    GROUP BY neighborhood;

- [ ] It calculates the lowest price of apartments in each neighborhood.
- [ ] It calculates the total number of apartments in each neighborhood.
- [x] It calculates the average price of apartments in each neighborhood.
- [ ] It calculates the highest price of apartments in each neighborhood.


#### Find the error in this code:

    SELECT COUNT(*)
    FROM songs
    HAVING plays > 100;

- [ ] There is no such thing as COUNT(*).
- [ ] There is no error.
- [ ] It should be GROUP BY instead of HAVING.
- [x] It should be WHERE instead of HAVING.


#### What does the following query do?

    SELECT price,
       COUNT(*)
    FROM menu
    WHERE orders > 50
    GROUP BY price;

- [x] It calculates the total number of menu items that have been ordered more than 50 times – for each price.
- [ ] It calculates the total number of menu items that have been ordered more than 50 times – sorted by price.
- [ ] It calculates the total number of menu items.
- [ ] It calculates the total number of menu items that have been ordered more than 50 times.


#### What does the following query do?

    SELECT genre,
       SUM(downloads)
    FROM kindle
    GROUP BY genre;

- [ ] It returns the total amount of downloads.
- [ ] It returns the highest number of downloads – for each genre.
- [ ] It returns the average number of downloads – for each genre.
- [x] It returns the total amount of downloads – for each genre.


#### The WHERE clause filters rows, whereas the HAVING clause filter groups.

- [ ] False
- [x] True
