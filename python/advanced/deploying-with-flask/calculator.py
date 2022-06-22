# What we're learning: We will cover how to deploy an application in Python using Flask.
# We will learn about:
# The importance of deployment
# How to install Flask using Python Pip
# How to locally deploy a simple Python program using Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
  return "Welcome to the Codecademy Calculator!"

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

@app.route('/division')
def division():
  return "Now dividing " + str(num1) + " and " + str(num2) + "! The result is: {result}".format(result=str(num1/num2))

@app.route('/multiplication')
def multiplication():
  return "Now multiplying " + str(num1) + " and " + str(num2) + "! The result is: {result}".format(result=str(num1*num2))

app.run()

# run the command 'python3 calculator.py' in terminal
#
# To run division:
# go to http://127.0.0.1:5000/division in your browser
#
# To run multiplication:
# go to http://127.0.0.1:5000/multiplication in your browser
