import roster
import classroom_organizer
import itertools

student_roster_iterator = iter(roster.student_roster)

#print(next(student_roster_iterator))

co = classroom_organizer.ClassroomOrganizer()

# task 3
print("Roll call: ")
co.roll_call()
print()

# task 4
two_seat_combos = co.student_combinations_2_seats()
print("Two seat combinations: ")
for two_seat_combo in two_seat_combos:
  print(two_seat_combo)
print()

# task 5
math_students = co.get_students_with_subject("Math")
science_students = co.get_students_with_subject("Science")
math_science_students = itertools.chain(math_students, science_students)
math_student_combinations = list(itertools.combinations(math_science_students, 4))

print("Combinations of math & science students at tables of four: ")
for combo in list(itertools.combinations(math_student_combinations, 4)):
  print(combo)
