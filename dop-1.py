import csv

def get_unique_publishers():
    with open('books-en.csv') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        unique_publishers = set()
        
        for row in reader:
            publisher = row[4]  
            unique_publishers.add(publisher)
        
        print("Перечень уникальных издательств:")
        for publisher in sorted(unique_publishers):
            print(publisher)
            print()

get_unique_publishers()