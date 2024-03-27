# Модуль для работы с файлами

def save_file(filename, content):
    # Сохранение файла
    with open(filename, 'w') as file:
        file.write(content)

def open_file(filename):
    # Открытие файла
    with open(filename, 'r') as file:
        content = file.read()
    return content

# Модуль для управления вкладками
class TabManager:
    def __init__(self):
        self.tabs = []

    def add_tab(self, tab):
        self.tabs.append(tab)

    def switch_tab(self, index):
        # Переключение на выбранную вкладку
        pass

    def close_tab(self, index):
        # Закрытие выбранной вкладки
        pass
