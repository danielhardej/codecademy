import roster
import itertools

# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(roster.student_roster)

  def __iter__(self):
    return self

  # def __next__(self):
  #   self.count += 1
  #   if self.count == len(roster.student_roster):
  #     raise StopIteration
  #   return self.count

  # task 3
  def roll_call(self):
    sorted_names_iterator = iter(self.sorted_names)
    while True:
      try:
        print(next(sorted_names_iterator))
      except StopIteration:
        break

  # task4
  def student_combinations_2_seats(self):
    student_combinations = list(itertools.combinations(self.sorted_names, 2))
    return student_combinations

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in roster.student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append(student['name'])
    return selected_students
