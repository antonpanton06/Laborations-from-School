#THE SITUATION: Juniper Café Collective wants to give customers a clear, readable receipt instead of handwritten totals.
#YOUR TASK: Create a small Python program that reads information about a table, the client, and three products, then prints a formatted receipt.
#
#THE INPUT:
#Table number: 7
#Client name: Ada Lovelace
#Tea, 18.5
#Sandwich, 42
#Fruit, 12.75

#Process the values here
café = "Juniper Café Collective"
table_number = input("Table number: ")
client_name = input("Client name: ")

product1 = input("Product 1: ")
price1 = float(input("Price 1: "))

product2 = input("Product 2: ")
price2 = float(input("Price 2: "))

product3 = input("Product 3: ")
price3 = float(input("Price 3: "))

total_price = float(price1 + price2 + price3)
#Print the receipt here
print()
print(café.upper())
print(f"Table: {table_number}")
print(f"Client: {client_name.upper()}")
print()
print(f"{product1:.<20}   {price1:.2f} SEK")
print(f"{product2:.<20}   {price2:.2f} SEK")
print(f"{product3:.<20}   {price3:.2f} SEK")
print()
print(f"Subtotal: {total_price:>18.2f} SEK")