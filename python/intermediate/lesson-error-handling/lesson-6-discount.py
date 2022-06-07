# we have an imaginary scenario where a store called Instrument World
# has a program that allows the user to apply a discount to an instrument price.
#
# in this lesson we practice handling multiple exceptions
# we use NameError and KeyError to trigger exception handlers
# we also use Exception




instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Banjo'
discount = 20

# Write your code below:
try:
  display_discounted_price(instrument, discount)
except KeyError:
  print('An invalid instrument was entered!')
except TypeError:
  print('Discount percentage must be a number!')
except Exception:
  print('Hit an exception other than KeyError or TypeError!')
