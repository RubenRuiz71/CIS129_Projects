def get_bottles():
    # Constants
    NBR_OF_DAYS = 7
    total_bottles = 0  # Initialize total bottles
    counter = 1        # Initialize counter
    today_bottles = 0  # Initialize bottles for today

    # Loop for each day
    while counter <= NBR_OF_DAYS:
        print(f"Enter number of bottles returned for day {counter}:")
        today_bottles = int(input())  # Get number of bottles for the day
        total_bottles += today_bottles  # Accumulate total bottles
        counter += 1  # Increment counter

    return total_bottles

def calc_payout(total_bottles):
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE
    return total_payout

def print_info(total_bottles, total_payout):
    print(f"\nTotal number of bottles collected: {total_bottles}")
    print(f"Total payout: ${total_payout:.2f}")

def main():
    keep_going = "y"  # Initialize to allow the loop to run

    while keep_going.lower() == "y":
        total_bottles = get_bottles()  # Get the total bottles for the week
        total_payout = calc_payout(total_bottles)  # Calculate the total payout
        print_info(total_bottles, total_payout)  # Print out the results
        
        print("Do you want to enter another week’s worth of data? (Enter y or n):")
        keep_going = input()  # Ask if the user wants to continue

if __name__ == "__main__":
    main()
