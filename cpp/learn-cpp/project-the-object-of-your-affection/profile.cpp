#include "profile.hpp"
#include <iostream>

Profile::Profile(std::string new_name, int new_age, std::string new_city, std::string new_country) {

  name = new_name;
  age = new_age;
  city = new_city;
  country = new_country;

}

std::string Profile::view_profile() {

  std::string profile = "Name: " + name;
  profile += "\nAge: " + std::to_string(age);
  profile += "\nLocation: " + city + ", " + country;
  std::string hobby_string = "\nHobbies:\n";

  for (std::string hobby : hobbies) {

    hobby_string += " - " + hobby + "\n";

  };

  profile += hobby_string;

  return profile + "\n";

};

void Profile::add_hobby(std::string new_hobby) {

  hobbies.push_back(new_hobby);

};
