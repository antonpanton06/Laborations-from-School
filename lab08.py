weeks = []

def add_week():
    records = []

    for day in range(1, 8):
        # Read and validate three participation values and store the day's data
        
        morning = int(input(f"Day {day} morning: "))
        afternoon = int(input(f"Day {day} afternoon: "))
        evening = int(input(f"Day {day} evening: "))
        
        if morning < 0 or afternoon < 0 or evening < 0:
            print("Number of participants has to be a positive integer or zero.")
            break
        

        record = [morning, afternoon, evening]
        records.append(record)
    weeks.append(records)
    

def show_summaries():
    for week_number, records in enumerate(weeks, 1):
        # Calculate the average, find the highest-participation day and print the summary
        total = 0 
        highest = -1
        highest_day = 0 

        for day_number, record in enumerate(records, 1):
            day_total = sum(record)
            total += day_total

            if day_total > highest:
                highest = day_total
                highest_day = day_number

        average = total / (len(records) * 3)

        print(f"Week {week_number}")
        print(f"Average participation: {average:.2f}")
        print(f"Highest participation: Day: {highest_day} ({highest})")



def main():
    while True:
        print("\nGATHERGRID PARTICIPATION TRACKER")
        print("1. Add a week")
        print("2. Show weekly summaries")
        print("3. Exit")
        choice = int(input("Choice: "))
        # Handle the choice
        if choice > 3 or choice < 1:
            print("Invalid choice, choose between options 1-3.")
        elif choice == 1:
            add_week()
        elif choice == 2:
            show_summaries()
        elif choice == 3:
            break


if __name__ == "__main__":
    main()