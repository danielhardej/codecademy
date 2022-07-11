## Data Structures in Python: Hash Maps Quiz

#### Given a hash table that handles collisions, which of the following need to be saved so that values can be assigned, reassigned, and looked up?

    - The Key
    - The Hash Code
    - The Array Index
    - The Value

- [x] The key and the value.
- [ ] Just the value.
- [ ] The array index and the value.
- [ ] The hash code and the value.

#### Which of the following is true of a hash function?

- [ ] Two different inputs can never have the same output.
- [ ] It can’t accept integers as input.
- [ ] It performs a complicated numerical calculation.
- [x] It is not reversible.

#### How does a hash map turn the hash code for something into an array index?

(Selected)Correct:
- [x] Using the modulus operator, usually via a compression method.
- [ ] By dividing the hash code into four different possibilities and choosing the one that’s empty.
- [ ] A hash map picks the next available space in the underlying array.


#### What does the collision strategy called Open Addressing do when it finds a collision?

- [x] Looks for another cell in the underlying array to add the value to.
- [ ] Adds the value to an underlying linked list implementation.
- [ ] Ignores the assignment and waits for the next method call.
