# генерация списка библиографических ссылок
import csv

 
biblio = []


with open('books-en.csv') as text:
    reader = csv.reader(text, delimiter=';')
    for row in reader:
        books = list(reader)   

 
with open('books-en.csv') as file:
    reader = csv.reader(file, delimiter=';')  


    count = 0 
    i = 0  
    for row in reader:
        if len(row) >= 4:   
            i += 1
            title = row[1]
            author = row[2]
            year = row[3]

             
            citation = f"{i}. {author}. \"{title}\" - {year}."
            biblio.append(citation)
            count += 1


            if count >= 21:
                break

 
with open('biblio.txt', mode='w', encoding='utf-8') as biblio_file:
    for entry in biblio:
        biblio_file.write(entry + '\n')


print("Библиографические ссылки созданы и сохранены в файл biblio.txt.")