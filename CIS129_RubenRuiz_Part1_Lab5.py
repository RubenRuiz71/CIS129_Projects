def process_sales():
    # Get the monthly Sales
    monthly_sales = float(input("Enter the monthly sales: "))

    # Get the Increase in Sales
    sales_increase = float(input("Enter the increase in sales: "))

    # Calculate the Store Bonus (example calculation, change as needed)
    store_amount = monthly_sales * 0.1  # Example calculation

    # Calculate the Employee Bonus (example calculation, change as needed)
    emp_amount = sales_increase * 0.05  # Example calculation

    # Print out all the results
    print(f"\nStore Bonus: ${store_amount:.2f}")
    print(f"Employee Bonus: ${emp_amount:.2f}")

def main_while_loop():
    keepGoing = "y"
    
    while keepGoing.lower() == "y":
        process_sales()
        keepGoing = input("Do you want to run the program again? (Enter y for yes): ")

def main_do_while_loop():
    keepGoing = "y"
    
    while True:
        process_sales()
        keepGoing = input("Do you want to run the program again? (Enter y for yes): ")
        
        if keepGoing.lower() != "y":
            break

# Main function to choose loop type
def main():
    loop_type = input("Enter 'while' to use the while loop or 'do-while' to use the do-while loop simulation: ").strip().lower()
    
    if loop_type == "while":
        main_while_loop()
    elif loop_type == "do-while":
        main_do_while_loop()
    else:
        print("Invalid choice. Please enter 'while' or 'do-while'.")

# Run the main function
if __name__ == "__main__":
    main()
