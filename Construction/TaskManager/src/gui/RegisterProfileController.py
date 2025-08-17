from PySide6.QtWidgets import *
from gui.forms.registerprofilewindow import Ui_Form
from bussinesslogic.profile.ProfileDAOImplementation import ProfileDAOImplementation
from model.Profile import Profile

class RegisterProfileController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.register_button.clicked.connect(self.add_profile)
        self.ui.cancel_button.clicked.connect(self.close_window)


    def close_window(self):
        self.close()

    def get_info(self):
        profile = Profile()
        profile.name = self.ui.name_edit.text()
        profile.username = self.ui.username_edit.text()
        profile.password = self.ui.password_edit.text()
        
        return profile

    def add_profile(self):
        profile = self.get_info()
        dao = ProfileDAOImplementation()
        profile_dict = profile.to_clean_dict()
        profile_dict.pop('id_profile', None)
        dao.insert_profile(profile_dict)
        self.close_window()