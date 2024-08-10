# CIS129 YourName Inventory Management System
# Date: August 5, 2024
# Description: A basic inventory management system for a local store to track product levels, manage categories, and reorder products.

class Product:
    def __init__(self, product_id, name, category, price, quantity, min_stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.min_stock = min_stock

    def update_quantity(self, quantity):
        self.quantity += quantity
        print(f"Updated {self.name} quantity to {self.quantity}.")

    def update_price(self, new_price):
        self.price = new_price
        print(f"Updated {self.name} price to ${self.price:.2f}.")

    def needs_reorder(self):
        return self.quantity < self.min_stock

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Min Stock: {self.min_stock}"

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}
        self.categories = {}

    def add_product(self, product):
        self.inventory[product.product_id] = product
        if product.category not in self.categories:
            self.categories[product.category] = []
        self.categories[product.category].append(product)
        print(f"Added {product.name} to inventory.")

    def update_product(self, product_id, quantity=None, price=None):
        if product_id in self.inventory:
            if quantity is not None:
                self.inventory[product_id].update_quantity(quantity)
            if price is not None:
                self.inventory[product_id].update_price(price)
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.inventory:
            product = self.inventory.pop(product_id)
            self.categories[product.category].remove(product)
            print(f"Deleted {product.name} from inventory.")
        else:
            print("Product not found.")

    def check_reorder(self):
        for product in self.inventory.values():
            if product.needs_reorder():
                print(f"Reorder needed for {product.name} (Current Quantity: {product.quantity}, Minimum Stock: {product.min_stock})")

    def view_inventory(self):
        print("\nCurrent Inventory:")
        for product in self.inventory.values():
            print(product)

    def view_products_by_category(self, category):
        if category in self.categories:
            print(f"\nProducts in Category: {category}")
            for product in self.categories[category]:
                print(product)
        else:
            print("Category not found.")

    def generate_report(self):
        print("\nInventory Report:")
        self.view_inventory()
        print("\nReorder Alerts:")
        self.check_reorder()

# Main Program
def main():
    ims = InventoryManagementSystem()

    while True:
        print("\nInventory Management System")
        print("1. Add a New Product")
        print("2. Update Product Quantity")
        print("3. Update Product Price")
        print("4. View Inventory")
        print("5. View Products by Category")
        print("6. Delete a Product")
        print("7. Generate Inventory Report")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            min_stock = int(input("Enter Minimum Stock Level: "))
            product = Product(product_id, name, category, price, quantity, min_stock)
            ims.add_product(product)

        elif choice == "2":
            product_id = input("Enter Product ID to update quantity: ")
            quantity = int(input("Enter Quantity to add (use negative to subtract): "))
            ims.update_product(product_id, quantity=quantity)

        elif choice == "3":
            product_id = input("Enter Product ID to update price: ")
            price = float(input("Enter New Price: "))
            ims.update_product(product_id, price=price)

        elif choice == "4":
            ims.view_inventory()

        elif choice == "5":
            category = input("Enter Category to view products: ")
            ims.view_products_by_category(category)

        elif choice == "6":
            product_id = input("Enter Product ID to delete: ")
            ims.delete_product(product_id)

        elif choice == "7":
            ims.generate_report()

        elif choice == "8":
            print("Exiting Inventory Management System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
