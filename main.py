from library import Book, Library

def main():
    library = Library()
    book_1 = Book(title="Капитанская дочка",
                  author="Пушкин",
                  year="1836",
                  genre="Роман")

    book_2 = Book(title="Герой нашего времени",
                  author="Лермонтов",
                  year="1836",
                  genre="Роман")

    library.add_book(book_1)
    library.add_book(book_2)

    books = library.get_books()
    for book in books:
        print(book.get_info())

    print(Library.get_book_count())


    qeury = "пуш"
    results = Library.search_book(query)
    if results:
        print("Найденные книги")
        for id_, book in results.items():
            print(f"{id_}.{book.get_info}"))
        else:
            print("ничего не найдено")



    id_for_del = "1"
    library.book_delete(id_for_del)

    books = library.get_books()
    for id_, book in books.items():
        print(f"{id_}.{book.get_info()}")



if __name__== '__main__':
    main()