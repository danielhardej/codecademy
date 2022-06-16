import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("cashier.log")
logger.addHandler(file_handler)

formatter = logging.Formatter("[%(asctime)s] {%(levelname)s} %(name)s: - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

print("Welcome to Food in a Jiffy!")

food_options = {
  "H": {
    "name": "Hamburger",
    "price": 2.49
    },
  "C": {
    "name": "Cheeseburger",
    "price": 4.99
    },
  "F": {
    "name": "Fries",
    "price": 2.50
    },
  "D": {
    "name": "Drink",
    "price": 1.99
    },
  "E": {
    "name": "End Order",
    "price": 0.00
    }
}

def menu():
  for food in food_options:
    print("[{key}] {food_name}: ${food_price}".format(key = food, food_name = food_options[food]["name"], food_price = food_options[food]["price"]))

menu()
cost = 0

choice = str(input("\nSelect a letter corresponding to the menu choice to order: ")).upper()
if choice not in food_options:
  logger.log(logging.ERROR, f"Invalid choice entered: {choice}")

while choice != "E":
  for key in food_options:
    if choice == key:
      food = food_options[key]
      logger.log(logging.INFO, f"Choice {choice} successfully entered.")
      try:
        num = int(input("\nHow many of the " + food['name'] + " would the customer like to order? "))
        logger.log(logging.INFO, f"Quantity {num} successfully entered.")
      except ValueError:
        print("\nInvalid number entered. Using quantity of 1.")
        logger.log(logging.ERROR, f"Invalid quantity entered: {num}")
        num = 1
      food_price = round(food['price'] * num, 2)
      cost += food_price
      print("\n" + food['name'] + "\t ${food_price}".format(food_price = food_price))
      break


  # if match == 0:
  #   print("Invalid Choice, please select again.")
  choice = str(input("\nSelect a letter corresponding to the menu choice to order: ")).upper()

if choice == "E":
  print("\nThe total for the order is ${cost}".format(cost = round(cost, 2)))
  logger.log(logging.INFO, f"Order total {cost}.")
  money = float(input("\nEnter the amount paid by the customer:"))
  if money < cost:
    logger.log(logging.WARNING, f"Insufficient amout paid. Money received: {money}  Money expected: {cost}")
    money = float(input("\nThere is not enough money. Please re-enter the amount paid:"))
  print("The customer's change is ${change}".format(change = round(money - cost, 2)))
  logger.log(logging.INFO, f"Balance paid. Money received: {money}  Money expected: {cost}")
