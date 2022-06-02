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
  std::string user_choice;
  std::string computer_choice;

  std::cout << "================================================\n";
  std::cout << "Let's play Rock, Paper, Scissors, Lizard, Spock!\n";
  std::cout << "================================================\n";
  std::cout << "1) ✊\n";
  std::cout << "2) ✋\n";
  std::cout << "3) ✌️\n";
  std::cout << "4) 🦎\n";
  std::cout << "5) 🖖\n";
  std::cout << "shoot! ";
  std::cin >> user;

  switch (user) {
  case 1:
    user_choice = "Rock";
    break;
  case 2:
    user_choice = "Paper";
    break;
  case 3:
    user_choice = "Scissors";
    break;
  case 4:
    user_choice = "Lizard";
    break;
  case 5:
    user_choice = "Spock";
    break;
  default:
    std::cout << "Invalid choice\n";
    break;
  }

  switch (computer) {
  case 1:
    computer_choice = "Rock";
    break;
  case 2:
    computer_choice = "Paper";
    break;
  case 3:
    computer_choice = "Scissors";
    break;
  case 4:
    computer_choice = "Lizard";
    break;
  case 5:
    computer_choice = "Spock";
    break;
  default:
    std::cout << "Invalid choice\n";
    break;
  }

  std::cout << "You chose " << user_choice << ", the computer chose " << computer_choice << "\n";

  // if user picks rock
  if (user == 1) {
    if (computer == 1) {
      std::cout << "Draw.\n";
    } else if (computer == 2 || computer == 5) {
       std::cout << "Computer wins. You lose.\n";
    } else if (computer == 3 || computer==4) {
      std::cout << "You win! Computer loses.\n";
    } else {
      // nothing
    }
  // if user picks paper
  } else if (user == 2) {
    if (computer == 1 || computer == 5) {
      std::cout << "You win! Computer loses.\n";
    } else if (computer == 2) {
       std::cout << "Draw.\n";
    } else if (computer == 3 || computer == 4) {
      std::cout << "Computer wins. You lose.\n";
    } else {
      // nothing
    }
  // if user pick scissors
  } else if (user == 3) {
    if (computer == 1  || computer == 5) {
      std::cout << "Computer wins. You lose.\n";
    } else if (computer == 2 || computer == 4) {
      std::cout << "You win! Computer loses.\n";
    } else if (computer == 3) {
      std::cout << "Draw.\n";
    } else {
      // nothing
    }
  }
  // if user picks lizard
  else if (user == 4) {
    if (computer==1 || computer==3) {
      std::cout << "Computer wins. You lose.\n";
    } else if (computer==2 || computer==5) {
      std::cout << "You win! Computer loses.\n";
    } else if (computer == 4) {
      std::cout << "Draw.\n";
    } else {
      // nothing
    }
  }
  // if user picks spock
  else if (user == 5) {
    if (computer==2 || computer==4) {
      std::cout << "Computer wins. You lose.\n";
    } else if (computer==1 || computer==3) {
      std::cout << "You win! Computer loses.\n";
    } else if (computer==5) {
      std::cout << "Draw.\n";
    } else {
      // nothing
    }
  } else {
    std::cout << "Whoops! Something went wrong!\n";
  }

  std::cout << "\n\n";
}
