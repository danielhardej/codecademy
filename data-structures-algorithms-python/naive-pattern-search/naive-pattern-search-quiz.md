#### In the worst case, what can the run-time performance of naive pattern searching approach?

- [ ] O(log(n))
- [x] O(n^2)
- [ ] O(n * log(n))
- [ ] O(n)

#### Complete the missing part of the conditional statement:

    def pattern_search(text, pattern):
      for index in range(len(text)):
        match_count = 0
        for char in range(len(pattern)):
          if pattern[char] == text[index + char]:
            match_count += 1
          else:
            break

#### It is possible for an algorithm to search a generic text in less than O(n) time.

- [ ] True
- [x] False

#### What is the runtime of naive pattern search?

- [ ] O(n^2)
- [x] O(nk)
- [ ] O(n)
- [ ] O(n * log(n))

#### What is the main cause for the growth of naive pattern search’s run time?

- [x] The constant backtracking to the next character of the input text.
- [ ] The length of the pattern.
- [ ] The length of the text.
- [ ] The number of possible characters.

#### Complete the missing part of the conditional statement:

    def pattern_search(text, pattern):
      for index in range(len(text)):
        match_count = 0
        for char in range(len(pattern)):
            if pattern[char] == text[index + char]:
                match_count += 1
            else:
                break
        if match_count == len(pattern):
            print(pattern, "found at index", index)

#### In the worst-case, how many times will each character in the text be compared to the pattern?

- [ ] The length of the text minus the length of the pattern.
- [ ] The length of the text.
- [x] The length of the pattern.
- [ ] Once.
