#include <iostream>

int main() {

  // Brain explodes here:
  for (int i=1; i<=100; i++)

  if (i%3!=0 && i%5!=0) {
    std::cout << i << '\n';
  } else if (i%3==0 && i%5==0) {
    std::cout << "Fizz Buzz\n";
  } else if (i%3==0) {
    std::cout << "Fizz\n";
  } else if (i%5==0) {
    std::cout << "Buzz\n";
  } else {
    // something
  }

}
