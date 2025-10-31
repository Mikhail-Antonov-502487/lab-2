import csv


def popular_books():

    with open('books-en.csv', 'r') as books:
        reader = csv.reader(books, delimiter=';')
        next(reader)
        list_books = []
        
        for row in reader:
            title = row[1]  
            author = row[2]  
            downloads = int(row[5])  
            list_books.append((title, author, downloads))
        
        sorted_books = sorted(list_books, key = lambda x: x[2], reverse=True)
        most_pop = sorted_books[:20]
        
        print("Cамые популярные 20 книг:")
        for i, (title, author, downloads) in enumerate(most_pop, start=1):
            print(f"{i}. {title} - {author} (Загрузок: {downloads})")

popular_books()