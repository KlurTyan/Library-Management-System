from models import Library

DATA_FILE = "books.json"
library = Library(DATA_FILE)

try:
    while True:
        print("\nСистема управления библиотекой")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год издания книги: ")
                status = input(
                    "Введите статус книги ( 1 -> В наличии или  2 -> Выдана): "
                )
                if status == "1":
                    print(library.add_book(title, author, int(year), "В наличии"))
                elif status == "2":
                    print(library.add_book(title, author, int(year), "Выдана"))
                else:
                    print("Вы ввели некорректное число в поле статуса!")

            elif choice == "2":
                book_id = int(input("Введите ID книги для удаления: "))
                print(library.remove_book(book_id))

            elif choice == "3":
                search_by = input(
                    "Введите значение для поиска по (title, author, year): "
                )
                print(library.search_book(search_by))

            elif choice == "4":
                library.display_books()

            elif choice == "5":
                book_id = int(input("Введите ID книги для изменения статуса: "))
                new_status = input(
                    "Введите статус книги ( 1 -> В наличии или  2 -> Выдана): "
                )
                if new_status == 1:
                    print(library.change_status_book(book_id, "В наличии"))
                elif new_status == 2:
                    print(library.change_status_book(book_id, "Выдана"))

            elif choice == "6":
                break

            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

        except ValueError:
            print(f"\nВы ввели не число! Пожалуйста, попробуйте снова.")


except KeyboardInterrupt:
    print("\nПока!")
