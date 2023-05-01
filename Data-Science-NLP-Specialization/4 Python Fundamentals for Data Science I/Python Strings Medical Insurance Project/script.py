from medical_data import medical_data

# Add your code here
print(medical_data)

updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

num_records = 0
for char in updated_medical_data:
  if char == "$":
    num_records += 1
print("There are {} medical records in the data.".format(num_records))

medical_data_split = updated_medical_data.split(";")
# print(medical_data_split)
medical_records = [record.split(",") for record in medical_data_split]
# print(medical_records)

medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

print(medical_records_clean)

for record in medical_records_clean:
  print(record[0].upper())

names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0].upper())
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

print(insurance_costs)

total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)
print("Average BMI: {}".format(average_bmi))

total_insurance_costs = 0
for cost in insurance_costs:
  total_insurance_costs += float(cost.strip("$"))

for record in medical_records_clean:
  print("{} is {} years old with a BMI of {} and an insurance cost of {}".format(record[0].split()[0], record[1], record[2], record[3]))
