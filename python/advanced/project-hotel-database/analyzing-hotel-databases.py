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
print(many)

# Task 5: Create object bra and print first 5 rows to view data
bra = cur.execute("SELECT * FROM booking_summary WHERE country='BRA'").fetchmany(5)
for line in bra:
  print(line)

# Task 6: Create new table called bra_customers


# Task 7: Insert the object bra into the table bra_customers


# Task 8: View the first 10 rows of bra_customers


# Task 9: Retrieve lead_time rows where the bookings were canceled


# Task 10: Find average lead time for those who canceled and print results


# Task 11: Retrieve lead_time rows where the bookings were not canceled


# Task 12: Find average lead time for those who did not cancel and print results


# Task 13: Retrieve special_requests rows where the bookings were canceled


# Task 14: Find total speacial requests for those who canceled and print results


# Task 15: Retrieve special_requests rows where the bookings were not canceled


# Task 16: Find total speacial requests for those who did not cancel and print results


# Task 17: Commit changes and close the connection
