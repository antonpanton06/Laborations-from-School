total = 0
items = 0
print("1. Coffee -- 25 SEK")
print("2. Sandwich -- 45 SEK")
print("3. Cake  35 -- SEK")
print("0. Finish order")
# Print the menu
choice = input("Choice: ")
while choice != "0":
    # Check the choice
    
    
    if choice == "1":
        print("Coffee: 25.00 SEK")
        total += 25
        items += 1
        
    elif choice == "2":
        print("Sandwich: 45.00 SEK")
        total += 45
        items += 1
        
    elif choice == "3":
        print("Cake: 35.00 SEK")
        total += 35
        items += 1
        
    else:
        print("Invalid choice.")

    choice = input("Choice: ")


print()
print("Order finished!")
    # Process the selected item
    # Read the next choice



# Calculate the discount
if total < 50:
    discount_rate = 0
elif total < 99.99:
    discount_rate = 0.05
else:
    discount_rate = 0.1

# Calculate the final total
discount = total * discount_rate
total_with_discount = total - discount

# Print the summary
print(f"Items: {items}")
print(f"{'Subtotal':.<16}{total:.>6.2f} SEK")
print(f"{'Discount':.<16}{discount:.>6.2f} SEK")
print(f"{'Total':.<16}{total_with_discount:.>6.2f} SEK")
