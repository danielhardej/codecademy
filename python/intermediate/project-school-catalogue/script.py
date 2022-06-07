# an excersize to put your knowledge of classes to the test by creating a digital school catalog for
# the City Department of Education. The Department of Education wants the catalog to hold quick reference
# material for each school in the city.

class School:

  def __init__(self, name, level, numberOfStudents):
    self.level = level
    self.name = name
    self.numberOfStudents = numberOfStudents

  def getName(self):
    return self.name

  def getLevel(self):
    return self.level

  def getNumberOfStudents(self):
    return self.numberOfStudents

  def setNumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    statement = "A {} school named {} with {} students. ".format(self.level, self.name, self.numberOfStudents)
    return statement

# test:
# mySchool = School("Codecademy", "high", 100)
# print(mySchool.getName())
# print(mySchool.getLevel())
# mySchool.setNumberOfStudents(200)
# print(mySchool.getNumberOfStudents())
# print(mySchool.__repr__())

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getPickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup policy is {pickupPolicy}.".format(pickupPolicy = self.pickupPolicy)


# test PrimarySchool class
# ps = PrimarySchool("Codecademy", 300, "Pickup Allowed")
# print(ps.getName())
# print(ps.getLevel())
# print(ps)

# ps.setNumberOfStudents(200)

# print("Pickup policy: " + ps.getPickupPolicy())
# print(ps)


class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
    teams = self.sportsTeams
    teams_as_str = ""
    for team in teams:
      teams_as_str += ' ' + team + ','
    return "Sports teams: " + teams_as_str[:-1] + '.'   ## replace the final comma with a fullstop to make the returned string look tidy

  def __repr__(self):
    parentRepr = super().__repr__()
    teams = self.sportsTeams
    teams_as_str = ""
    for team in teams:
      teams_as_str += ' ' + team + ','
    return parentRepr + "The sports teams are: " + teams_as_str[:-1] + '.'    ## replace the final comma with a fullstop to make the returned string look tidy

# test the high school class
teams_list = ["Football", "Ice Hockey", "Rugby", "Tennis", "Rowing", "Track"]
hs = HighSchool("Codecademy", 300, teams_list);

print(hs.getName())
print(hs.getLevel())
print(hs)

print(hs.getSportsTeams())
hs.setNumberOfStudents(200)
print(hs)
