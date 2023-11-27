from PyQt6 import QtCore, QtGui, QtWidgets
from userstate import UserState
from PyQt6.QtWidgets import QMessageBox
from userstate import user_state
from login import Ui_LoginForm

class Ui_Dialog(object):
    
        
    def setupUi(self, Dialog):
        self.user_state = UserState()
        self.login=Ui_LoginForm()
        
        Dialog.setObjectName("Больница")
        Dialog.resize(604, 320)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 10, 521, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.servicesLabel = QtWidgets.QLabel(parent=self.widget)
        self.servicesLabel.setObjectName("servicesLabel")
        self.verticalLayout_2.addWidget(self.servicesLabel)
        self.addMeetingButton = QtWidgets.QPushButton(parent=self.widget)
        self.addMeetingButton.setObjectName("addMeetingButton")
        self.verticalLayout_2.addWidget(self.addMeetingButton)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ViewListButton = QtWidgets.QPushButton(parent=self.widget)
        self.ViewListButton.setObjectName("ViewListButton")
        self.verticalLayout.addWidget(self.ViewListButton)
        self.openCardButton = QtWidgets.QPushButton(parent=self.widget)
        self.openCardButton.setObjectName("openCardButton")
        self.verticalLayout.addWidget(self.openCardButton)
    
     
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.extrainformationLabel = QtWidgets.QLabel(parent=self.widget)
        self.extrainformationLabel.setObjectName("extrainformationLabel")
        self.verticalLayout_2.addWidget(self.extrainformationLabel)

        self.informationButton= QtWidgets.QPushButton(parent=Dialog)
        self.informationButton.setObjectName("informationButton")
        self.informationButton.setGeometry(QtCore.QRect(520, 5, 71, 25))
        
        self.loginButton = QtWidgets.QPushButton(parent=Dialog)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setGeometry(QtCore.QRect(270, 5, 88, 25))
       

        self.loginButton.clicked.connect(self.count_clicked)
        self.loginButton.clicked.connect(self.check_login)
             
        
         # Вызываем метод setupUi из Ui_LoginForm
        
       
        
        self.click_count = 0
        
        self.registerButton = QtWidgets.QPushButton(parent=Dialog)
        self.registerButton.setObjectName("registerButton")
        self.registerButton.setGeometry(QtCore.QRect(370, 5, 140, 25))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    
    def count_clicked(self):
        
        self.click_count += 1
        print(self.click_count)

    def check_login(self):
        print("form1 "+str(self.login.user_state.is_user_logged_in))
        
        if (self.login.user_state.is_user_logged_in and  self.click_count>1):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Вы вышли из системы!")
            msg.setWindowTitle("Success")
            self.login.user_state.logout()
            msg.exec()
        elif (self.login.user_state.is_user_logged_in):
            print("Вы в системе")
           
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Больница"))
        self.servicesLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#00557f;\">Сервисы</span></p></body></html>"))
        self.addMeetingButton.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#00557f;\">Записаться на приём</span></p></body></html>"))
        self.addMeetingButton.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.addMeetingButton.setText(_translate("Dialog", "Записаться на приём"))
        self.ViewListButton.setText(_translate("Dialog", "Список врачей"))
        self.openCardButton.setText(_translate("Dialog", "Открыть медицинскую карту"))
        self.extrainformationLabel.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.extrainformationLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#00557f;\">Контактная информация: +79183451234. </span></p><p align=\"center\"><span style=\" font-size:12pt; color:#00557f;\">Срочный вызов: +79886545678</span></p></body></html>"))
        self.loginButton.setText(_translate("Dialog", "Войти"))
        self.registerButton.setText(_translate("Dialog", "Зарегистрироваться"))
        self.informationButton.setText(_translate("Dialog", "Справка"))
        
        
        """ if self.login.user_state.is_user_logged_in:
            print("form1 кнопку менять должен"+str(self.login.user_state.is_user_logged_in))
            self.loginButton.setText("Выйти")
        else:
            self.loginButton.setText("Войти")
         """
        
            
