#### What does the hasattr() function call in the last line here evaluate to?

    class HoldsFive:
      five = 5

    five_holder = HoldsFive()

    hasattr(five_holder, 'five')

- [ ] 5
- [ ] False
- [x] True

#### What would be printed from the following code?

    class User:
      def __init__(self, name):
        self.name = name

      def __repr__(self):
        return "Hiya {}!".format(self.name)

    devorah = User("Devorah")
    print(devorah)

- [ ] Devorah
- [ ] Hiya devorah!
- [ ] devorah
- [x] Hiya Devorah!

#### What function, defined within a class, provides instructions on what to assign to a new instance when it is created?

- [x] __init__
- [ ] init
- [ ] __new__
- [ ] __create__

#### What is the first argument of a method?

- [x] The instance of the object itself. We usually refer to it as self.
- [ ] The class itself. We usually refer to it as self.
- [ ] The context in which the object is created. We usually name the parameter this.

#### How would we create an instance of the following class?

    class NiceClass:
      neat_attribute = "neat"

- [ ] nice_instance = new NiceClass
- [x] nice_instance = NiceClass()
- [ ] nice_instance = NiceClass

#### What keyword is used to indicate the start of a class definition?

- [ ] type
- [ ] __init__
- [ ] def
- [x] class

#### What does the type() function do in Python?

- [x] Returns the class that an object implements.
- [ ] Returns an implementation of a class.
- [ ] Returns a string that’s the name of the class.
- [ ] Returns a type object that contains some metadata about the class.
