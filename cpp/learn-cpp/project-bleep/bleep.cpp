#include <iostream>
#include <string>
#include "functions.cpp"

int main() {

  std::string word = "broccoli";
  std::string text = "I sometimes eat broccoli. There are three interesting things about broccoli. Number One. Nobody knows how to spell it. Number Two. No matter how long you boil it, it's always cold by the time it reaches your plate. Number Three. It's green. #broccoli";

  bleep(word, text);

  for (int i = 0; i < text.size(); i++) {

    std::cout << text[i];

  }

  std::cout << "\n";

}
