from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import psycopg2
import bcrypt
from userstate import user_state
from user import user_inf
from docxtpl import DocxTemplate

class Ui_LoginForm(object):
    def __init__(self):
        self.user_state = user_state
        self.user_inf=user_inf
        self.login=False
        
        
    
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(380, 285)
        
       
        ###
        LoginForm.setStyleSheet(
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
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setGeometry(QtCore.QRect(150, 10, 100, 35))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LoginForm)  # Label for "Фамилия"
        self.label_2.setGeometry(QtCore.QRect(20, 50, 100, 35))
        self.label_2.setText("Фамилия")
        self.label_3 = QtWidgets.QLabel(LoginForm)  # Label for "Имя"
        self.label_3.setGeometry(QtCore.QRect(20, 95, 100, 35))
        self.label_3.setText("Имя")
        self.label_4 = QtWidgets.QLabel(LoginForm)  # Label for "Отчество"
        self.label_4.setGeometry(QtCore.QRect(20, 140, 100, 35))
        self.label_4.setText("Ваш код")
        self.label_5 = QtWidgets.QLabel(LoginForm)  # Label for "Пароль"
        self.label_5.setGeometry(QtCore.QRect(20, 185, 100, 35))
        self.label_5.setText("Пароль")

        self.lastNameEdit = QtWidgets.QLineEdit(LoginForm)
        self.lastNameEdit.setGeometry(QtCore.QRect(160, 50, 175, 35))
        self.lastNameEdit.setObjectName("lastNameEdit")
        self.firstNameEdit = QtWidgets.QLineEdit(LoginForm)
        self.firstNameEdit.setGeometry(QtCore.QRect(160, 95, 175, 35))
        self.firstNameEdit.setObjectName("firstNameEdit")
        self.codeEdit = QtWidgets.QLineEdit(LoginForm)
        self.codeEdit.setGeometry(QtCore.QRect(160, 140, 175, 35))
        self.codeEdit.setObjectName("CodeEdit")

        self.passwordEdit = QtWidgets.QLineEdit(LoginForm)
        self.passwordEdit.setGeometry(QtCore.QRect(160, 185, 175, 35))
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Скрыть ввод пароля
        self.passwordEdit.setObjectName("passwordEdit")

        self.LoginButton2 = QtWidgets.QPushButton(LoginForm)
        self.LoginButton2.setGeometry(QtCore.QRect(10, 230, 355, 35))
        self.LoginButton2.setText("Войти")
        self.LoginButton2.clicked.connect(self.checkuserindatabase)
        self.LoginButton2.clicked.connect(self.adddocx)
       
        
       

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)
        
        
        
    def checkuserindatabase(self):
        # Получаем данные из формы
        lastName = self.lastNameEdit.text()
        firstName = self.firstNameEdit.text()
        codeName = self.codeEdit.text()
        password = self.passwordEdit.text()

        # Проверяем, заполнены ли все поля
        if not lastName or not firstName or not codeName  or not password:
            # Если какое-то из полей не заполнено, выдаем сообщение об ошибке
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Пожалуйста, заполните все поля")
            msg.setWindowTitle("Ошибка")
            msg.exec()
        else:
            # Если все поля заполнены, выполняем регистрацию в базе данных
            self.checkuserindatabaseY()
        
    
        
    def checkuserindatabaseY(self):
        lastname = self.lastNameEdit.text() 
        firstname = self.firstNameEdit.text()  # Получаем введенное имя пользователя
        codename = self.codeEdit.text()
        passwordedit = self.passwordEdit.text()  # Получаем введенный пароль
        # Проверка пароля
        
            
        
        # Подключаемся к базе данных
        conn = psycopg2.connect(
            dbname="Больница", 
            user="postgres", 
            password="2118", 
            host="localhost"
        )
        
        # Создаем объект курсора для выполнения SQL-запросов
        cur = conn.cursor()
       
        cur.execute("SELECT  password  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s",
                 (lastname, firstname, codename,))
        password=cur.fetchone()[0]
        

        cur.execute("SELECT lastname, firstname, patient_code  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s ",
                 (lastname, firstname, codename ))
        

        user = cur.fetchone()
        
        password_check=passwordedit.encode(encoding='utf-8')
        password_hash= str(password).encode(encoding='utf-8')
     
        if user and bcrypt.checkpw(password_check, password_hash):
          
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Вы вошли в систему!")
            msg.setWindowTitle("Success")
            msg.exec()
            print("login.py"+ str(self.user_state.is_user_logged_in))
            self.user_state.login()
            print("login.py"+ str(self.user_state.is_user_logged_in))
            
            self.user_inf.lastname_patient=lastname
            self.user_inf.firstname_patient=firstname
            self.user_inf.codename_patient=codename
            self.user_inf.passwordedit=passwordedit
            
            print(self.user_inf.codename_patient)
            print(self.user_inf.lastname_patient)
          
            self.login=True
            
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Неправильное имя пользователя или пароль!")
            msg.setWindowTitle("Ошибка")
            msg.exec()
           
        cur.close()
        conn.close()
        
    def adddocx(self):
        doc=DocxTemplate(r'C:\Users\Alice\Desktop\Hospital\myproject\Views\user_state_template.docx')
        context={'user_state':self.user_state.is_user_logged_in,
                 'code_patient':self.user_inf.codename_patient,
                 'lastname':self.user_inf.lastname_patient,
                 'firstname':self.user_inf.firstname_patient,
                 'password':self.user_inf.passwordedit}
        doc.render(context)
        doc.save("login.docx")
        

    
    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.label.setText(_translate("LoginForm", "Вход в аккаунт"))
        self.LoginButton2.setStyleSheet(
    """
    background-color: #00557f;  /* Цвет фона кнопки */
    border: none;  /* Удаление границы кнопки */
    color: white;  /* Цвет текста кнопки */
    """
)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec())
