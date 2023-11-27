from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt6.QtCore import QObject
import psycopg2
from PyQt6.QtWidgets import QApplication, QMessageBox
from userstate import user_state
from login import Ui_LoginForm
from userstate import UserState
from user import user_inf
from docxtpl import DocxTemplate

class Ui_RegisterMeetForm(object):
    def __init__(self):
        self.user_inf=user_inf
        self.user_state = user_state
        
    def setupUi(self, RegisterMeetForm):
        
        self.user_state = UserState()
        self.login=Ui_LoginForm()
        
        RegisterMeetForm.setObjectName("Добавить запись")
        RegisterMeetForm.resize(660, 400)

        RegisterMeetForm.setStyleSheet(
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


        self.widget = QtWidgets.QWidget(parent=RegisterMeetForm)
        self.widget.setGeometry(QtCore.QRect(40, 10, 300, 200))  

        # Добавление заголовка
        self.titleLabel = QtWidgets.QLabel(parent=RegisterMeetForm)
        self.titleLabel.setGeometry(QtCore.QRect(200, 10, 250, 30))
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#00557f;\">Записаться на прием</span></p></body></html>")

        self.tableWidget = QtWidgets.QTableWidget(6, 2, parent=RegisterMeetForm)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 360, 340))
        self.tableWidget.setObjectName("tableWidget")
        # Добавление заголовков столбцов
        self.tableWidget.setHorizontalHeaderLabels(["Врач", "Информация"])

        # Растянуть второй столбец на оставшуюся таблицу
        # Растянуть второй столбец на оставшуюся таблицу
       
        # Установить размер столбца 0
        self.tableWidget.setColumnWidth(0, 100)  # Устанавливает ширину столбца 0 равной 100 пикселям
        self.tableWidget.setColumnWidth(1, 243)  # Устанавливает ширину столбца 0 равной 100 пикселям
      
        # Установить высоту строки 0
        self.tableWidget.setRowHeight(0, 100) 
        self.tableWidget.setRowHeight(1, 100)  # Устанавливает высоту строки 0 равной 100 пикселям
        self.tableWidget.setRowHeight(2, 100) 
        self.tableWidget.setRowHeight(3, 100) 
        self.tableWidget.setRowHeight(4, 100)
        self.tableWidget.setRowHeight(5, 100) 


        

        doctorButton = QtWidgets.QPushButton("Кардиолог", self.tableWidget)
        self.tableWidget.setCellWidget(0, 0, doctorButton)
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("-Боль в сердце\n-Одышка\n-Аритмия\n-Отечность\n-Обмороки"))


  
      
        # Заполнение таблицы
        
        doctorButton1 = QtWidgets.QPushButton("Невролог", self.tableWidget)
        self.tableWidget.setCellWidget(1, 0, doctorButton1)
        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem("-Внезапные головные боли\n-Обмороки\n-Головокружения\n-Бессоница\n-Ухудшение памяти"))

        doctorButton2 = QtWidgets.QPushButton("Онколог", self.tableWidget)
        self.tableWidget.setCellWidget(2, 0, doctorButton2)
        self.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem("-Резкое ухудшение  самочувствия\n-Слабость\n-Снижение аппетита\n-Тошнота\n-Сдавливание в горле"))

        doctorButton3 = QtWidgets.QPushButton("Ревматолог", self.tableWidget)
        self.tableWidget.setCellWidget(3, 0, doctorButton3)
        self.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem("-Боли в области сустовов\n-Боли в мышцах\n-Кожные высыпания\n-Длительное повышение температуры"))

        doctorButton4 = QtWidgets.QPushButton("Хирург", self.tableWidget)
        self.tableWidget.setCellWidget(4, 0, doctorButton4)
        self.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem("-Гнойники\n-Язвы на теле\n-Сильные порезы\n-Наросты\n-Боли в позвоночнике, теле"))

        doctorButton5 = QtWidgets.QPushButton("Терапевт", self.tableWidget)
        self.tableWidget.setCellWidget(5, 0, doctorButton5)
        self.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem("-Изменения артериального давления\n-Общая слабость\n-Шелушение\n-Чувство тревожности\n-Сухости во рту"))


         # события для кнопок
        doctorButton.clicked.connect(lambda: self.handleDoctorButtonClicked(doctorButton))
        doctorButton1.clicked.connect(lambda: self.handleDoctorButtonClicked(doctorButton1))
        doctorButton2.clicked.connect(lambda: self.handleDoctorButtonClicked(doctorButton2))
        doctorButton3.clicked.connect(lambda: self.handleDoctorButtonClicked(doctorButton3))
        doctorButton4.clicked.connect(lambda: self.handleDoctorButtonClicked(doctorButton4))
        doctorButton5.clicked.connect(lambda: self.handleDoctorButtonClicked(doctorButton5))

        # форма. заполнение формочки
       
        self.label_2 = QtWidgets.QLabel(RegisterMeetForm)  # Label for "Фамилия"
        self.label_2.setGeometry(QtCore.QRect(365, 50, 100, 35))
        self.label_2.setText("Фамилия")
        self.label_3 = QtWidgets.QLabel(RegisterMeetForm)  # Label for "Имя"
        self.label_3.setGeometry(QtCore.QRect(365, 95, 100, 35))
        self.label_3.setText("Имя")
        self.label_4 = QtWidgets.QLabel(RegisterMeetForm)  # Label for "Номер телефона"
        self.label_4.setGeometry(QtCore.QRect(365, 140, 100, 35))
        self.label_4.setText("Номер телефона")

        self.label_5 = QtWidgets.QLabel(RegisterMeetForm)  # Label for "Врач"
        self.label_5.setGeometry(QtCore.QRect(365, 185, 100, 35))
        self.label_5.setText("Выберите врача")


        self.lastNameEdit = QtWidgets.QLineEdit(RegisterMeetForm)
        self.lastNameEdit.setGeometry(QtCore.QRect(460, 50, 175, 25))
        self.lastNameEdit.setObjectName("lastNameEdit")
        self.firstNameEdit = QtWidgets.QLineEdit(RegisterMeetForm)
        self.firstNameEdit.setGeometry(QtCore.QRect(460, 95, 175, 25))
        self.firstNameEdit.setObjectName("firstNameEdit")
        self.telephone_number = QtWidgets.QLineEdit(RegisterMeetForm)
        self.telephone_number.setGeometry(QtCore.QRect(460, 140, 175, 25))
        self.telephone_number.setObjectName("telephone_number")

        self.doctoredit = QtWidgets.QLineEdit(RegisterMeetForm)
        self.doctoredit.setGeometry(QtCore.QRect(460, 185, 175, 25))
        self.doctoredit.setObjectName("doctor")
        
        print("registermeet"+str(self.login.user_state.is_user_logged_in))
        #если пациент зарегестрирован и зашел в систему, то автоматически заполнять поля
        if self.login.user_state.is_user_logged_in:
            self.lastNameEdit.setText(self.user_inf.lastname_patient)
            self.firstNameEdit.setText(self.user_inf.firstname_patient)
        else:
            pass
            
            
        #кнопка для формы
        self.registermeetButton = QtWidgets.QPushButton(RegisterMeetForm)
        self.registermeetButton.setGeometry(QtCore.QRect(365, 230, 270, 25))
        self.registermeetButton.setText("Записаться на приём")
        self.registermeetButton.clicked.connect(self.addusertourgentappoointments)
        self.registermeetButton.clicked.connect(self.adddocx)

        self.retranslateUi(RegisterMeetForm)
        QtCore.QMetaObject.connectSlotsByName(RegisterMeetForm)
        
    def adddocx(self):
        doc=DocxTemplate(r'C:\Users\Alice\Desktop\Hospital\myproject\Views\user_registermeet.docx')
        context={'lastname':self.lastNameEdit.text(), 'firstname':self.firstNameEdit.text(),
                 'telephone_number':self.telephone_number.text(),
                 'doctor':self.doctoredit.text()}
        doc.render(context)
        doc.save("registermeet.docx")
        
    def addusertourgentappoointments(self):
    # Получаем данные из формы
        lastName = self.lastNameEdit.text()
        firstName = self.firstNameEdit.text()
        telephone_number = self.telephone_number.text()
        doctoredit = self.doctoredit.text()
       

        # Проверяем, заполнены ли все поля
        if not lastName or not firstName or not telephone_number or not doctoredit:
            # Если какое-то из полей не заполнено, выдаем сообщение об ошибке
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Пожалуйста, заполните все поля")
            msg.setWindowTitle("Ошибка")
            msg.exec()
        else:
            # Если все поля заполнены, выполняем регистрацию в базе данных
            self.addusertourgentappoointmentsY()
            
    def addusertourgentappoointmentsY(self):
            lastname=self.lastNameEdit.text()
            firstname=self.firstNameEdit.text()
            telephone_number=self.telephone_number.text() 
            doctor=self.doctoredit.text()  
            # Проверка на нулевые значения
            if not lastname or not firstname or not telephone_number or not doctor:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Пожалуйста, заполните все поля")
                msg.setWindowTitle("Ошибка")
                msg.exec()
                return
            # Подключаемся к базе данных
            conn = psycopg2.connect(
                dbname="Больница", 
                user="postgres", 
                password="2118", 
                host="localhost"
            )
            cur=conn.cursor()
            
            cur.execute("INSERT INTO urgent_appointments  VALUES (%s, %s , %s , %s)", (lastname, firstname,telephone_number, doctor))
            conn.commit()
            if cur.rowcount > 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setText("Вы записаны! Ожидайте звонка для точного времени приема")
                msg.setWindowTitle("Регистрация")
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Не удалось записаться на прием")
                msg.setWindowTitle("Ошибка")
                msg.exec()
                
            cur.close()
            conn.close()
           
            

    def handleDoctorButtonClicked(self, button:QtWidgets.QPushButton):
        text = button.text()  # получаем текст данной кнопки
        self.doctoredit.setText(text)

    def retranslateUi(self, AddAppointmentForm):
        _translate = QtCore.QCoreApplication.translate
        AddAppointmentForm.setWindowTitle(_translate("AddAppointmentForm", "Добавить запись"))
        self.registermeetButton.setStyleSheet(
    """
    background-color: #00557f;  /* Цвет фона кнопки */
    border: none;  /* Удаление границы кнопки */
    color: white;  /* Цвет текста кнопки */
    """
)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddAppointmentForm = QtWidgets.QWidget()
    ui = Ui_RegisterMeetForm()
    ui.setupUi(AddAppointmentForm)
    AddAppointmentForm.show()
    sys.exit(app.exec())

