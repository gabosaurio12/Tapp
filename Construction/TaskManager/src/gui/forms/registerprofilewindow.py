# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerprofilewindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(397, 330)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 80, 341, 217))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.register_button = QPushButton(self.gridLayoutWidget)
        self.register_button.setObjectName(u"register_button")

        self.horizontalLayout.addWidget(self.register_button)

        self.cancel_button = QPushButton(self.gridLayoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 1, 1, 1)

        self.password_edit = QLineEdit(self.gridLayoutWidget)
        self.password_edit.setObjectName(u"password_edit")

        self.gridLayout.addWidget(self.password_edit, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 1, 1, 1)

        self.name_edit = QLineEdit(self.gridLayoutWidget)
        self.name_edit.setObjectName(u"name_edit")

        self.gridLayout.addWidget(self.name_edit, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.username_edit = QLineEdit(self.gridLayoutWidget)
        self.username_edit.setObjectName(u"username_edit")

        self.gridLayout.addWidget(self.username_edit, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 20, 111, 41))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(28)
        font.setBold(False)
        self.label_4.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.register_button.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Usuario", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Registro", None))
    # retranslateUi

