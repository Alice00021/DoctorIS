from PyQt6 import QtWidgets
from form1 import Ui_Dialog
from controller import UiFunctions


app = QtWidgets.QApplication([])
main_window = QtWidgets.QMainWindow()

ui = Ui_Dialog()
ui.setupUi(main_window)
ui.retranslateUi(main_window)

ui_functions = UiFunctions()

ui.registerButton.clicked.connect(ui_functions.openRegistration)  # Подключаем событие для кнопки регистрации
ui.loginButton.clicked.connect(ui_functions.openLogin)  # Подключаем событие для кнопки входа
ui.addMeetingButton.clicked.connect(ui_functions.openRegisterMeet)  # Подключаем событие для кнопки "Записаться на прием"
ui.ViewListButton.clicked.connect(ui_functions.openListOfDoctors)
ui.openCardButton.clicked.connect(ui_functions.openMedicalReport)
ui.informationButton.clicked.connect(ui_functions.openextrainformation)




main_window.show()
app.exec()


