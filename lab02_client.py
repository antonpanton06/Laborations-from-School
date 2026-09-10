print(type(5+2))
print(type(5/2))
print(type(5//2))
print(type("5"))

print(int("12") + 3)

price = 80 
discount = 0.25
final_price = price * (1 - discount)
print(final_price)
#Now this is for the main task, things above are just for testing.
#CampusNest needs my help.
total_minutes = 175
#t_m stores the total minutes of the booking
hours = total_minutes // 60
#"hours" stores the number of whole hours in the booking
remaining_minutes = total_minutes % 60
#remaining_minutes stores the number of minutes left after accounting for whole hours
booking_name = "Hilma Svensson"
print(f"You have booked a group room for {hours} hours and {remaining_minutes} min!")
print(f"Booking name: {booking_name}")

#More practice exercises
#A.Distance
distance_meters = 1750
distance_kilometers = distance_meters / 1000
print(f"{distance_meters} meters")
print(f"Distance in kilometers: {distance_kilometers} km")

#B. Temperature
temperature_c = 20
temperature_f = (temperature_c * 9/5 + 32)
print(f"{temperature_c} degrees celsius")
print(f"Temperature in fahrenheit: {temperature_f} degrees fahrenheit")

#C. Discount
price1 = 200
discount1 = 0.15
final_price1 = price1 * (1 - discount1)
print(f"Original price: {price1} kr")
print(f"Discount: {discount1 * 100}%")
print(f"Discounted price: {final_price1} kr")