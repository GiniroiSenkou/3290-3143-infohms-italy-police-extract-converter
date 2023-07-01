data = "1629/06/2023 4Rossi Mario 228/02/1940 100001100000231PASOR444333111 1000000231"

fields = data.split(" ")

intended_purpose = fields[0][:2]  # 2-digit intended purpose
date = fields[0][2:]  # Date without the first 2 digits
last_name = fields[1][1:]  # Rossi (remove the leading digit)
field_digit_2 = fields[2][0]  # 2
first_name = fields[2][1:]  # Mario
dob = fields[3][1:]  # 28/02/1940 (remove the leading digit)
passport_category = fields[4][15:19]  # PASOR (extract the passport category)
passport_number = fields[4][19:]  # 444333111 (extract the passport number)

print("Intended Purpose:", intended_purpose)
print("Date:", date)
print("Last Name:", last_name)
print("Field Digit 2:", field_digit_2)
print("First Name:", first_name)
print("Date of Birth:", dob)
print("Passport Category:", passport_category)
print("Passport Number:", passport_number)
