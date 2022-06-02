/*
Scissors cuts paper.
Paper covers rock.
Rock crushes lizard.
Lizard poisons Spock.
Spock smashes scissors.
Scissors decapitates lizard.
Lizard eats paper.
Paper disproves Spock.
Spock vaporizes rock.
Rock crushes scissors.
*/

#include <iostream>
#include <stdlib.h>

int main() {

  // Live long and prosper
  srand (time(NULL));
  int computer = rand() % 3 + 1;
  int user = 0;
  std::cout << "===============================\n";
  std::cout << "Let's play rock paper scissors!\n";
  std::cout << "===============================\n";
  std::cout << "1) ✊\n";
  std::cout << "2) ✋\n";
  std::cout << "3) ✌️\n";
  std::cout << "shoot! ";

  std::cin >> user;

  // if user picks rock
  if (user == 1) {
    if (computer == 1) {
      std::cout << "Draw.\n";
    } else if (computer == 2) {
       std::cout << "Computer wins. You lose.\n";
    } else if (computer == 3) {
      std::cout << "You win! Computer loses.\n";
    } else {
      // nothing
    }
  // if user picks paper
  } else if (user == 2) {
    if (computer == 1) {
      std::cout << "You win! Computer loses.\n";
    } else if (computer == 2) {
       std::cout << "Draw.\n";
    } else if (computer == 3) {
      std::cout << "Computer wins. You lose.\n";
    } else {
      // nothing
    }
  // if user pick scissors
  } else if (user == 3) {
    if (computer == 1) {
      std::cout << "Computer wins. You lose.\n";
    } else if (computer == 2) {
      std::cout << "You win! Computer loses.\n";
    } else if (computer == 3) {
      std::cout << "Draw.\n";
    } else {
      // nothing
    }
  } else {
    std::cout << "Whoops! Something went wrong!\n";
  }

  std::cout << "\n\n";
}
