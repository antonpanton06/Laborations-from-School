import csv
import json

def calculate_totals_csv(input_path, output_path):
    # Reuse or implement the CSV solution
    with open(input_path, "r", encoding="utf-8", newline="") as file:
        reader =csv.DictReader(file)

        with open(output_path, "w", encoding="utf-8", newline="") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=["id", "name", "total"])
            writer.writeheader()


            for student in reader:
                total = (int(student["math"])
                    + int(student["english"])
                    + int(student["science"]))

                writer.writerow({"id": student["id"],
                    "name": student["name"],
                    "total": total})


def calculate_totals_json(input_path, output_path):
    # Reuse or implement the JSON solution
    with open(input_path, "r", encoding="utf-8") as file:
        students = json.load(file)

    results = []

    for student in students:
        total = (
            student["math"]
            + student["english"]
            + student["science"]
        )

        results.append({"id":student["id"], 
            "name": student["name"],
            "total": total})

    with open(output_path, "w", encoding="utf-8") as output_file:
        json.dump(results, output_file, indent=4)