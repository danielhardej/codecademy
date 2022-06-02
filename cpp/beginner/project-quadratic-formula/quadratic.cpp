#include <iostream>
#include <cmath>

int main() {
  // Add your code below
  double a, b, c;
  double root1, root2;

  std::cout << "Welcome! This is a program to help you solve quadratic equations in the format ax^2 + bx + c = 0\n";
  std::cout << "Enter the coefficient a: ";
  std::cin >> a;
  std::cout << "Enter the coefficient b: ";
  std::cin >> b;
  std::cout << "Enter the coefficient c: ";
  std::cin >> c;

  root1 = (-b + std::sqrt((b*b) - (4*a*c) ) ) /(2*a);
  root2 = (-b - std::sqrt((b*b) - (4*a*c) ) ) / (2*a);

  std::cout << "  \n";
  std::cout << "The solutions to your quadratic equation are:\n";
  std::cout << root1 << " and " << root2 << "\n";
}
