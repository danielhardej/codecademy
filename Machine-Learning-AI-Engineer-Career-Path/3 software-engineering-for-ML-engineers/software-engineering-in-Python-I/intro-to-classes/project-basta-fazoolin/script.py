import datetime
from menus import brunch_items, earlybird_items, dinner_items, kids_items

class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"{self.name} menu available from {self.start_time}.00 to {self.end_time}.00"

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

class Franchise:

    def __init__(self, address, menus):
      self.address = address
      self.menus = menus

    def __repr__(self):
      return "Basta Fazoolin’ with My Heart" + self.address

    def available_menus(self, time):
      available_menus = []
      for menu in self.menus:
        if (time >= menu.start_time) and (time < menu.end_time):
          available_menus.append(menu)
        else:
          pass
      return available_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises




brunch = Menu("Brunch", brunch_items, 11, 16)
earlybird = Menu("Earlybird", earlybird_items, 15, 18)
dinner = Menu("Dinner", dinner_items, 17, 23)
kids = Menu("Kids", kids_items, 11, 21)

def main():
  print(brunch)

  print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
  print(earlybird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
  # print(brunch_items['coffee'])

  flagship_store = Franchise("1232 West End Road", [brunch, earlybird, dinner, kids])
  new_installment = Franchise("12 East Mulberry Street", [brunch, earlybird, dinner, kids])

  print(flagship_store.available_menus(12))
  print(new_installment.available_menus(12))

  print(flagship_store.available_menus(17))
  print(new_installment.available_menus(17))

  arepas_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
  }
  arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

  first_biz = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
  new_biz = Business("Take a' Arepa", [arepas_place])

if __name__=="__main__":
    main()
