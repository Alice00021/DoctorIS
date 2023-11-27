import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTextBrowser
from PyQt6 import QtWidgets, QtCore
import os

class Ui_HelpForm(object):
    def setupUi(self, HelpForm):
        HelpForm.setObjectName("HelpForm")
        HelpForm.resize(600, 400)
        HelpForm.setWindowTitle("Справка")

        self.label = QtWidgets.QLabel(HelpForm)
        self.label.setGeometry(QtCore.QRect(20, 10, 200, 35))
        self.label.setText('Справочная система  ')
        self.label.setStyleSheet('color: #00557f; font-size: 18px;')

        self.info_text = QTextBrowser(HelpForm)
        self.info_text.setGeometry(QtCore.QRect(0, 50, 600, 350))
        self.info_text.setOpenExternalLinks(True)
        self.info_text.setStyleSheet('background-color: #f0f0f0; color: #000; font-size: 14px;')
        self.info_text.anchorClicked.connect(self.open_link)  # Подключаем обработчик события anchorClicked

        # Чтение информации о врачах из файла и создание гиперссылок
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, 'Templates/doctors_info.html')  # Используем HTML-файл для создания гиперссылок

        with open(file_path, 'r', encoding='utf-8') as file:
            doctors_info = file.read()
            self.info_text.setHtml(doctors_info)

    def open_link(self, url):
        # Открываем страницу по ссылке
        file_path = os.path.join(os.path.dirname(__file__), url.path())  # Получаем путь к файлу из URL
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                page_content = file.read()
                self.info_text.setHtml(page_content)  # Отображаем содержимое файла в QTextBrowser
        else:
            print(f"Файл {file_path} не найден")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    HelpForm = QtWidgets.QWidget()
    ui = Ui_HelpForm()
    ui.setupUi(HelpForm)
    HelpForm.show()
    sys.exit(app.exec())