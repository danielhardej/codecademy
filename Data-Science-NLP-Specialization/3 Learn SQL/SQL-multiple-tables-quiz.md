# Learn SQL

## Multiple Tables Quiz

#### You have two tables authors and books. Each book belongs to an author and references that author through a foreign key. If the primary key of the authors table is id, what would be the most sensical name for a foreign key in the books table that references the id column in authors?

- [ ] id
- [x] author_id
- [ ] foreign_key

#### In a LEFT JOIN, if a join condition is not met, what will it use to fill columns on the right table?


- [x] NULL values
- [ ] id
- [ ] column_name.id
- [ ] primary keys

#### You have two tables teachers and students. Each student belongs to a teacher. Complete the query to join the tables on the teacher id.

    SELECT *
    FROM students
    JOIN teachers
      ON __________________;

- [x] students.teacher_id = teachers.id
- [ ] teachers_id = id
- [ ] teachers.id = student_id
- [ ] teachers = students.id

#### UNION allows us to stack one dataset on top of another.

- [ ] False
- [x] True

#### Which kind of join is in the animation below?

![An animation of two tables being joined into one. At the beginning of the animation, there are two tables side by side. The left table has columns "C1" and "C2". Column "C1" has values [A, Q, X] and Column "C2" has values [B, W, Y]. The table on the right has columns "C2" and "C3". Column "C2" has values [B, E, Y] and Column "C3" has values [C, R, Z]. The animation shows these two tables joining together on column "C2". After the join, there is only one table with the columns "C1", "C2", and "C3".  Column "C1" has values [A, X], Column "C2" has values [B, Y], and Column "C3" has values [C, Z].](https://content.codecademy.com/courses/learn-sql/multiple-tables/inner-join-quiz.gif)

- [x] INNER JOIN
- [ ] RIGHT JOIN
- [ ] CROSS JOIN
- [ ] LEFT JOIN

#### What is the best definition of a foreign key?

- [ ] A NULL value.
- [ ] A primary key that is not present when a table is created but is later added.
- [x] A column that contains the primary key of another table in the database.
- [ ] A unique identifier for each row or record in a given table.

#### Which keyword would you use to alias recipes.name and chefs.name in the following query’?

    SELECT recipes.name __ 'Recipe',
       chefs.name __ 'Chef'
    FROM recipes
    JOIN chefs
      ON recipes.chef_id = chefs.id;

- [x] AS
- [ ] ALIAS
- [ ] WITH
- [ ] ON

#### What is the best definition of a primary key?

- [ ] A foreign key with distinct attributes.
- [ ] A primary record in a database that serves as a template for all other records.
- [ ] A NULL value.
- [x] A unique identifier for each row or record in a given table.

#### Why is a CROSS JOIN not so useful?

- [ ] It is no longer supported by SQL.
- [ ] It combines all foreign keys into one table called foreign keys.
- [ ] It nullifies all primary keys.
- [x] It combines every row in one table with every row in another table.

#### What is the difference between an INNER JOIN and a LEFT JOIN?

- [ ] A LEFT JOIN is an obsolete form of an INNER JOIN.
- [x] LEFT JOIN combines rows from two or more tables, but unlike INNER JOIN, it does not require the join condition to be met.
- [ ] An INNER JOIN joins rows within a table. A LEFT JOIN joins rows between tables.
- [ ] An INNER JOIN is an obsolete form of a LEFT JOIN.
