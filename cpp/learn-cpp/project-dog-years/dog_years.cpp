#include <iostream>

int main() {

  // declare and assign variable for dog's age
  int dog_age;
  std::string dog_name;

  std::cout << "Hello! Enter your dog's age: \n";
  std::cin >> dog_age;
  std::cout << "Hello! Enter your dog's name: \n";
  std::cin >> dog_name;

  int early_years = 21;        //The first two years of a dog’s life count as 21 human years.
  int later_years = (dog_age - 2)*4;  //Each following year counts as 4 human years.
  int human_years;

  if(dog_age >2) {
    // statement(s) will execute if the boolean expression is true
    human_years = early_years + later_years;
  } else {
    human_years = early_years;
  }

  std::cout << "My name is " << dog_name <<"! Ruff ruff, I am " << human_years << " years old in human years.\n";

}
