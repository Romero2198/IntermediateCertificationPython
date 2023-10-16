import Note

def create_note(number):
    title_create = check_len_text_input(
        input('Введите Название заметки: '), number)
    body_create = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(title = title_create, body = body_create)


def menu():
    print("\nЭто программа 'Заметки'. Имеются следующие функции:\n"
          "\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки"
          "\n4 - редактирование заметки\n5 - выборка заметок по дате"
          "\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")


def check_len_text_input(text: object, n: object) -> object:
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Завершение работы")