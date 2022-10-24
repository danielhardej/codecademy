# Learn C++
## C++ Classes and Objects Quiz

#### Instantiate a City object called seoul with (in this order):

- name set to "Seoul".
- population set to 9776000.

    City seoul("Seoul", 9776000);

#### Define a method .add_resident() for a City class. (This method is defined in a .cpp file, not inside the class.) City has a population attribute that tracks the number of residents.

    #include "city.hpp"

    void City::add_resident() {

      population++;

    }

#### Build an empty class for cities.

class City {

  // class members go here

};

#### What is not possible to do with a Country object?

    class Country {
    private:

      std::string name;

    public:

      Country(std::string new_name)
        : name(new_name) {}

      std::string get_name() {

        return name

      }

    };

- [ ] You cannot retrieve a Country instance’s name attribute.
- [ ] You cannot create a Country object with a name attribute.
- [x] You cannot change a Country instance’s name attribute.

#### Why are destructors helpful in C++?

- [ ] Without defining a destructor, there is no way to destroy an object.
- [x] A destructor allows you to conduct any final cleanup necessary before an object is destroyed.
- [ ] A destructor allows you to destroy a class.

#### Which of the following are class members of Country?

    class Country {
    private

      std::string name;

    public:

      Country(std::string new_name)
        : name(new_name) {}

      std::string get_name() {

        return name

      }

    };

- [ ] The Country constructor is the only class member.
- [ ] The .get_name() method is the only class member.
- [ ] The name attribute is the only class member.
- [x] name, the Country constructor, and .get_name() are all class members.
