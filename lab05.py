name = input("Student name:")

total = 0
days_above_target = 0 

for day in range(1, 8):
    hours = int(input(f"Day: {day}: "))
    total += hours 

    if hours > 2:
        days_above_target += 1

average = total/7



if average < 1:
    performance = "Low"
elif average == 1 or total/7 == 2:
    performance = "Moderate"
elif average > 2:
    performance = "High"
elif average < 0:
    performance = None


#PROGRAM
print("STUDYSPARK WEEK REVIEW")
print()
print(f"{'Student:':20} {name.upper()}")
print(f"{'Total:':20} {total} hours")
print(f"{'Average:':20} {total/7:.2f} hours")
print(f"{'Days above target:':20} {days_above_target}")
print(f"{'Performance:':20} {performance}")