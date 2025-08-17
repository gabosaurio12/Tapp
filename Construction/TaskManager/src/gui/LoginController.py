from PySide6.QtWidgets import *
from gui.forms.login import Ui_Dialog
from gui.MainPageController import MainPageController
from gui.RegisterProfileController import RegisterProfileController

from bussinesslogic.profile.ProfileDAOImplementation import ProfileDAOImplementation

class LoginController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.login)
        self.ui.register_button.clicked.connect(self.register)

    def login(self):
        username = self.ui.usernameEdit.text()
        password = self.ui.passwordEdit.text()

        dao = ProfileDAOImplementation()
        profile = dao.read_profile_by_username(username)
        if profile.username == username:
            if password == profile.password:
                if (self.ui.remember_check.isChecked()):
                    self.save_current_profile(profile)
                self.main_window = MainPageController(profile)
                self.main_window.show()
                self.close()
            else:
                QMessageBox.information(self, "Login", "Wrong password")
        else:
            QMessageBox.critical(self, "Login", "Unregistered username")

    def save_current_profile(self, profile):
        dao = ProfileDAOImplementation()
        dao.update_current_profile(profile.id_profile)

    def register(self):
        self.register_profile_window = RegisterProfileController()
        self.register_profile_window.show()