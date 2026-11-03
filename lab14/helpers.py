import re

def extract_prices(text):
    # Extract and convert SEK amounts
    pattern = r"(\d+[.,]\d{2}) SEK"
    matches = re.findall(pattern, text)

    prices = []
    for  amount in matches:

        normalized = re.sub(r",", ".", amount)
        price = float(normalized)
        prices.append(price)
    return prices
   
    
def calculate_statistics(prices):
    # Calculate total and average
    total = sum(prices)
    if len(prices) == 0:
        average = 0
    else:
        average = total / len(prices)
    return total, average

def statistics(data): # calculate overall statistics

    all_prices = []
    receipt_results = []
    for receipt in data["receipts"]:

        prices = extract_prices(receipt["text"])
        all_prices.extend(prices)
        total, average = calculate_statistics(prices)
        receipt_results.append({
        "id": receipt["id"],
        "shop": receipt["shop"],
        "prices": prices,
        "total": total,
        "average": average})

    overall_total, overall_average = calculate_statistics(all_prices)
    number_of_amounts = len(all_prices)

    return receipt_results, overall_total, overall_average, number_of_amounts
