# Multiple Tables in Pandas - Quiz

#### Question 1: A veterinarian’s office stores all of their data on pets and their owners in two dataframes: pets and owners. The owners dataframe has the columns id, first_name, last_name and address. The pets dataframe has the columns id, name, owner_id, and type. If the office wanted to combine the two dataframes into one dataframe called pets_owners, what following code could work?

- [ ] `pets_owners = pd.merge(pets, owners)`   
- [ ] `pets_owners = pd.merge(pets.rename(columns = {'owner_id':'id'}), owners)`
- [ ] `pets_owners = pd.merge(pets, owners, how = 'inner')`
- [x] `pets_owners = pd.merge(pets, owners.rename(columns = {'id':'owner_id'}))`

#### Question 2: Which of the following best describes an outer merge?

- [ ] A merge where all rows from the second Dataframe are included, but only matching rows from the first Dataframe.
- [ ] A merge where only matching rows are included.
- [x] A merge where all rows are included, whether they match or not.
- [ ] A merge where all rows from the first Dataframe are included, but only matching rows from the second Dataframe.

#### Question 3: Consider the following two Dataframes vets and appointments that store the appointment and vet data for a veterinarian’s office. Notice that some vets do not have any appointments scheduled, and some appointments do not yet have a vet assigned. If we wanted to combine the DataFrames into scheduled_appointments and only show the appointments that have had vets assigned to them, what code could we use?

- [ ] `scheduled_appointments = pd.merge(vets.rename(columns = {'id':'doctor-id'}), appointments, how = 'right')`
- [ ] `scheduled_appointments = pd.merge(vets.rename(columns = {'id':'doctor-id'}), appointments, how = 'left')`
- [x] `scheduled_appointments = pd.merge(vets.rename(columns = {'id':'doctor-id'}), appointments, how = 'inner')`
- [ ] `scheduled_appointments = pd.merge(vets.rename(columns = {'id':'doctor-id'}), appointments, how = 'outer')`

#### Question 4: Which of the following best describes an inner merge?

- [ ] A merge where all rows from the second Dataframe are included, but only matching rows from the first Dataframe.
- [x] A merge where only matching rows are included.
- [ ] A merge where all rows from the first Dataframe are included, but only matching rows from the second Dataframe.
- [ ] A merge where all rows are included, whether they match or not.

#### Question 5: A veterinarians office is run by two vets, Greg and Susan, and stores each of their appointment data in separate DataFrames, called greg_appointments and susan_appointments respectively. These DataFrames have the same columns. If the vet office wanted to combine the two DataFrames into a single DataFrame called appointments_all which of the following commands would they use?

- [ ] `appointments_all = pd.merge(greg_appointments, susan_appointments)`
- [ ] `appointments_all = pd.merge(greg_appointments, susan_appointments, how = 'outer')`
- [x] `appointments_all = pd.concat([greg_appointments, susan_appointments])`
- [ ] `appointments_all = pd.merge(greg_appointments, susan_appointments, how = 'concatenation')`

#### Question 6: What is the correct syntax for performing an outer merge on two Dataframes: df_one and df_two?

- [x] ```merged_df = pd.merge(df_one, df_two, how = 'outer')```
- [ ] ```merged_df = pd.merge( df_one, df_two, type = 'outer')```
- [ ] ```merged_df = pd.outermerge(df_one, df_two)```
- [ ] ```merged_df = pd.merge.outer(df_one, df_two)```

#### Question 7: Which of the following best describes a left merge?

- [ ] A merge where all rows from the second Dataframe are included, but only matching rows from the first Dataframe.
- [x] A merge where all rows from the first Dataframe are included, but only matching rows from the second Dataframe.
- [ ] A merge where only matching rows are included.
- [ ] A merge where all rows are included, whether they match or not.