from PyQt6 import QtCore, QtGui, QtWidgets
import psycopg2
import random
from PyQt6.QtWidgets import QApplication, QMessageBox
import bcrypt
from docxtpl import DocxTemplate

class Ui_RegistrationForm(object):
    def setupUi(self, RegistrationForm):
        RegistrationForm.setObjectName("RegistrationForm")
        RegistrationForm.resize(380, 370)

        ###
        RegistrationForm.setStyleSheet(
    """
    QWidget {
        background-color: #f0f0f0;  /* Цвет фона */
    }
    QLabel {
        color: #00557f;  /* Основной цвет текста */
        font-size: 14px;  /* Размер шрифта */
    }
    QLineEdit, QDateEdit, QPushButton {
        background-color: #fff;  /* Цвет фона поля ввода и кнопки */
        border: 1px solid #aaa;  /* Обводка полей ввода и кнопки */
        padding: 5px;  /* Отступ вокруг текста в полях ввода и кнопке */
    }
    """
)

        ###
        self.label = QtWidgets.QLabel(RegistrationForm)
        self.label.setGeometry(QtCore.QRect(150, 10, 100, 35))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(RegistrationForm)  # Label for "Фамилия"
        self.label_2.setGeometry(QtCore.QRect(20, 50, 100, 35))
        self.label_2.setText("Фамилия")
        self.label_3 = QtWidgets.QLabel(RegistrationForm)  # Label for "Имя"
        self.label_3.setGeometry(QtCore.QRect(20, 95, 100, 35))
        self.label_3.setText("Имя")
        self.label_4 = QtWidgets.QLabel(RegistrationForm)  # Label for "Отчество"
        self.label_4.setGeometry(QtCore.QRect(20, 140, 100, 35))
        self.label_4.setText("Отчество")
        self.label_5 = QtWidgets.QLabel(RegistrationForm)  # Label for "День рождения"
        self.label_5.setGeometry(QtCore.QRect(20, 185, 100, 35))
        self.label_5.setText("День рождения")

        self.lastNameEdit = QtWidgets.QLineEdit(RegistrationForm)
        self.lastNameEdit.setGeometry(QtCore.QRect(160, 50, 175, 35))
        self.lastNameEdit.setObjectName("lastNameEdit")
        self.firstNameEdit = QtWidgets.QLineEdit(RegistrationForm)
        self.firstNameEdit.setGeometry(QtCore.QRect(160, 95, 175, 35))
        self.firstNameEdit.setObjectName("firstNameEdit")
        self.middleNameEdit = QtWidgets.QLineEdit(RegistrationForm)
        self.middleNameEdit.setGeometry(QtCore.QRect(160, 140, 175, 35))
        self.middleNameEdit.setObjectName("middleNameEdit")
        self.dobEdit = QtWidgets.QDateEdit(RegistrationForm)
        self.dobEdit.setGeometry(QtCore.QRect(160, 185, 175, 35))
        self.dobEdit.setObjectName("dobEdit")
        ########
        self.label_6 = QtWidgets.QLabel(RegistrationForm)  # Label for "Пароль"
        self.label_6.setGeometry(QtCore.QRect(20, 230, 175, 35))
        self.label_6.setText("Пароль")

        self.passwordEdit = QtWidgets.QLineEdit(RegistrationForm)
        self.passwordEdit.setGeometry(QtCore.QRect(160, 230, 175, 35))
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Скрыть ввод пароля
        self.passwordEdit.setObjectName("passwordEdit")

        self.label_7 = QtWidgets.QLabel(RegistrationForm)  # Label for "Повторите пароль"
        self.label_7.setGeometry(QtCore.QRect(20, 275, 175, 35))
        self.label_7.setText("Повторите пароль")

        self.confirmPasswordEdit = QtWidgets.QLineEdit(RegistrationForm)
        self.confirmPasswordEdit.setGeometry(QtCore.QRect(160, 275, 175, 35))
        self.confirmPasswordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Скрыть ввод повторного пароля
        self.confirmPasswordEdit.setObjectName("confirmPasswordEdit")

        self.registerButton = QtWidgets.QPushButton(RegistrationForm)
        self.registerButton.setGeometry(QtCore.QRect(10, 320, 355, 35))
        self.registerButton.setText("Зарегистрироваться")
        self.registerButton.clicked.connect(self.checkPassword)
        self.registerButton.clicked.connect(self.adddocx)

        self.retranslateUi(RegistrationForm)
        QtCore.QMetaObject.connectSlotsByName(RegistrationForm)

        self.retranslateUi(RegistrationForm)
        QtCore.QMetaObject.connectSlotsByName(RegistrationForm)


    def checkPassword(self):
        
        password = self.passwordEdit.text()
        confirmPassword = self.confirmPasswordEdit.text()

        
        if password == confirmPassword:
            
            print("Пароли совпадают. Регистрация успешна.")
            self.registerUserInDatabase()  # Вызываем метод для добавления пользователя в базу данных
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Пароли не совпадают. Пожалуйста, повторите ввод.")
            msg.setWindowTitle("Ошибка")
            msg.exec()
            print("Пароли не совпадают. Пожалуйста, повторите ввод.")


    def generate_patient_code(self,cur):
        while True:
            # Генерируем случайный код пациента
            patient_code = random.randint(1000, 9999)
            print(patient_code)

            # Проверяем, существует ли уже такой код в базе данных
            cur.execute("SELECT COUNT(*) FROM patient WHERE patient_code = %s", (patient_code,))
            count = cur.fetchone()[0]

            # Если код пациента не существует, используем его для вставки в базу данных
            if count == 0:
                return patient_code


    def registerUserInDatabase(self):
        
        # Получаем данные из формы
        lastName = self.lastNameEdit.text()
        firstName = self.firstNameEdit.text()
        middleName = self.middleNameEdit.text()
        dob = self.dobEdit.date().toString('yyyy-MM-dd')
        password = self.passwordEdit.text()

        # Проверяем, заполнены ли все поля
        if not lastName or not firstName or not middleName or not dob or not password:
            # Если какое-то из полей не заполнено, выдаем сообщение об ошибке
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Пожалуйста, заполните все поля")
            msg.setWindowTitle("Ошибка")
            msg.exec()
        else:
            # Если все поля заполнены, выполняем регистрацию в базе данных
            self.registerUserInDatabaseY()
            
    def registerUserInDatabaseY(self):
        
        # Подключаемся к базе данных
        conn = psycopg2.connect(
            dbname="Больница", 
            user="postgres", 
            password="2118", 
            host="localhost"
        )
        
        # Создаем объект курсора для выполнения SQL-запросов
        cur = conn.cursor()
        
        # Получаем данные из формы
        lastName = self.lastNameEdit.text()
        firstName = self.firstNameEdit.text()
        middleName = self.middleNameEdit.text()
        dob = self.dobEdit.date().toString('yyyy-MM-dd')
        password = self.passwordEdit.text()
        salt = bcrypt.gensalt()
        encoded_password = password.encode('utf-8')
        encoded_salt = salt

        hashed = bcrypt.hashpw(encoded_password, encoded_salt)
        # сгенерированный код пациента 
        patient_code = self.generate_patient_code(cur)

        print(f"{lastName}\n{firstName}\n{middleName}\n{dob}\n{patient_code}")

        # Преобразуем хеш пароля в строку шестнадцатеричного представления
        hashed_str = hashed.decode('utf-8')  # Преобразуем байтовый хеш в строку
        # Выполняем SQL-запрос для вставки данных в таблицу "Пациент"
        cur.execute("INSERT INTO patient  VALUES (%s, %s, %s, %s, %s, %s)", 
            (patient_code, lastName, firstName, middleName, dob, hashed_str))
        # Подтверждаем выполнение SQL-запроса
        conn.commit()

        # Закрываем соединение с базой данных
        cur.close()
        conn.close()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(f"Вы успешно зарегистрированы! Ваш код {patient_code}")
        msg.setWindowTitle("Регистрация")
        msg.exec()

    def adddocx(self):
        doc=DocxTemplate(r'C:\Users\Alice\Desktop\Hospital\myproject\Views\user_register.docx')
        context={'lastname':self.lastNameEdit.text(),
                 'firstname':self.firstNameEdit.text(),
                 'middlename':self.middleNameEdit.text(),
                 'birthday':self.dobEdit.text(),
                 'password':self.passwordEdit.text() }
        doc.render(context)
        doc.save("register.docx")
        
    def retranslateUi(self, RegistrationForm):
        _translate = QtCore.QCoreApplication.translate
        RegistrationForm.setWindowTitle(_translate("RegistrationForm", "Регистрация"))
        self.label.setText(_translate("RegistrationForm", "Регистрация"))
        self.registerButton.setStyleSheet(
    """
    background-color: #00557f;  /* Цвет фона кнопки */
    border: none;  /* Удаление границы кнопки */
    color: white;  /* Цвет текста кнопки */
    """
)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrationForm = QtWidgets.QWidget()
    ui = Ui_RegistrationForm()
    ui.setupUi(RegistrationForm)
    RegistrationForm.show()
    sys.exit(app.exec())
