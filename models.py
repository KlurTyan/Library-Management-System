import json


class Book:
    """
    Класс для представления книги.

    Атрибуты:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги (например, "В наличии", "Выдана").
        book_id (int): Уникальный идентификатор книги.
    """

    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        status: str,
        book_id: int,
    ):
        self.book_id = book_id
        self.title = title
        self.year = year
        self.author = author
        self.status = status

    def to_dict(self):
        """
        Преобразует объект книги в словарь.
        """
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }


class Library:
    """
    Класс для управления библиотекой.
    """

    def __init__(self, data_file: str):
        self.data_file = data_file
        self.books = self._load_books()
        self.id = self._max_value_id()

    def _max_value_id(self):
        """
        Определяет максимальное значение идентификатора книги.
        """

        if not self.books:
            return 1
        return max(book["book_id"] for book in self.books) + 1

    def _save_file(self, list_books: list) -> list:
        """
        Сохраняет список книг в файл.
        """
        with open(self.data_file, "w", encoding="utf-8") as books:
            json.dump(
                list_books,
                books,
                ensure_ascii=False,
                indent=4,
            )
        return "Книга успешно добавлена!"

    def _load_books(self):
        """
        Загружает список книг из файла.
        """

        try:
            with open(self.data_file, encoding="utf-8") as books_file:
                books_data = json.load(books_file)
                return books_data
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            print(
                f"Ошибка чтения файла {self.data_file}. Файл может быть пустым или содержать некорректные данные.",
                f"Файл был успешно изменен!",
            )
            return self._save_file([])

    def _format_book_info(self, book: dict) -> str:
        """
        Форматирует информацию о книге для вывода.
        """

        return f"\nID: {book['book_id']}\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nStatus: {book['status']}"

    def add_book(self, title: str, author: str, year: int, status: str):
        """
        Добавляет новую книгу в библиотеку.
        """
        book = Book(title, author, year, status, self.id).to_dict()
        if status in ["В наличии", "Выдана"]:
            self.id += 1
            self.books.append(book)
        else:
            return "Такого статуса нет в программе, пожалуйста попробуйте еще раз!"
        return self._save_file(self.books)

    def search_book(self, *args):
        """
        Ищет книги по заданным параметрам.
        """

        ls = []
        books = self._load_books()

        for arg in args:
            if arg.isdigit():
                arg = int(arg)

        for book in books:
            if isinstance(arg, int) and book["year"] == arg:
                ls.append(self._format_book_info(book))

            elif book["title"] == arg or book["author"] == arg:
                ls.append(self._format_book_info(book))

        return "\n".join(ls) if ls else "\nКнига не найдена :("

    def remove_book(self, book_id: int):
        """
        Удаляет книгу по её идентификатору.
        """

        try:
            data_books = self._load_books()
            found = False
            for book in range(len(data_books)):
                print(data_books[book]["book_id"])
                if data_books[book]["book_id"] == book_id:
                    data_books.pop(book)
                    found = True
                    break

            if found:
                self._save_file(data_books)
                return f"Книга под номер - {book_id}\nУспешно удалена!"
            else:
                return f"Книга под номером - {book_id} не найдена!"

        except ValueError:
            return f"Вы ввели не число!"

    def display_books(self):
        """
        Выводит список всех книг в библиотеке.
        """

        list_books = self._load_books()
        for book in list_books:
            print(self._format_book_info(book))
        return self._load_books()

    def change_status_book(self, book_id: int, status: str):
        """
        Изменяет статус книги.
        """

        books = self._load_books()
        for book in books:
            if book["book_id"] == book_id:
                book["status"] = status
                break

        self._save_file(books)
        return f"\nСтатус успешно изменен на {status}"
