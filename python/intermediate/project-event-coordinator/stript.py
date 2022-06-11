# You are starting up your own event coordination business and want to
# create a Python application using generators to help manage your events.
#
# This project will help you practice and further master the use of
# generators by managing and coordinating customer events for your business.

guests = {}

def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    g = yield name, age       ### Step 1 ###
    if g is not None:
      g = g.split(',')
      name = g[0]
      age = int(g[1])
      guests[name] = age
      yield name, age

guest_list = read_guestlist('guest_list.txt')

### Step 2 ###
for i in range(10):
  print(next(guest_list))

guest_list.send('Jane, 35')

for guest in guest_list:
  print(guest)

### Step 3 ###
# print(next(guest_list))
# print(next(guest_list))
# print(next(guest_list))
# print(next(guest_list))
# print(next(guest_list))

### Step 4 ###
guests_over_21 = (key for key, val in  guests.items() if int(val) > 21)
for guest in guests_over_21:
  print(guest)

### Step 5 ###
N_SEATS = 5
def chicken():
  food = "Chicken"
  table = 1
  for i in range(N_SEATS):
    seat = i + 1
    yield (f'Food: {food}', f'Table: {table}', f'Seat: {seat}')

def beef():
  food = "Beef"
  table = 2
  for i in range(N_SEATS):
    seat = i + 1
    yield (f'Food: {food}', f'Table: {table}', f'Seat: {seat}')

def fish():
  food = "Fish"
  table = 3
  for i in range(N_SEATS):
    seat = i + 1
    yield (f'Food: {food}', f'Table: {table}', f'Seat: {seat}')

chook = chicken()
for i in range(5):
  print(next(chook))


### Step 5 ###
def meal_assigner(guests, generator1, generator2, generator3):
  names = list(guests.keys())
  for i in range(5):
    yield (names[i], next(generator1))
  for i in range(5):
    i += 5
    yield (names[i], next(generator2))
  for i in range(5):
    i += 10
    yield (names[i], next(generator3))

meal_plans = meal_assigner(guests, chicken(), fish(), beef())

for i in meal_plans:
  print(i)
