# Northline Mobility needs your help.
# The task: Create a Python program that asks for the passenger's age andwhether they are a student, then determines their fare category and price.

age = input("Age: ")
student = input("Student? ")
company = "Northline Mobility"
# Process the values here
age = int(age)
# Determine the fare here
if age < 0 or age > 120:
    fare_category = "Invalid age"
    price = None
elif age < 18:
    fare_category = "Child"
    price = 15
elif age >= 18 and age <= 25 and student == "Yes" or student == "YES" or student == "yes":
    fare_category = "Student"
    price = 24
elif age >= 65:
    fare_category = "Senior"
    price = 20
else:
    fare_category = "Adult"
    price = 36
    
# Print the result here
print()
print()
print(f"Age: {age}")
print(f"Student? {student.upper()}")
print()
print()
print(company.upper())
print(f"Fare Category:   {fare_category}")
if price is not None:
    print(f"Age: {age:>14}")
if price is not None:
    print(f"Price: {price:>15.2f} SEK")

