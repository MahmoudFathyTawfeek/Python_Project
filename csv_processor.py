
import csv

def main():
    filename = 'data.csv'
    try:
        with open(filename, mode='r', encoding='utf-8') as file:   #mode=r --> to close the file after reading
            reader = csv.DictReader(file)  #every row to dict
            
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
# if __name__ == "__main__":    #تشغيل الكود عند تشغيل الملف وليس عند استدعاءه
    main()