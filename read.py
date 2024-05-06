"""
This module contains functions for reading land data from a file.
"""

def read_lands(file_path):
    """
    Reads land data from a file and returns a list of dictionaries.

    Args:
        file_path (str): The path to the file containing land data.

    Returns:
        list: A list of dictionaries, where each dictionary represents a land.
    """
    lands = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                land_data = line.strip().split(',')
                land = {
                    'id': land_data[0],
                    'location': land_data[1],
                    'area': int(land_data[2]),
                    'price': int(land_data[3]),
                    'status': land_data[4],
                }
                lands.append(land)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return lands



