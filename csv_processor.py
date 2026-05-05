
import csv

def main():
    filename = 'data.csv'
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            try:
                first_row = next(reader)
                print("First row found:")
                print(first_row)
            except StopIteration:
                print("The CSV file is empty.")
                
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create a data.csv file.")

if __name__ == "__main__":
    main()