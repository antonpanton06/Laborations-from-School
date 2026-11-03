import json
from helpers import extract_prices, calculate_statistics, statistics

"""Your main task: Create an Expense and Receipt Analyzer
DETAILS: Develop a program that reads
purchase data from a JSON file (provided on
the last slide), extracts prices in SEK from
receipt text using regular expressions,
calculates spending statistics, and saves a
summary report.
YOUR PROGRAM MUST:
• Load the provided purchases.json file using the json module.
• Use a regular expression and re.findall() to extract SEK amounts
with exactly two decimal digits, accepting either . or , as the decimal
separator. Ignore numbers that are not explicitly followed by SEK,
including prices in other currencies.
• Convert extracted amounts to numbers and calculate the total and
average for each receipt.
• Calculate the total and average across all extracted amounts.
• Save the results to report.txt, including the receipt ID, shop, extracted
amounts, total, and average.
• Organize the program into main.py and helpers.py, using functions
and imports.
• Handle a missing input file and the case where no valid amounts are
found.
• Use loops, conditionals, and file handling to process the data and
produce the report. """

def main():
    data = load_json("purchases.json")
    if data != None:
        receipt_results, overall_total, overall_average, number_of_amounts = statistics(data)

        print_receipt("report.txt", receipt_results, overall_total, overall_average, number_of_amounts)
 
#Load data, process receipts,
def load_json(text):
    try:
        with open(text,"r",encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as error:
        print(error)

# and save the report
def print_receipt(path, receipt_results, overall_total, overall_average, number_of_amounts):
    
    try:
        with open(path, "w", encoding="utf-8") as output_receipt:
            for receipt in receipt_results:
                amounts = ", " .join([f"{price:.2f} SEK" for price in receipt['prices']])

                output_receipt.write(f"Receipt ID: {receipt['id']}\n")
                output_receipt.write(f"Shop: {receipt['shop']}\n")
                output_receipt.write(f"Extracted amounts: {amounts}\n")
                output_receipt.write(f"Total: {receipt['total']:.2f} SEK\n")
                output_receipt.write(f"Average: {receipt['average']:.2f} SEK\n")
                output_receipt.write("\n")

            output_receipt.write("OVERALL SUMMARY\n")
            output_receipt.write(f"Number of amounts: {number_of_amounts}\n")
            output_receipt.write(f"Total: {overall_total:.2f} SEK\n")
            output_receipt.write(f"Average: {overall_average:.2f} SEK\n")
    except FileNotFoundError as error:
        print(error)


if __name__ == "__main__":
    main()