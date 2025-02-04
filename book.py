from datetime import datetime

import uuid

from core.enmus import *


class Book:
    def __init__(self, title, author,
                 year, genre=None, isbn=None):
        """
        Конструктор класса Book
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        :param genre: Жанр книги (по умолнчанию None)
        :param isbn: ISBN книги (по умолнчанию None)
        """
        self.title = title
        self.author = author
        self._year = year
        self.genre = genre
        self.__isbn = uuid.uuid4().hex[:9]

    def get_info(self):
        """
        Возвращает строгки с информацией о книге
        :return: Строка с информацией о книге
        """
        info = f"{self.title} - {self.author} ({self.year}"
        if self.genre:
            info +- f", Жанр: {self.genre}"
        if self.__isbn:
            info +- f", ISBN: {self.__isbn}"

        return info

    def is_older_than(self, year):
        """
        Проверяет, была ли книга издана до указанного года
        :param year: год издания
        :return: bool
        """
        return self._year < year

    @property
    def year(self):
        return self._year

    @genre.setter
    def genre(self, genre):
        if genre.lower() in GENRES:
            self._genre = genre
        else:
            raise ValueError("есть")

    def get_book_age(self):
        current_year = datetime.today().year
        return current_year - self._year

    @year.setter
    def year(self, new_year):
       if self.is_valid_year(new_year):
           self._year = new_year
       else:
           raise ValueError("НЕВЕРНОЕ ЗНАЧЕНИЕ ДЛЯ ГОДА ИЗДАНИЯ!!!!!!!!!!!!!!!")


        def get_book_age(self):
            current_year = datetime.today().year
            return current_year - self._year


book = Book(title="Капитанская дочка",
            author="А.С. Пушкин",
            year=1836,
            genre="Роман")

print(book.get_info())


