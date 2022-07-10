## Codecademy - Python Data Structures
## Stacks Quiz

#### In which of the following scenarios, would a stack NOT be the ideal data structure to model the situation?

- [x] A line in a grocery store.
- [ ] Dirty plates in a sink.
- [ ] Using the back and forward arrows in an internet browser to navigate through pages.


#### If I “peeked” at the following stack using peek(), what value would be returned, and what would the new stack look like from top to bottom?

      Stack:
      |55|
      |60|
      |50|
      ----
      Top Value: 55
      Bottom Value: 50

- [ ] Return Value: 50, Stack: [55, 60, 50]
- [ ] Return Value: 55, Stack: [60, 50]
- [x] Return Value: 55, Stack: [55, 60, 50]
- [ ] Return Value: 50, Stack: [55, 60]


#### In what case would “stack overflow” occur?

- [ ] Pushing data onto an empty stack.
- [ ] Popping data from a full stack.
- [x] Pushing data onto an already full stack.
- [ ] Popping data from an empty stack.


#### Which method would this line of code belong in?

    self.size -= 1

- [ ] .__init__()
- [ ] .push()
- [x] .pop()
- [ ] .peek()


#### If the following stack was implemented using a linked list (with the head node of the linked list representing the top of the stack), what would the linked list look like if a 40 pound gym plate was “pushed” onto the stack?

    Stack:
    |55|
    |60|
    |50|
    ----
    Top Value: 55
    Bottom Value: 50
    Value to Add: 40

- [ ] 55 -> 60 -> 50 -> 40
- [ ] 40 -> 55 -> 60
- [x] 40 -> 55 -> 60 -> 50
- [ ] 60 -> 50 -> 40


This stack class method could be useful because it allows us to:

    def some_method(self):
      return self.limit > self.size

- [ ] Check if the stack is empty.
- [ ] Check the number of nodes that exist in the stack.
- [ ] Check how many nodes can still be added to the stack.
- [x] Check if there’s enough space to add another node.




#### Fill in the code for Stack‘s .is_empty() method so that you can use it to check if a stack is empty.

    class Stack:
     def __init__(self, limit=1000):
       self.size = 0
       self.top_item = None
       self.limit = limit

     def is_empty(self):
       return self.size == 0


#### In .__init__(), what purpose does the line self.limit = limit serve?

 def __init__(self, limit=8000):
   self.size = 0
   self.top_item = None
   self.limit = limit

- [x] It sets a limit for the number of nodes that can be added to the stack at any one time.
- [ ] It sets a limit for the number of stacks that can be created by the Stack class.
- [ ] It sets a limit for the total number of nodes that can ever be instantiated within the stack.
- [ ] It sets a limit for the number of strings that can be added to the stack.


#### True or False: You can traverse a stack through its nodes.


- [x] False
- [ ] True


#### If we popped a value from the following stack, what value would be returned, and what would the new stack look like from top to bottom?

      Stack:
      |55|
      |60|
      |50|
      ----
      Top Value: 55
      Bottom Value: 50

- [ ] Return Value: 55, Stack: [55, 60, 50]
- [ ] Return Value: 50, Stack: [55, 60]
- [ ] Return Value: 50, Stack: [55, 60, 50]
- [x] Return Value: 55, Stack: [60, 50]


#### Which values go where in a stack’s .__init__() method?

     def __init__(self, limit=55):
       self.size = 0
       self.top_item = None
       self.limit = limit
