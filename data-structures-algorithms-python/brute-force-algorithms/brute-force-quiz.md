#### You are looking for a novel at the local library. There are 10 bookshelves in the library, each bookshelf consists of 5 rows, and each row is filled with 20 books. Using a brute force approach, how many books would you need to look through in the worst-case scenario?

- [ ] 50 books
- [ ] 20 books
- [x] 1000 books
- [ ] 100 books

#### Fill in the blanks to complete the following linearSearch() function. As a reminder, this function returns the index of the first element in searchList that matches targetValue.

    def linearSearch(searchList, targetValue):
      for i in range(len(searchList)):
        if (searchList[i] == targetValue):
          return i
      return -1


#### Compared to optimized algorithms, brute force algorithms are usually:


- [ ] Slower and more difficult to implement
- [x] Slower and easier to implement
- [ ] Faster and more difficult to implement
- [ ] Faster and easier to implement


#### Given the list of numbers, how many comparisons would linear search require in order to find 89 in the list?

      1, 10, 23, 94, 83, 35, 22, 44, 23, 67

- [x] 10
- [ ] Linear search is unable to perform a search on the list.
- [ ] 4
- [ ] 0


#### Consider the given code. What will be returned by the function call linearSearch(numberList, 23) ?

    def linearSearch(searchList, targetValue):
      for i in range(len(searchList)):
        if (searchList[i] == targetValue):
          return i
      return -1

    numberList = [ 1, 10, 23, 94, 23, 67 ]
    linearSearch(numberList, 23)

- [ ] 5
- [ ] 4
- [x] 2
- [ ] 3


#### What is the time complexity for linear search in Big-O notation?

- [ ] log N
- [ ] N
- [x] O(N)
- [ ] O(log N)


#### You are given the code for the greaterSearch() function, which searches for elements in searchList that have values greater than targetValue. What does this function return if there are matches?

    def greaterSearch(searchList, targetValue):
      result = []
      for i in range(len(searchList)):
        if (searchList[i] > targetValue):
          result.append(searchList[i])
       return result

- [ ] The index of the first value in searchList that is greater than targetValue.
- [x] Returns a list of all values greater than targetValue in searchList.
- [ ] Returns a list of indices of all values greater than targetValue in searchList.
- [ ] Return the first value in searchList that is greater than targetValue.
