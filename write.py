"""
This module contains functions for writing data to a file.
"""

def update_file(file_path, lands):
    """
    Updates the land data in the file with the new land status.

    Args:
        file_path (str): The path to the file containing land data.
        lands (list): A list of dictionaries representing the updated lands.
    """
    try:
        with open(file_path, 'w') as file:
            for land in lands:
                line = f"{land['id']}, {land['location']},{land['area']},{land['price']},{land['status']}"
                if 'rent_date' in land:
                    line += f",{land['rent_date']}"
                if 'return_date' in land:
                    line += f",{land['return_date']}"
                file.write(line + "\n")
        print(f"File '{file_path}' updated successfully.")
    except Exception as e:
        print(f"Error: {e}")