from PyQt6 import QtCore, QtGui, QtWidgets
from userstate import UserState
from userstate import user_state
from login import Ui_LoginForm
from medicalhistory import Ui_MedicalHistoryForm
from registermeet import Ui_RegisterMeetForm
from PyQt6.QtWidgets import QMessageBox
from user import user_inf
import psycopg2
from datetime import datetime

class Ui_MedicalReportForm(object):
    def __init__(self):
        self.user_state = user_state
        self.user_inf = user_inf
    def setupUi(self, MedicalReportForm):
        self.user_state = UserState()
        self.login=Ui_LoginForm()
        
        MedicalReportForm.setObjectName("Медицинская карта")
        MedicalReportForm.resize(510, 400)

        MedicalReportForm.setStyleSheet(
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


        self.widget = QtWidgets.QWidget(parent=MedicalReportForm)
        self.widget.setGeometry(QtCore.QRect(40, 10, 300, 200))  

        # Добавление заголовка
        self.titleLabel = QtWidgets.QLabel(parent=MedicalReportForm)
        self.titleLabel.setGeometry(QtCore.QRect(20, 10, 250, 30))
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("<html><head/><body><p align=\"left\"><span style=\" font-size:14pt; color:#00557f;\">Личный кабинет</span></p></body></html>")


        self.registermeetButton = QtWidgets.QPushButton(MedicalReportForm)
        self.registermeetButton.setGeometry(QtCore.QRect(200, 10, 210, 28))
        self.registermeetButton.setText("Записаться на приём")
        self.registermeetButton.clicked.connect(self.open_register_meet)

        self.logoutButton = QtWidgets.QPushButton(MedicalReportForm)
        self.logoutButton.setGeometry(QtCore.QRect(420, 10, 70, 28))
        self.logoutButton.setText("Выйти")
        self.logoutButton.clicked.connect(self.close_window_logout_user)

 # Личные данные пациента
        self.label_patientcode = QtWidgets.QLabel(MedicalReportForm)  
        self.label_patientcode.setGeometry(QtCore.QRect(20, 50, 100, 35))
        self.label_patientcode.setText("Код пациента")

        self.label_doctorcode = QtWidgets.QLabel(MedicalReportForm) 
        self.label_doctorcode.setGeometry(QtCore.QRect(20, 95, 100, 35))
        self.label_doctorcode.setText("Код врача")

        self.label_patientlastname = QtWidgets.QLabel(MedicalReportForm) 
        self.label_patientlastname.setGeometry(QtCore.QRect(20, 140, 105, 35))
        self.label_patientlastname.setText("Фамилия пациента")

        self.label_doctorlastname = QtWidgets.QLabel(MedicalReportForm) 
        self.label_doctorlastname.setGeometry(QtCore.QRect(20, 185, 100, 35))
        self.label_doctorlastname.setText("Фамилия врача")


        self.label_datemeet = QtWidgets.QLabel(MedicalReportForm) 
        self.label_datemeet.setGeometry(QtCore.QRect(20, 230, 100, 35))
        self.label_datemeet.setText("Дата посещения")

        self.label_disease = QtWidgets.QLabel(MedicalReportForm)  
        self.label_disease.setGeometry(QtCore.QRect(20, 275, 100, 35))
        self.label_disease.setText("Диагноз")

        self.label_patientanalysis = QtWidgets.QLabel(MedicalReportForm)  
        self.label_patientanalysis.setGeometry(QtCore.QRect(20, 320, 130, 35))
        self.label_patientanalysis.setText("Код анализов пациента")

       
      
        self.patientcodeEdit = QtWidgets.QLineEdit(MedicalReportForm)
        self.patientcodeEdit.setGeometry(QtCore.QRect(200, 50, 290, 35))
        self.patientcodeEdit.setObjectName("patientcodeEdit")

        self.doctorcodeEdit = QtWidgets.QLineEdit(MedicalReportForm)
        self.doctorcodeEdit.setGeometry(QtCore.QRect(200, 95, 290, 35))
        self.doctorcodeEdit.setObjectName("doctorcodeEdit")

        self.patientlastnameEdit = QtWidgets.QLineEdit(MedicalReportForm)
        self.patientlastnameEdit.setGeometry(QtCore.QRect(200, 140, 290, 35))
        self.patientlastnameEdit.setObjectName("patientlastnameEdit")

        self.doctorlastnameEdit = QtWidgets.QLineEdit(MedicalReportForm)
        self.doctorlastnameEdit.setGeometry(QtCore.QRect(200, 185, 290, 35))
        self.doctorlastnameEdit.setObjectName("doctorlastnameEdit")

        self.datemeetEdit = QtWidgets.QLineEdit(MedicalReportForm)
        self.datemeetEdit.setGeometry(QtCore.QRect(200, 230, 290, 35))
        self.datemeetEdit.setObjectName("datemeetEdit")

        self.diseaseEdit = QtWidgets.QLineEdit(MedicalReportForm)
        self.diseaseEdit.setGeometry(QtCore.QRect(200, 275, 290, 35))
        self.diseaseEdit.setObjectName("diseaseEdit")

        self.patientanalysisEdit = QtWidgets.QLineEdit(MedicalReportForm)
        self.patientanalysisEdit.setGeometry(QtCore.QRect(200, 320, 290, 35))
        self.patientanalysisEdit.setObjectName("patientanalysisEdit")

        
        # Ваша история посещений

        self.registermeetButton = QtWidgets.QPushButton(MedicalReportForm)
        self.registermeetButton.setGeometry(QtCore.QRect(20, 365, 250, 28))
        self.registermeetButton.setText("Смотреть свою медицинскую историю")
        self.registermeetButton.clicked.connect(self.open_history_visits)

       
        print(self.user_inf.lastname_patient)
        
        
        #Вставляем информацию о пациенте
        self.patientcodeEdit.setText(self.user_inf.codename_patient)
        self.patientlastnameEdit.setText(self.user_inf.lastname_patient)
        
        conn = psycopg2.connect(
            dbname="Больница", 
            user="postgres", 
            password="2118", 
            host="localhost"
        )
        
        # Создаем объект курсора для выполнения SQL-запросов
        cur = conn.cursor()
        cur.execute("SELECT medical_report.patient_code, medical_report.code_doctor, patient.lastname, doctor.lastname, medical_report.datemeet FROM medical_report JOIN patient ON medical_report.patient_code = patient.patient_code JOIN doctor ON medical_report.code_doctor = doctor.code_doctor WHERE medical_report.patient_code = %s AND patient.lastname = %s",
                    (self.user_inf.codename_patient, self.user_inf.lastname_patient))
        
        medical_cart=cur.fetchone()
        print(f"medical cart {medical_cart}")
        
        print(type(medical_cart))
        print((medical_cart[0]))
        
        
        self.patientcodeEdit.setText(str(medical_cart[0]))
        self.doctorcodeEdit.setText(str(medical_cart[1]))
        self.patientlastnameEdit.setText(medical_cart[2])
        self.doctorlastnameEdit.setText(medical_cart[3])
        self.datemeetEdit.setText((medical_cart[4].strftime('%H:%M')))
        
        print(self.user_inf.codename_patient)
        print(type(self.user_inf.codename_patient))
        cur.execute("SELECT disease.name_of_disease FROM disease JOIN  patient_disease ON patient_disease.code_disease=disease.code_disease WHERE  patient_disease.code_patient= %s",
                    (self.user_inf.codename_patient, ))
        
        disease=cur.fetchone()[0]
        print(disease)
        self.diseaseEdit.setText(disease)
        
        cur.execute("SELECT code_analysis FROM analysis WHERE analysis.code_patient= %s",(self.user_inf.codename_patient, ))
        code_analysis=cur.fetchone()[0]
        print(code_analysis)
        self.patientanalysisEdit.setText(str(code_analysis))
        
        cur.close()
        conn.close()

        self.retranslateUi(MedicalReportForm)
        QtCore.QMetaObject.connectSlotsByName(MedicalReportForm)

    def retranslateUi(self, AddAppointmentForm):
        _translate = QtCore.QCoreApplication.translate
        AddAppointmentForm.setWindowTitle(_translate("AddAppointmentForm", "Личный кабинет. Медицинская карта пациента"))
        
    def close_window_logout_user(self):
        self.login.user_state.logout()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Вы вышли из системы!")
        msg.setWindowTitle("Success")
        msg.exec()
        print(self.login.user_state.is_user_logged_in)
             
        
    def open_history_visits(self):
        self.MedicalHistoryForm = QtWidgets.QWidget()
        self.ui = Ui_MedicalHistoryForm()
        self.ui.setupUi(self.MedicalHistoryForm)
        self.MedicalHistoryForm.show()
        
    def open_register_meet(self):
        self.RegisterMeetForm = QtWidgets.QWidget()
        self.ui = Ui_RegisterMeetForm()
        self.ui.setupUi(self.RegisterMeetForm)
        self.RegisterMeetForm.show()
          

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddAppointmentForm = QtWidgets.QWidget()
    ui = Ui_MedicalReportForm()
    ui.setupUi(AddAppointmentForm)
    AddAppointmentForm.show()
    sys.exit(app.exec())
