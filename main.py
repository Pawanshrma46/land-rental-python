# """
# This is the main module of the land rental system.
# It imports functions from other modules and provides the user interface.
# """
from read import read_lands
from operations import rent_land, return_land, generate_bill
from write import update_file

def main():
    # """
    # The main function that runs the land rental system.
    # """
    lands = read_lands("lands.txt")
    while True:
        print("\n*****************************")
        print("\nWelcome to the Land Rental System!")
        print("\n*****************************")
        print("\n")
        print("\n--------------------------------")
        print("Available options:")
        print("\n--------------------------------")
        print("\n")
        print("1. press 1 for Show available lands")
        print("2. press 2 for Rent land")
        print("3. press 3 fro Return land")
        print("4. press 3 for Exit ")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            print("\n--------------------------------")
            print("\nAvailable lands:")
            print("\n--------------------------------")
            for land in lands:
                if land['status'] == 'available':
                    print(f"Kitta no: {land['id']}, Location: name {land['location']} Area: {land['area']}aana, Price: Rs. {land['price']}per month, ")

        elif choice == 2:
            rented_lands = rent_land(lands)
            if rented_lands:
                bill = generate_bill(rented_lands, "rent")
                print(bill)
                update_file("lands.txt", lands)

        elif choice == 3:
            returned_lands = return_land(lands)
            if returned_lands:
                bill = generate_bill(returned_lands, "return")
                print(bill)
                update_file("lands.txt", lands)

        elif choice == 4:
            print("\n*************************************************************************************")
            print("Thank you for using the Land Rental System. Goodbye! ")
            print("\n*************************************************************************************")
            break

        else:
            print("\n--------------------------------")
            print("Invalid choice. Please try again.")
            print("\n--------------------------------")

if __name__ == "__main__":
    main()