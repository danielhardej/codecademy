from datetime import date   # import datetime for setting attendance

class Student:

  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

  def get_grades(self):
    grades_list = []
    for grade in self.grades:
      grades_list.append(grade.score)
    return grades_list

  def get_average(self):
    sum_grades = 0
    num_grades = 0
    for grade in self.grades:
      sum_grades += grade.score
      num_grades += 1
    return sum_grades / num_grades

  def set_attendance(self, attended):
    today = date.today()
    #print(today)
    if isinstance(attended, bool):
      self.attendance[today] = attended
    else:
      print("Not a valid entry.")


class Grade:

  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self):
    return self.score > self.minimum_passing


### Test the classes and methods in main() ###

def main():

  roger = Student("Roger van der Weyden", 10)
  sandro = Student("Sandro Botticelli", 12)
  pieter = Student("Pieter Bruegel the Elder", 8)

  pieter.add_grade(Grade(100))
  pieter.add_grade(Grade(72))
  pieter.add_grade(Grade(80))
  pieter.add_grade(Grade(100))

  print("Pieters grades: {}".format(pieter.get_grades()))

  for grade in pieter.grades:
    print(grade.is_passing())

  print("Pieters average grade: {}".format(pieter.get_average()))

  pieter.set_attendance(True)
  sandro.set_attendance(True)
  roger.set_attendance(False)
  pieter.set_attendance("poop")
  print(pieter.attendance)

# Using the special variable
# __name__
if __name__=="__main__":
    main()
