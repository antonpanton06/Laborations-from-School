
product1 = "Notebook"
price1 = 40
product2 = "Mug"
price2 = 60
product3 = "Tote bag"
price3 = 80

def show_products():
    # Display the available products
    print()
    print("Choice: 1")
    print()
    print("AVAILABLE PRODUCTS")
    print(f"1. {product1} - {price1:.2f} SEK")
    print(f"2. {product2} - {price2:.2f} SEK")
    print(f"3. {product3} - {price3:.2f} SEK")
    print()


def make_order():
    items = 0
    total_price = 0
    discount = 0
    product_discount = 0
    price = 0
    quantity = 0
    product_total = price * quantity
    print("Choice: 2")
    print()
    print("MAKE AN ORDER")
    print("Enter 0 when you are finished ordering.")
    # Let the customer add products
# Return the order information
    while True:
        product_choice = int(input("Product: "))
        if product_choice == 0:
            break

        quantity = int(input("Quantity: "))
        while quantity < 1:
            print("Quantity must be at least 1.")
            quantity = int(input("Quantity: "))

        if quantity >= 5:
            product_discount = price * quantity * 0.10
            discount += product_discount
            product_total = total_price - product_discount

        if product_choice < 1 or product_choice > 3:
            print("Invalid product.")
            continue

        if product_choice == 1:
            price = price1
            product_total = price * quantity
            items += quantity
            print("Product: 1")
            print(f"Quantity: {quantity}")
            print(f"{product1} x{quantity}: {product_total:.2f} SEK")
            continue

        elif product_choice == 2:
            price = price2
            product_total = price * quantity
            items += quantity
            print("Product: 2")
            print(f"Quantity: {quantity}")
            print(f"{product2} x{quantity}: {product_total:.2f} SEK")
            continue

        elif product_choice == 3:
            price = price3
            items += quantity
            product_total = price3 * quantity
            print("Product: 3")
            print(f"Quantity: {quantity}")
            print(f"{product3} x{quantity}: {product_total:.2f} SEK")
            continue

        else:
            print("Invalid choice, choose between 1,2 or 3.")

    return items, total_price, discount


def finish_order(items, total_price, product_discount):
    total_with_discount = total_price - product_discount
    # Display the final receipt
    print("Choice 3:")
    print()
    print("LANTERN POP-UP RETAIL")
    print(f"Items: {items}")
    print(f"{'Subtotal':.<16}{total_price:.>6.2f} SEK")
    print(f"{'Discount':.<16}{product_discount:.>6.2f} SEK")
    print(f"{'Total':.<16}{total_with_discount:.>6.2f} SEK")

 

def main():
    items = 0
    total_price = 0
    discount = 0

    while True:
    # Display the main menu
        print("LANTERN POP-UP RETAIL")
        print("1. View products")
        print("2. Make an order")
        print("3. Finish")
    # Process the customer's choice
        choice = int(input())
        if choice == 1:
            show_products()

        elif choice == 2:
            items, total_price, discount = make_order()

        elif choice == 3:
            finish_order(items, total_price, discount)
            return
        else: 
            print("Invalid choice!")


if __name__ == "__main__":
    main()

"The finished recipt needs changing, doesn't return right values."