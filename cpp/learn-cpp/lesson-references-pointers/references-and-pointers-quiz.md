# Codecademy Learn C++
## References and Pointers Quiz

#### What is a memory address?

- [x] The location in the memory, of an object.
- [ ] The alias for something else.
- [ ] A keyword that tells the compiler that we won’t change something.
- [ ] A variable that stores a location.

#### What would the output be for a program like this:

    #include <iostream>

    int main() {

      double sofa = 600;

      double &couch = sofa;

      couch = couch + 40;

      std::cout << sofa << "\n";

    }

- [ ] 600
- [x] 640
- [ ] 0x7fff374573ac
- [ ] sofa

*Because couch is a reference to sofa, when couch changes, sofa also changes. So 600 + 40 = 640.*

#### What is the difference between a reference and a pointer?

- [ ] References can be changed to alias something else.
- [ ] A pointer is more modern and it’s originated in C++.
- [x] A reference is an alias for something else, while a pointer stores the memory address of something else.

*Pointers are an older mechanism that was inherited from C, while references are a new mechanisms that originated in C++.*

#### What would the output be for a program like this:

    #include <iostream>

    void square(int &i) {

      i = i * i;

    }

    int main() {

      int num = 5;

      square(num);

      std::cout << num << "\n";

    }

- [ ] 0x7ffd7caa5b54
- [ ] 5
- [x] 25
- [ ] 10


#### What should go in the blank to pass-by-reference with const?

    int square(int const &i) {

      return i * i;

    }

    int main() {

      int side = 5;

      std::cout << square(side) << "\n";

    }
