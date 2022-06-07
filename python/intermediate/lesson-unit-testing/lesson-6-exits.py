# At Small Air World, every plane seat has a monitor which displays 
# the nearest emergency exit.
#
# This monitor relies on a function called get_nearest_exit(), which takes a
# row number and then returns an exit location depending on where the row is.
# Let’s make sure our function is working properly by creating a unit test.

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  elif row_number > 30:
    location = 'back'
  else:
    location = 'back'
  return location

# Write your code below:
def test_row_1():
  assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'

def test_row_20():
  assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'

def test_row_40():
  assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back!'

test_row_1()
test_row_20()
test_row_40()
