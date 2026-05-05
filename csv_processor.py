
import csv

def main():
    filename = 'data.csv'
    try:
        with open(filename, mode='r', encoding='utf-8') as file:   #mode=r --> to close the file after reading
            reader = csv.DictReader(file)  #to eery row to dict
            
            try:
                first_row = next(reader)
                print("First row found:")
                print(first_row)
                # if file is empty
            except StopIteration:
                print("The CSV file is empty.")
                #if file not found
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create a data.csv file.")

    main()