import csv

# Function to collect user data and save it to CSV
def save_data_to_csv(filename):
    # List of fields for the CSV
    fields = ["Name", "Age", "Email"]

    # Collect user data
    user_data = {}
    for field in fields:
        user_data[field] = input(f"Enter {field}: ")

    # Write data to CSV
    with open(filename, mode="a", newline="") as file:  # "a" mode to append data
        writer = csv.writer(file)
        writer.writerow(user_data.values())

    print(f"Data saved to {filename} successfully.")

# Function to read data from CSV and print it
def read_data_from_csv(filename):
    # Open the CSV file and read data
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

# Main program
csv_filename = "user_data.csv"

# Save user input to CSV
save_data_to_csv(csv_filename)

# Read and display data from CSV
print("\nData in CSV file:")
read_data_from_csv(csv_filename)
