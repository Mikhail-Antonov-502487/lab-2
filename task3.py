# генерация списка библиографических ссылок
import csv

 
biblio = []


with open('books-en.csv') as f:
    reader = csv.reader(f, delimiter=';')  
    count = 0  
    for i, row in enumerate(reader, 1):
        if len(row) >= 4:
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