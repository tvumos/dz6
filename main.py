"""
Домашнее задание № 6 - Трясцын Владимир
"""

import module.dz_lib as lib
import module.victory as game_victory
import module.bill as game_bill

CREATE_DIR = "Создать папку"
DELETE_FILE_DIR = "Удалить (файл/папку)"
COPY_FILE_DIR = "Копировать (файл/папку)"
SHOW_CURRENT_DIR = "Просмотр содержимого рабочей директории"
SHOW_FILES_IN_CURRENT_DIR = "Посмотреть только папки"
SHOW_DIRS_IN_CURRENT_DIR = "Посмотреть только файлы"
SHOW_SYSTEM_INFO = "Просмотр информации об операционной системе"
SHOW_AUTHOR = "Создатель программы"
GAME_VICTORY = "Играть в викторину"
GAME_BILL = "Мой банковский счет"
CHANGE_CURRENT_DIR = "Смена рабочей директории"
EXIT_PROGRAM = "Выход"

menu_actions = {
    EXIT_PROGRAM: lib.exit_program,
    CREATE_DIR: lib.create_dir,
    DELETE_FILE_DIR: lib.del_file_or_dir,
    COPY_FILE_DIR: lib.copy_file_or_dir,
    SHOW_CURRENT_DIR: lib.find_all_in_current_dir,
    SHOW_FILES_IN_CURRENT_DIR: lib.get_dir_in_current_dir,
    SHOW_DIRS_IN_CURRENT_DIR: lib.get_files_in_current_dir,
    SHOW_SYSTEM_INFO: lib.get_system_info,
    SHOW_AUTHOR: lib.show_author,
    GAME_VICTORY: game_victory.victory_run,
    GAME_BILL: game_bill.my_bill_run,
    CHANGE_CURRENT_DIR: lib.change_current_dir
}


def is_correct_input(choice):
    return choice.isdigit() and int(choice) >=0 and int(choice) < len(menu_actions)


# Меню программы
while True:
    #lib.show_help()
    lib.print_menu(menu_actions)
    response = input('Укажите пункт меню -> ')
    if is_correct_input(response):
        menu_name = list(menu_actions.keys())[int(response)]
        action = menu_actions[menu_name]
        action()
    else:
        print("Не корректный вод пункта меню. Повторите ввод.")

    # if response == '1':  # Создать папку
    #     lib.create_dir()
    # elif response == '2':  # Удалить (файл/папку)
    #     lib.del_file_or_dir()
    # elif response == '3':  # Копировать (файл/папку)
    #     lib.copy_file_or_dir()
    # elif response == '4':  # Просмотр содержимого рабочей директории
    #     lib.find_all_in_current_dir()
    # elif response == '5':  # Посмотреть только папки
    #     lib.get_dir_in_current_dir()
    # elif response == '6':  # Посмотреть только файлы
    #     lib.get_files_in_current_dir()
    # elif response == '7':  # Просмотр информации об операционной системе
    #     lib.get_system_info()
    # elif response == '8':  # Создатель программы
    #     print(lib.show_autor())
    # elif response == '9':  # Играть в викторину
    #     answer = input('Укажите количество вопросов в викторине: -> ')
    #     if answer.isdigit():
    #         count_questions = int(answer)
    #         if (count_questions >= 10) | (count_questions < 2):
    #             print("В викторине будет 5 вопросов")
    #             game_victory.victory_run()
    #         else:
    #             game_victory.victory_run(count_questions)
    # elif response == '10':  # Мой банковский счет
    #     game_bill.my_bill_run()
    # elif response == '11':  # Смена рабочей директории
    #     lib.change_current_dir()
    # elif response == '0':  # Выход
    #     print('Программа завершается!')
    #     break
    # else:
    #     print("Не корректный вод пункта меню. Повторите ввод.")
