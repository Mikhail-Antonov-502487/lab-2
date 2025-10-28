# кол-во записей, у которых длина строки "Название" > 30
import csv


with open('books-en.csv','r') as books:
    reader = csv.reader(books, delimiter = ';')  
    count = 0
    for row in reader:
        if len(row[1]) > 30:
            count += 1
    print(count)