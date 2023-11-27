import psycopg2
from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_ListOfDoctorsForm(object):
    def setupUi(self, ListOfDoctorsForm):
        ListOfDoctorsForm.setObjectName("Список врачей")
        ListOfDoctorsForm.resize(659, 440)

        ListOfDoctorsForm.setStyleSheet(
        """
        QWidget {
            background-color: #f0f0f0;  /* Цвет фона */
        }
        QLabel {
            color: #00557f;  /* Основной цвет текста */
            font-size: 12px;  /* Размер шрифта */
        }
        QLineEdit, QDateEdit {
            background-color: #fff;  /* Цвет фона поля ввода */
            border: 1px solid #aaa;  /* Обводка полей ввода */
            padding: 5px;  /* Отступ вокруг текста в полях ввода */
        }
        QPushButton {
            background-color: #00557f;  /* Цвет фона кнопки */
            color: #fff;  /* Цвет текста кнопки */
            border: 1px solid #00557f;  /* Обводка кнопки */
            padding: 5px;  /* Отступ вокруг текста в кнопке */
        }
        """
        )


        self.widget = QtWidgets.QWidget(parent=ListOfDoctorsForm)
        self.widget.setGeometry(QtCore.QRect(40, 10, 300, 200))  

        # Добавление заголовка
        self.titleLabel = QtWidgets.QLabel(parent=ListOfDoctorsForm)
        self.titleLabel.setGeometry(QtCore.QRect(200, 10, 250, 30))
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#00557f;\">Список врачей</span></p></body></html>")

        self.searchEdit = QtWidgets.QLineEdit(ListOfDoctorsForm)
        self.searchEdit.setGeometry(QtCore.QRect(10, 50, 560, 28))
        self.searchEdit.setObjectName("search")

        self.searchButton = QtWidgets.QPushButton(ListOfDoctorsForm)
        self.searchButton.setGeometry(QtCore.QRect(570, 50, 70, 28))
        self.searchButton.setText("Поиск")
        

        
        
        conn = psycopg2.connect(
            dbname="Больница", 
            user="postgres", 
            password="2118", 
            host="localhost"
        )

        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM doctor")  # Запрос для получения количества записей в таблице
        row_count = cur.fetchone()[0]  # Получение количества записей
        #self.tableWidget.setRowCount(row_count)  # Установка количества строк в таблице

        self.tableWidget = QtWidgets.QTableWidget(row_count, 5, parent=ListOfDoctorsForm)
        self.tableWidget.setGeometry(QtCore.QRect(0, 100, 660, 340))
        self.tableWidget.setObjectName("tableWidget")
        # Добавление заголовков столбцов
        self.tableWidget.setHorizontalHeaderLabels(["Код врача", "Фамилия","Имя","Отчество","Должность"])

        # Растянуть второй столбец на оставшуюся таблицу
        # Растянуть второй столбец на оставшуюся таблицу
       
        # Установить размер столбца 0
        self.tableWidget.setColumnWidth(0, 80)  
        self.tableWidget.setColumnWidth(1, 130)  
        self.tableWidget.setColumnWidth(2, 130)  
        self.tableWidget.setColumnWidth(3, 148)  
        self.tableWidget.setColumnWidth(4, 130)  
       

        # Установить высоту строки 0
        self.tableWidget.setRowHeight(0, 20) 
        self.tableWidget.setRowHeight(1, 20)  # Устанавливает высоту строки 0 равной 100 пикселям
        self.tableWidget.setRowHeight(2, 20) 
        self.tableWidget.setRowHeight(3, 20) 
        self.tableWidget.setRowHeight(4, 20)
        self.tableWidget.setRowHeight(5, 20) 


        cur.execute("SELECT  doctor.code_doctor, doctor.lastname,doctor.firstname,doctor.middlename, position_doctor.name_of_position FROM doctor JOIN position_doctor ON doctor.id_position = position_doctor.id_position")
        rows = cur.fetchall()


      
# Заполнение таблицы данными
        for row_number, row_data in enumerate(rows):
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)
     

        self.retranslateUi(ListOfDoctorsForm)
        QtCore.QMetaObject.connectSlotsByName(ListOfDoctorsForm)

        def search_doctor():
            search_text = self.searchEdit.text().strip()  # Получаем текст из QLineEdit
            if search_text:  # Проверяем, что введен поисковый запрос
                conn = psycopg2.connect(
            dbname="Больница", 
            user="postgres", 
            password="2118", 
            host="localhost"
        )
                cur = conn.cursor()
                cur.execute("""
                SELECT doctor.code_doctor, doctor.lastname, doctor.firstname, doctor.middlename, position_doctor.name_of_position 
                FROM doctor 
                JOIN position_doctor ON doctor.id_position = position_doctor.id_position 
                WHERE doctor.lastname LIKE %s 
                OR doctor.firstname LIKE %s 
                OR doctor.middlename LIKE %s 
                OR position_doctor.name_of_position LIKE %s
""", ('%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%'))  # Получение результатов запроса
                self.tableWidget.setRowCount(0)  # Очистка таблицы
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))  # Установка количества строк в соответствии с результатами запроса
                for row_number, row_data in enumerate(rows):
                    for column_number, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        self.tableWidget.setItem(row_number, column_number, item)
                  # Заполнение ячеек таблицы данным
                self.tableWidget.setColumnWidth(4, 155)  
                
                cur.close()
                conn.close()

        self.searchButton.clicked.connect(search_doctor)

    def retranslateUi(self, AddAppointmentForm):
        _translate = QtCore.QCoreApplication.translate
        AddAppointmentForm.setWindowTitle(_translate("AddAppointmentForm", "Список врачей"))
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddAppointmentForm = QtWidgets.QWidget()
    ui = Ui_ListOfDoctorsForm()
    ui.setupUi(AddAppointmentForm)
    AddAppointmentForm.show()
    sys.exit(app.exec())
