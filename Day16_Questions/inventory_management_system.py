# Question:
# Add, update, delete and display products.

inventory = {}

while True:

    print("\n1.Add Product")
    print("2.Update Product")
    print("3.Delete Product")
    print("4.Display")
    print("5.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        product = input("Product Name: ")
        qty = int(input("Quantity: "))

        inventory[product] = qty

    elif choice == 2:

        product = input("Product Name: ")
        qty = int(input("New Quantity: "))

        inventory[product] = qty

    elif choice == 3:

        product = input("Product Name: ")

        if product in inventory:
            del inventory[product]

    elif choice == 4:

        print("\nInventory")

        for p, q in inventory.items():
            print(p, ":", q)

    elif choice == 5:
        break