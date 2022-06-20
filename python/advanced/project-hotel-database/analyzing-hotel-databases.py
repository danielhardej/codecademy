# Import module
import sqlite3

# Task 1: Create connection object
con = sqlite3.connect("hotel_booking.db")

# Task 2: Create cursor object
cur = con.cursor()

# Task 3: View first row of booking_summary
one = cur.execute("SELECT * FROM booking_summary").fetchone()
print(one)

# Task 4: View first ten rows of booking_summary
many = cur.execute("SELECT * FROM booking_summary").fetchmany(5)
for line in many:
  print(line)

# Task 5: Create object bra and print first 5 rows to view data
bra = cur.execute("SELECT * FROM booking_summary WHERE country='BRA'").fetchall()

# Task 6: Create new table called bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
                   num INTEGER,
                   hotel TEXT,
                   is_cancelled INTEGER,
                   lead_time INTEGER,
                   arrival_date_year INTEGER,
                   arrival_date_month TEXT,
                   arrival_date_day_of_month INTEGER,
                   adults INTEGER,
                   children INTEGER,
                   country TEXT,
                   adr REAL,
                   special_requests INTEGER)''')

# Task 7: Insert the object bra into the table bra_customers
cur.executemany('''INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', bra)

# Task 8: View the first 10 rows of bra_customers
bra_ten = cur.execute("SELECT * FROM bra_customers").fetchmany(10)
for line in bra_ten:
  print(line)

# Task 9: Retrieve lead_time rows where the bookings were canceled
lead_time_can = cur.execute("SELECT lead_time FROM bra_customers WHERE is_cancelled=1").fetchall()

# Task 10: Find average lead time for those who canceled and print results
lead_time_sum = 0
booking_count = 0
for lead_time in lead_time_can:
  lead_time_sum += lead_time[0]
  booking_count += 1
avg_lead_time_can = lead_time_sum/booking_count
print(avg_lead_time_can)

# Task 11: Retrieve lead_time rows where the bookings were not canceled
lead_time_not_can = cur.execute("SELECT lead_time FROM bra_customers WHERE is_cancelled=0").fetchall()

# Task 12: Find average lead time for those who did not cancel and print results
lead_time_not_can_sum = 0
booking_count_not_can = 0
for lead_time in lead_time_not_can:
  lead_time_not_can_sum += lead_time[0]
  booking_count_not_can += 1
avg_lead_time_not_can = lead_time_not_can_sum/booking_count_not_can
print(avg_lead_time_not_can)

# Task 13: Retrieve special_requests rows where the bookings were canceled
bra_customers_special_requests_can = cur.execute("SELECT special_requests FROM bra_customers WHERE is_cancelled=1").fetchall()

# Task 14: Find total speacial requests for those who canceled and print results
total_spec_requests_can = 0
for sr in bra_customers_special_requests_can:
   total_spec_requests_can += sr[0]
print(total_spec_requests_can)

# Task 15: Retrieve special_requests rows where the bookings were not canceled
bra_customers_special_requests_not_can = cur.execute("SELECT special_requests FROM bra_customers WHERE is_cancelled=0").fetchall()

# Task 16: Find total speacial requests for those who did not cancel and print results
total_spec_requests_not_can = 0
for sr in bra_customers_special_requests_not_can:
   total_spec_requests_not_can += sr[0]
print(total_spec_requests_not_can)

# Task 17: Commit changes and close the connection
con.commit()
con.close()
