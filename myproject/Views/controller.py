from form1 import Ui_Dialog
from register import Ui_RegistrationForm
from login import Ui_LoginForm
from registermeet import Ui_RegisterMeetForm
from listofdoctors import Ui_ListOfDoctorsForm
from medical_report import Ui_MedicalReportForm
from extrainformation import Ui_InformationForm
from userstate import UserState


from PyQt6 import QtWidgets

class UiFunctions(QtWidgets.QMainWindow, Ui_Dialog):
    #прописаны события кнопок
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registerButton.clicked.connect(self.openRegistration)
        self.loginButton.clicked.connect(self.openLogin)
        self.addMeetingButton.clicked.connect(self.openRegisterMeet)
        self.ViewListButton.clicked.connect(self.openListOfDoctors)
        self.openCardButton.clicked.connect(self.openMedicalReport)
        self.informationButton.clicked.connect(self.openextrainformation)
        
        self.user_state = UserState()
        self.login=Ui_LoginForm()
        

    # функции для кнопок
    def openRegistration(self):
        self.registrationForm = QtWidgets.QWidget()
        self.ui = Ui_RegistrationForm()
        self.ui.setupUi(self.registrationForm)
        self.registrationForm.show()

    def openLogin(self):
        self.loginForm = QtWidgets.QWidget()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self.loginForm)
        self.loginForm.show()

    def openRegisterMeet(self):
        self.registermeetForm = QtWidgets.QWidget()
        self.ui = Ui_RegisterMeetForm()
        self.ui.setupUi(self.registermeetForm)
        self.registermeetForm.show()

    def openListOfDoctors(self):
        self.listofdoctorsForm = QtWidgets.QWidget()
        self.ui = Ui_ListOfDoctorsForm()
        self.ui.setupUi(self.listofdoctorsForm)
        self.listofdoctorsForm.show()

    def openMedicalReport(self):
        
        self.MedicalReportForm = QtWidgets.QWidget()
        self.ui = Ui_MedicalReportForm()
        print("controller"+str(self.login.user_state.is_user_logged_in))
        if  not(self.login.user_state.is_user_logged_in):
            print("Функция в контроллере ")
            self.loginForm = QtWidgets.QWidget()
            self.ui_login = Ui_LoginForm()
            self.ui_login.setupUi(self.loginForm)
            self.loginForm.show()
        else:
            self.ui.setupUi(self.MedicalReportForm)
            self.MedicalReportForm.show()
    
    def openextrainformation(self):
        self.loginForm = QtWidgets.QWidget()
        self.ui = Ui_InformationForm()
        self.ui.setupUi(self.loginForm)
        self.loginForm.show()
        
   
        
