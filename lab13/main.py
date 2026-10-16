"""Your main task: Create a Student Score Report program
DETAILS: Develop a program that reads
student scores from CSV and JSON files,
calculates the total score for each student,
and saves the results in the corresponding
format. You will continue the work you started
during the warm-up by reusing your existing
function and implementing a function for the
other format. 
YOUR PROGRAM MUST:
• Reuse the function you implemented during the warm-up
and add a second function to support both CSV and JSON
files.
• Store both format-processing functions in a separate
helpers.py file and import them into main.py.
• Use os.listdir() to identify the files in the input folder and
select the appropriate function based on each file's
extension.
• Calculate the total score for each student and save the
results in the same format as the input file.
• Store the generated reports in an output folder, creating
the folder if it does not exist.
• Skip files with unsupported extensions. """

import os
from helpers import calculate_totals_csv, calculate_totals_json

def main():
    input_folder = "input"
    output_folder = "output"

    os.makedirs(output_folder, exist_ok=True)

    # Identify the file format
    for filename in os.listdir(input_folder):
    
        # Construct input and output paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Call the appropriate function  
        if filename.endswith(".csv"):
            calculate_totals_csv(input_path, output_path)

        elif filename.endswith(".json"):
            calculate_totals_json(input_path, output_path)
        

if __name__ == "__main__":
    main()