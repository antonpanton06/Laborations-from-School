# Python Labs

A collection of Python programs I wrote during class to practise programming fundamentals.

| Lab | Description | Main topics |
| --- | --- | --- |
| 01 | Displays a festival welcome message and ticket kiosk menu. | Variables, strings, printing, f-strings |
| 02 | Calculates booking duration, unit conversions, and discounted prices. | Data types, arithmetic, type conversion |
| 03 | Takes customer and product details and prints a café receipt. | User input, floats, string formatting |
| 04 | Determines a passenger’s fare based on age and student status. | Conditionals, comparisons, logical operators |
| 05 | Summarises a week of study hours and assigns a performance category. | For loops, counters, averages, conditionals |
| 06 | Takes café orders and calculates a discounted total. | While loops, menus, running totals |
| 07 | Organises a shop ordering system into separate functions. | Functions, parameters, return values, loops |
| 08 | Records participation across daily sessions and summarises each week. | Nested lists, iteration, aggregation |
| 09 | Recursively totals scores, treating negative scores as doubled penalties. | Recursion, lists, base cases |
| 10 | Calculates average scores, counts passing scores, and determines a result. | Functions, constants, lists, tuple unpacking |
| 11 | Stores players and their scores and generates performance summaries. | Dictionaries, lists, recursion, error handling |
| 12 | Loads, edits, and saves measurements and summary reports. | Text files, pathlib, validation, exceptions |
| 13 | Reads student scores and exports totals in CSV and JSON formats. | CSV, JSON, modules, folder handling |
| 14 | Extracts SEK amounts from receipts and saves spending summaries. | Regex, JSON, file writing, statistics |

## Extra Practice

- **re_testlab.py:** Checks email input against a basic pattern using regex and `re.fullmatch()`.

These are learning exercises and are still being improved. Known issues and limitations:

- **Lab 04:** Some student answers bypass the 18–25 age restriction because of how the condition is grouped.
- **Lab 07:** The subtotal is not accumulated, and discounts are calculated before the selected product’s price is set.
- **Lab 08:** Negative participation input can save an incomplete or empty week; an empty week causes division by zero in the summary.
- **Lab 11:** Summaries only display the last player and crash when no players exist. A zero average is labelled N/A even when scores have been recorded.
- **Lab 12:** Reports with no measurements omit the average and skipped count.
- **Labs 13–14:** Run each program from its own lab folder, since input and output paths are relative to the working directory.
