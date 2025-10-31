# поиск книги по автору
import csv


def search_books_by_author(author_name):
    books = []
    
    
    with open('books-en.csv') as file:
        reader = csv.DictReader(file, delimiter=';')   
        for row in reader:
            try:
                year = int(row['Year-Of-Publication'])   
                if (1991 <= year < 1995):
                    if author_name.lower() in row['Book-Author'].lower():
                        books.append(row)   
            except ValueError:
                continue   
    return books


author_to_search = input("Введите имя автора для поиска книг: ")
found_books = search_books_by_author(author_to_search)


if found_books:
    print(f"\nКниги автора '{author_to_search}' с 1991 до 1995 года:")
    for book in found_books:
        title = book['Book-Title']
        year = book['Year-Of-Publication']
        print(f"Название: {title}, Год: {year}")
else:
    print(f"Нет книг автора '{author_to_search}' с 1991 до 1995 года.")