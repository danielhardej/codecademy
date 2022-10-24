#include <iostream>

int main() {

  double pesos, reais, soles, dollars;
  double conversion_rate1, conversion_rate2, conversion_rate3;

  std::cout << "Enter number of Colombian Pesos: \n";
  std::cin >> pesos;
  std::cout << "Enter number of Brazilian Reais: \n";
  std::cin >> reais;
  std::cout << "Enter number of Peruvian Soles: \n";
  std::cin >> soles;

  //USD-pesos = 3907.86
  conversion_rate1 = 3907.86;
  //USD-reais = 4.74
  conversion_rate2 = 4.74;
  //USD-soles = 3.67
  conversion_rate3 = 3.67;

  //calculate dollars
  dollars = (pesos/conversion_rate1) + (reais/conversion_rate2) + (soles/conversion_rate3);

  std::cout << "US Dollars = $" << dollars << "\n";
}
