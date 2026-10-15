"""Your main task: Create a Measurement Report program
DETAILS: Create a program that reads
measurements from a text file, allows the user
to add and update measurements, displays a
summary, and saves the changes and report to
files.
MAIN MENU:
YOUR PROGRAM MUST:
• Load measurements from external source file. Store them in a list.
• Display a menu: Load data, Show measurements, Add a measurement, Update a
measurement, Show summary, Save changes, Save report, Exit.
• Use a while loop to keep the menu running.
• Allow users to add and update measurements.
• Save changes by replacing the source file's contents.
• Skip blank lines and NA (case-insensitive), counting them as skipped.
• Report and skip lines that cannot be converted to numbers.
• Display the valid count, average, and skipped count. Show N/A if no valid
measurements exist.
• Save the summary to report.txt without overwriting an existing report.
• Handle FileNotFoundError when loading and OSError when saving files.
• Use functions, loops, conditionals, pathlib.Path, with, and UTF-8 encoding.
• Use try/except for errors and f-strings for formatted output."""

from pathlib import Path

def load_data(path):
    # Read measurements from file
    values = []
    skipped = 0
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            text = line.strip()

            if text == "" or text.upper() == "NA":
                skipped += 1
                continue

            try:
                values.append(float(text))
            except ValueError:
                print(f"Line {line_number}: invalid measurment '{text}'")
                skipped += 1
        return values, skipped


# Add your own functions to manipulate the measurements
def show_data(values):
    if not values:
        print("No measurements to show.")
        return
    for number, value in enumerate(values, start=1):
        print(f"{number}. {value}")

def add_values(values):
        try:
            value = float(input("Add measurement: "))
            
        except ValueError: 
            print("Value has to be a number!")
            return
        
        values.append(value)
        print(f"Measurement {value} added")

def update_values(values):
    show_data(values)

    try:
        number = int(input("Which measurement number do you want to update?\n"))
    except ValueError:
        print("Enter a integer.")
        return
    if number < 1 or number > len(values):
        print(f"Choose a number between 1 and{len(values)}.")
        return

    try:
        new_value = float(input("Enter measurement: "))
    except ValueError:
        print("Measurement has to be number!")
        return

    values[number - 1] = new_value
    print(f"Measurement {number} updated to {new_value}.")

def show_summary(values, skipped):
    print(f"Valid count: {len(values)}")

    if values:
        average = sum(values) / len(values)
        print(f"Average: {average:.2f}")
    else:
        print("Average: N/A")

    print(f"Skipped count: {skipped}")


def save_data(path, values):
    # Save updated measurements
    try:
        with open(path, "w", encoding="utf-8") as file:
            for value in values:
                file.write(f"{value}\n")
    except OSError as error:
        print(f"Could not save measurement(s): {error}")
    else:
        print("Measurement(s) saved!")


def save_report(path, values, skipped):
    # Save summary to report.txt
    try:
        with open(path, "x", encoding="utf-8") as file:
            file.write(f"Valid count: {len(values)}\n")

            if values:
                if values:
                    average = sum(values) / len(values)
                    file.write(f"Average: {average:.2f}\n")
                else:
                    file.write("Average: N/A\n")
                
                file.write(f"Skipped count: {skipped}\n")
    except FileExistsError:
        print("Report already exists. It was not overwritten.")
    except OSError as error:
        print(f"Could not save report: {error}")
    else:
        print("Report saved")

def main():
    # Display and handle the menu
    path = Path(__file__).resolve().parent / "data.txt"
    values = []
    skipped = 0
    while True:
        print("\nMEASUREMENT REPORT")
        print("1. Load data")
        print("2. Show measurments")
        print("3. Add a measurment")
        print("4. Update a measurment")
        print("5. Show summary")
        print("6. Save changes")
        print("7. Save report")
        print("8. Exit\n")

        try: 
            choice = int(input("Choice: "))

            if choice == 1:
                try:
                    values, skipped = load_data(path)
                    print(f"Loaded {len(values)} measurements.")
                except FileNotFoundError: 
                    print(f"File not found: {path}")

            elif choice == 2:
                show_data(values)

            elif choice == 3:
                add_values(values)
                
            elif choice == 4:
                update_values(values)

            elif choice == 5:
                show_summary(values, skipped)

            elif choice == 6:
                save_data(path, values)

            elif choice == 7:
                report_path = path.parent / "report.txt"
                save_report(report_path, values, skipped)

            elif choice == 8:
                break
            
            else:
                print("Input between 1-8!!\n")
        except ValueError:
            print("Input has to be integer between 1-8!!\n")
            continue
            


if __name__ == "__main__":
    main()
