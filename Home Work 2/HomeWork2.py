def custom_write(file_name, strings):
    # Создаем пустой словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл в режиме записи (это удалит его старое содержимое)
    with open(file_name, 'w', encoding='utf-8') as file:
        # Проходим по списку строк и записываем их в файл
        for line_number, string in enumerate(strings, start=1):
            # Получаем текущую позицию в байтах в начале строки
            byte_position = file.tell()

            # Записываем строку в файл с новой строкой
            file.write(string + '\n')

            # Добавляем позицию строки в словарь
            strings_positions[(line_number, byte_position)] = string

    # Возвращаем словарь с позициями строк
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('HW.txt', info)
for elem in result.items():
  print(elem)
