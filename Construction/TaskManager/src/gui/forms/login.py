# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(311, 381)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 311, 381))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 23, 1, 1, 1)

        self.passwordEdit = QLineEdit(self.gridLayoutWidget)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.passwordEdit, 14, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 17, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 15, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 11, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 13, 1, 1, 1)

        self.tappLabel = QLabel(self.gridLayoutWidget)
        self.tappLabel.setObjectName(u"tappLabel")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(28)
        font.setBold(False)
        self.tappLabel.setFont(font)
        self.tappLabel.setTextFormat(Qt.TextFormat.AutoText)
        self.tappLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.tappLabel, 1, 1, 1, 1)

        self.usernameEdit = QLineEdit(self.gridLayoutWidget)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.gridLayout.addWidget(self.usernameEdit, 10, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 2, 1, 1, 1)

        self.passwordLabel = QLabel(self.gridLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        self.passwordLabel.setFont(font1)

        self.gridLayout.addWidget(self.passwordLabel, 12, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.remember_check = QCheckBox(self.gridLayoutWidget)
        self.remember_check.setObjectName(u"remember_check")

        self.gridLayout.addWidget(self.remember_check, 16, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 10, 2, 1, 1)

        self.loginButton = QPushButton(self.gridLayoutWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setFont(font1)

        self.gridLayout.addWidget(self.loginButton, 19, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.usernameLabel = QLabel(self.gridLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setFont(font1)

        self.horizontalLayout_3.addWidget(self.usernameLabel, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 9, 1, 1, 1)

        self.register_button = QPushButton(self.gridLayoutWidget)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setFont(font1)

        self.gridLayout.addWidget(self.register_button, 22, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 20, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tappLabel.setText(QCoreApplication.translate("Dialog", u"Tapp", None))
        self.usernameEdit.setInputMask("")
        self.passwordLabel.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.remember_check.setText(QCoreApplication.translate("Dialog", u"Recordarme", None))
        self.loginButton.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.usernameLabel.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.register_button.setText(QCoreApplication.translate("Dialog", u"Registrar", None))
    # retranslateUi

