from hurricane_data import names, months, years, max_sustained_winds, areas_affected, damages, deaths

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages

def update_damages(damages_list):
  new_list = []
  for item in damages_list:
    if item == "Damages not recorded":
      new_list.append(item)
    else:
      if "M" in item:
        new_str = item.replace("M", "")
        new_val = float(new_str) * 1000000
        new_list.append(new_val)
      elif "B" in item:
        new_str = item.replace("B", "")
        new_val = float(new_str) * 1000000000
        new_list.append(new_val)
      else:
        pass
  return new_list

updated_damages_list = update_damages(damages)
# for item in updated_damages_list:
#   print(item)

# 2
# Create a Table
def create_hurricanes_table(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  new_hurricanes_table = {}

  for i in range(len(names)):
    new_hurricaine_dict = {}
    new_hurricaine_dict["Name"] = names[i]
    new_hurricaine_dict["Month"] = months[i]
    new_hurricaine_dict["Year"] = years[i]
    new_hurricaine_dict["Max Sustained Wind"] = max_sustained_winds[i]
    new_hurricaine_dict["Areas Affected"] = areas_affected[i]
    new_hurricaine_dict["Damage"] = damages[i]
    new_hurricaine_dict["Deaths"] = deaths[i]
    new_hurricanes_table[names[i]] = new_hurricaine_dict

  return new_hurricanes_table

# Create and view the hurricanes dictionary
hurricanes_table = create_hurricanes_table(names, months, years, max_sustained_winds, areas_affected, updated_damages_list, deaths)

# print(hurricanes_table)
# for hurricane in hurricanes_table.values():
#   print(hurricane)

# 3
# Organizing by Year
def list_hurricanes_by_year(hurricanes_table_dict):
  hurrricanes_by_year = {}
  for hurricane, details in hurricanes_table_dict.items():
    current_year = details["Year"]
    if current_year in hurrricanes_by_year.keys():
      hurrricanes_by_year[current_year].append(details)
    else:
      hurrricanes_by_year[current_year] = [details]
  return hurrricanes_by_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = list_hurricanes_by_year(hurricanes_table)
# for year, cane in hurricanes_by_year.items():
#   print(year, cane)

# 4
# Counting Damaged Areas
def count_damaged_areas(areas_list):
  damaged_area_count = {}
  for areas in areas_list:
    for area in areas:
      if area in damaged_area_count.keys():
        damaged_area_count[area] += 1
      else:
        damaged_area_count[area] = 1

  return damaged_area_count

# create dictionary of areas to store the number of hurricanes involved in
affected_areas_count = count_damaged_areas(areas_affected)

# for area, count in affected_areas_count.items():
#   print(area, count)

# 5
# Calculating Maximum Hurricane Count
def max_hurricane_count(hurricane_count_dict):
  max_count = 0
  area_with_max_count = ""
  for area, count in hurricane_count_dict.items():
    current_count = count
    current_area = area
    if current_count > max_count:
      max_count = current_count
      area_with_max_count = current_area
  return area_with_max_count, max_count

# print("Area most affected: ")
# print(max_hurricane_count(affected_areas_count))

# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane
def highest_mortality_count(hurricane_dict):
  max_mortality = 0
  max_mortality_cane = ""
  for hurricane_details in hurricane_dict.values():
    currnet_hurricane_name = hurricane_details["Name"]
    current_mortality_count = hurricane_details["Deaths"]
    if current_mortality_count > max_mortality:
      max_mortality = current_mortality_count
      max_mortality_cane = currnet_hurricane_name
  return max_mortality_cane, max_mortality

# find highest mortality hurricane and the number of deaths
highest_mortality_cane = highest_mortality_count(hurricanes_table)
print("Highest mortailty hurricane: ")
print(highest_mortality_cane)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def get_hurricane_mort_ratings(hurricane_dict):

  hurricanes_by_mortality_rating = {0:[],1:[],2:[],3:[],4:[],5:[]}

  for hurricane in hurricane_dict.values():

    hurricane_name = hurricane["Name"]
    death_count = hurricane["Deaths"]

    if death_count == 0:
      hurricanes_by_mortality_rating[0].append(hurricane_name)

    elif death_count > mortality_scale[0] and death_count <= mortality_scale[1]:
      hurricanes_by_mortality_rating[1].append(hurricane_name)

    elif death_count > mortality_scale[1] and death_count <= mortality_scale[2]:
      hurricanes_by_mortality_rating[2].append(hurricane_name)

    elif death_count > mortality_scale[2] and death_count <= mortality_scale[3]:
      hurricanes_by_mortality_rating[3].append(hurricane_name)

    elif death_count > mortality_scale[3] and death_count <= mortality_scale[4]:
      hurricanes_by_mortality_rating[4].append(hurricane_name)

    elif death_count > 10000:
      hurricanes_by_mortality_rating[5].append(hurricane_name)

    else:
      pass

  return hurricanes_by_mortality_rating


# categorize hurricanes in new dictionary with mortality severity as key
# hurricanes_by_mortality_rating = get_hurricane_mort_ratings(hurricanes_table)
# print(hurricanes_by_mortality_rating)

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def find_greatest_damage_and_cost(hurricane_dict):
  max_damage = 0
  hurricane_max_damage = ""
  for hurricane in hurricane_dict.values():
    current_hurricane_name = hurricane["Name"]
    current_damages = hurricane["Damage"]
    try:
      if current_damages > max_damage:
        max_damage = current_damages
        hurricane_max_damage = current_hurricane_name
    except:
      pass
  return hurricane_max_damage, max_damage

hurricane_with_most_damage = find_greatest_damage_and_cost(hurricanes_table)
print("Hurricane with highest damages:")
print(hurricane_with_most_damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
def get_hurricane_damage_ratings(hurricane_dict):

  hurricanes_by_damage_rating = {0:[],1:[],2:[],3:[],4:[],5:[]}

  for hurricane in hurricane_dict.values():

    hurricane_name = hurricane["Name"]
    damages = hurricane["Damage"]

    try:
      if damages == 0:
        hurricanes_by_damage_rating[0].append(hurricane_name)

      elif damages > damage_scale[0] and damages <= damage_scale[1]:
        hurricanes_by_damage_rating[1].append(hurricane_name)

      elif damages > damage_scale[1] and damages <= damage_scale[2]:
        hurricanes_by_damage_rating[2].append(hurricane_name)

      elif damages > damage_scale[2] and damages <= damage_scale[3]:
        hurricanes_by_damage_rating[3].append(hurricane_name)

      elif damages > damage_scale[3] and damages <= damage_scale[4]:
        hurricanes_by_damage_rating[4].append(hurricane_name)

      elif damages > 50000000000:
        hurricanes_by_damage_rating[5].append(hurricane_name)

      else:
        pass

    except:
      pass

  return hurricanes_by_damage_rating

hurricanes_by_damage_rating = get_hurricane_damage_ratings(hurricanes_table)
print(hurricanes_by_damage_rating)
