#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main() {

  // Whale, whale, whale.
  // What have we got here?
  std::string phrase = "a whale of a deal!";
  //std::cout << "Enter a phrase: ";
  //std::cin >> phrase;
  //std::cout << "\n";

  std::vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
  std::vector<char> result;

  for (int i=0; i<phrase.length(); i++) {
    for (int j=0; j<vowels.size(); j++) {
      if (phrase[i]==vowels[j]) {
        result.push_back(phrase[i]);
        if (phrase[i] == 'u' || phrase[i] == 'e') {
          result.push_back(phrase[i]);
        }
      }
    }
  }

  std::cout << "Result:\n";
  for (int k = 0; k < result.size(); k++) { std::cout << result[k]; }
  std::cout << "\n\n";

}
