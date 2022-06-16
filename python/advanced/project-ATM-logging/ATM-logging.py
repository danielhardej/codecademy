import random
import logging
import sys
from datetime import datetime

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("formatted.log")
logger.addHandler(file_handler)

formatter = logging.Formatter('%(asctime)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")

  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      if pin != 1234:
        logger.warning("Error! Invalid pin. Try again.")
      else:
        return None

  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      if amount < 0:
        logger.warning("Warning! You entered a negative number to deposit.")
      self.balance += amount
      logger.info("Amount Deposited: ${amount}".format(amount=amount))
      logger.info("Transaction Info:")
      logger.info("Status: Successful")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.warning("Error! You entered a non-number value to deposit.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))

  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        logger.info("You withdrew: ${amount}".format( amount=amount))
        logger.info("Transaction Info:")
        logger.info("Status: Successful")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      else:
        logger.warning("Error! Insufficient balance to complete withdraw.")
        logger.info("Transaction Info:")
        logger.info("Status: Failed")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.warning("Error! You entered a non-number value to withdraw.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))

  def display(self):
    logger.info("Available Balance = ${balance}".format(balance=self.balance))

acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()
