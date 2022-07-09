#### Fill in the code to complete Queue‘s __init__() method.

   def __init__(self, max_size=None):
     self.size = 0
     self.head = None
     self.tail = None
     self.max_size = max_size


#### What should be the if statement for .has_space()?

   def has_space(self):
     if ???:
       return self.max_size > self.get_size()
     else:
       return True

- [ ] self.size > 0
- [ ] self.get_size()
- [ ] self.is_empty()
- [x] self.max_size


#### What will the return value be if we add a final statement calling .dequeue() on sharks_in_the_shark_tank?

    sharks_in_the_shark_tank = Queue(5)

    sharks_in_the_shark_tank.enqueue("Alex")
    sharks_in_the_shark_tank.enqueue("Alisha")
    sharks_in_the_shark_tank.dequeue()
    sharks_in_the_shark_tank.enqueue("Kenny")


- [ ] A node with a value of “Alisha”
- [ ] “Kenny”
- [x] “Alisha”
- [ ] A node with a value of “Alex”


#### Which two Queue methods should alert that the queue is empty?

- [ ] .__init__() and .enqueue()
- [ ] .__init__() and .peek()
- [ ] .enqueue() and .dequeue()
- [x] .dequeue() and .peek()


#### In which of the following scenarios, would a queue NOT be the ideal data structure to model the situation?

-[x] Pile of dirty plates in the sink.
- [ ] Cars sitting through traffic.
- [ ] Waiting in line for groceries.


#### If you instantiate an empty queue, what should self.head and self.tail be set to?

- [x] None and None
- [ ] head and None
- [ ] None and tail
- [ ] head and tail


#### .is_empty() is a useful method for preventing __.

- [ ] queue overflow
- [x] queue underflow


#### Why is .has_space() a useful method for the Queue class to have?

- [x] It allows us to see if we can .enqueue() a new value on the end of the queue.
- [ ] It allows us to see if we can .dequeue() the first item on the queue.
- [ ] It allows us to see if we can .peek() the first item on the queue.
- [ ] It allows us to see if the queue is empty.


#### In what case would queue underflow occur?

- [ ] Enqueuing data onto an empty queue.
- [x] Dequeuing data from an empty queue
- [ ] Dequeuing data from a full queue.
- [ ] Enqueuing data onto a full queue.


#### Take a look at the following code based on the Queue class you’ve been working with. What do we know is true for muffins_to_be_eaten?

    muffins_to_be_eaten = Queue(10)

    muffins_to_be_eaten.enqueue("blueberry")
    muffins_to_be_eaten.enqueue("corn")
    muffins_to_be_eaten.peek()
    muffins_to_be_eaten.dequeue()

- [x] muffins_to_be_eaten.head == muffins_to_be_eaten.tail
- [ ] muffins_to_be_eaten.max_size == muffins_to_be_eaten.size
- [ ] muffins_to_be_eaten now has 11 nodes.
- [ ] The remaining node has a value of “blueberry”.

#### If the following queue was implemented using a linked list, what would the linked list look like if “Adam” was enqueued?

    Queue: Charlie -> Bob -> Ann
    Front: Ann
    Back: Charlie

- [ ] Adam -> Charlie-> Bob
- [x] Adam -> Charlie -> Bob -> Ann
- [ ] Ann -> Bob -> Charlie -> Adam
- [ ] Bob -> Charlie -> Adam
