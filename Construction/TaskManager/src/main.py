import sys
import os
from PySide6.QtWidgets import QApplication
from gui.LoginController import LoginController
from gui.MainPageController import MainPageController
from bussinesslogic.profile.ProfileDAOImplementation import ProfileDAOImplementation

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dao = ProfileDAOImplementation()
    id_profile = dao.read_current_profile()
    if (id_profile == 0):
        loginWindow = LoginController()
        loginWindow.show()
    else:
        profile = dao.read_profile_by_id(id_profile)
        main_window = MainPageController(profile)
        main_window.show()
    sys.exit(app.exec())