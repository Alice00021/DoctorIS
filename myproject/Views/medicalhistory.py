import psycopg2
from PyQt6 import QtCore, QtGui, QtWidgets
from user import user_inf

""" SELECT medical_report.datemeet, medical_report.code_doctor, 
doctor.lastname, doctor.firstname, doctor.middlename, position_doctor.name_of_position
from medical_report 
JOIN doctor
ON 
medical_report.code_doctor=doctor.code_doctor
JOIN position_doctor
ON
position_doctor.id_position= doctor.id_position
JOIN patient
ON
medical_report.patient_code= patient.patient_code
WHERE patient.patient_code=3613; """
class Ui_MedicalHistoryForm(object):
    def __init__(self):
        self.user_inf=user_inf
    def setupUi(self, MedicalHistoryForm):
        MedicalHistoryForm.setObjectName("История посещения")
        MedicalHistoryForm.resize(740, 390)

        MedicalHistoryForm.setStyleSheet(
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

        self.widget = QtWidgets.QWidget(parent=MedicalHistoryForm)
        self.widget.setGeometry(QtCore.QRect(40, 10, 300, 200))  

        # Добавление заголовка
        self.titleLabel = QtWidgets.QLabel(parent=MedicalHistoryForm)
        self.titleLabel.setGeometry(QtCore.QRect(260, 10, 250, 30))
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#00557f;\">История посещений</span></p></body></html>")


        self.tableWidget = QtWidgets.QTableWidget(12, 6, parent=MedicalHistoryForm)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 740, 400))
        self.tableWidget.setObjectName("tableWidget")
        # Добавление заголовков столбцов
        self.tableWidget.setHorizontalHeaderLabels(["Код врача", "Фамилия","Имя","Отчество","Должность", "Время посещения"])

        # Растянуть второй столбец на оставшуюся таблицу
        # Растянуть второй столбец на оставшуюся таблицу
       
        # Установить размер столбца 0
        self.tableWidget.setColumnWidth(0, 80)  
        self.tableWidget.setColumnWidth(1, 120)  
        self.tableWidget.setColumnWidth(2, 120) 
        self.tableWidget.setColumnWidth(3, 128)  
        self.tableWidget.setColumnWidth(4, 120)  
        self.tableWidget.setColumnWidth(5, 130)  

         # Установить высоту строки 0
        self.tableWidget.setRowHeight(0, 26) 
        self.tableWidget.setRowHeight(1, 26)  # Устанавливает высоту строки 0 равной 100 пикселям
        self.tableWidget.setRowHeight(2, 26) 
        self.tableWidget.setRowHeight(3, 26) 
        self.tableWidget.setRowHeight(4, 26) 
        self.tableWidget.setRowHeight(5, 26) 
        self.tableWidget.setRowHeight(6, 26) 
        self.tableWidget.setRowHeight(7, 26)  # Устанавливает высоту строки 0 равной 100 пикселям
        self.tableWidget.setRowHeight(8, 26) 
        self.tableWidget.setRowHeight(9, 26) 
        self.tableWidget.setRowHeight(10, 26) 
        self.tableWidget.setRowHeight(11, 26) 
        
        conn = psycopg2.connect(
            dbname="Больница", 
            user="postgres", 
            password="2118", 
            host="localhost"
        )
        
        # Создаем объект курсора для выполнения SQL-запросов
        cur = conn.cursor()
        cur.execute("SELECT medical_report.code_doctor, doctor.lastname, doctor.firstname, doctor.middlename, position_doctor.name_of_position, medical_report.datemeet from medical_report  JOIN doctor ON  medical_report.code_doctor=doctor.code_doctor JOIN position_doctor ON position_doctor.id_position= doctor.id_position JOIN patient ON medical_report.patient_code= patient.patient_code WHERE patient.patient_code=%s",
                    (self.user_inf.codename_patient, ))
        
        self.tableWidget.setRowCount(0)  # Очистка таблицы
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))  # Установка количества строк в соответствии с результатами запроса
        for row_number, row_data in enumerate(rows):
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)
                
        self.tableWidget.setColumnWidth(4, 155)       
        cur.close()
        conn.close()
                
               

        self.retranslateUi(MedicalHistoryForm)
        QtCore.QMetaObject.connectSlotsByName(MedicalHistoryForm)

    def retranslateUi(self, AddAppointmentForm):
        _translate = QtCore.QCoreApplication.translate
        AddAppointmentForm.setWindowTitle(_translate("AddAppointmentForm", "История посещения"))
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddAppointmentForm = QtWidgets.QWidget()
    ui = Ui_MedicalHistoryForm()
    ui.setupUi(AddAppointmentForm)
    AddAppointmentForm.show()
    sys.exit(app.exec())