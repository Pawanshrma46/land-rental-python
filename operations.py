#
# This module contains functions for renting, returning, and generating bills for lands.
#

import datetime

def rent_land(lands):
    #
    # Allows the user to rent one or more lands and updates the land status.

    # Args:
    #     lands (list): A list of dictionaries representing available lands.

    # Returns:
    #     list: A list of dictionaries representing the rented lands.
    #

    rented_lands = []
    land_ids = input("Enter the land IDs (separated by commas) to rent: ").split(',')

    for land_id in land_ids:
        land_id = land_id.strip()
        for land in lands:
            if land['id'] == land_id and land['status'] == 'available':
                land['status'] = 'rented'
                land['rent_date'] = datetime.date.today()
                rented_lands.append(land)
                print(f"Land with ID {land_id} has been rented.")
                break
        else:
            print(f"Land with ID {land_id} is not available or does not exist.")

    return rented_lands

def return_land(lands):
    #
    # Allows the user to return one or more lands and updates the land status.

    # Args:
    #     lands (list): A list of dictionaries representing available lands.

    # Returns:
    #     list: A list of dictionaries representing the returned lands.
    #

    returned_lands = []
    land_ids = input("Enter the land IDs (separated by commas) to return: ").split(',')

    for land_id in land_ids:
        land_id = land_id.strip()
        for land in lands:
            if land['id'] == land_id and land['status'] == 'rented':
                land['status'] = 'available'
                land['return_date'] = datetime.date.today()
                returned_lands.append(land)
                print(f"Land with ID {land_id} has been returned.")
                break
        else:
            print(f"Land with ID {land_id} is not rented or does not exist.")

    return returned_lands

def generate_bill(lands, operation):
    #
    # Generates a bill for rented or returned lands.

    # Args:
    #     lands (list): A list of dictionaries representing the rented or returned lands.
    #     operation (str): The operation being performed ('rent' or 'return').

    # Returns:
    #     str: The generated bill as a string.
    #

    bill = f"{'Rent' if operation == 'rent' else 'Return'} Bill\n\n"
    total_amount = 0
    total_fine = 0

    for land in lands:
        rent_date = land.get('rent_date', datetime.date.today())
        return_date = land.get('return_date', datetime.date.today())
        rented_months = (return_date.year - rent_date.year) * 12 + return_date.month - rent_date.month
        price = land['price'] * rented_months
        fine = 0

        if operation == 'return':
            if rented_months > (return_date - rent_date).days // 30:
                delayed_months = rented_months - (return_date - rent_date).days // 30
                fine = 0.1 * delayed_months * land['price']

        bill += f"Land ID: {land['id']}, {land['location']}, Area: {land['area']} aana, Price: Rs. {price}"

        if fine:
            bill += f", Fine: Rs. {fine:.2f}"

        bill += "\n"
        total_amount += price
        total_fine += fine

    bill += f"\nTotal Amount: Rs. {total_amount:.2f}"

    if total_fine:
        bill += f"\nTotal Fine: Rs. {total_fine:.2f}"
        bill += f"\nGrand Total: Rs. {total_amount + total_fine:.2f}"

    return bill