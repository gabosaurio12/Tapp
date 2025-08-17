# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(553, 403)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 551, 401))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.buttons_grid = QVBoxLayout()
        self.buttons_grid.setObjectName(u"buttons_grid")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttons_grid.addItem(self.verticalSpacer)

        self.add_button = QPushButton(self.gridLayoutWidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setMinimumSize(QSize(35, 35))
        self.add_button.setMaximumSize(QSize(35, 35))
        self.add_button.setBaseSize(QSize(20, 20))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.add_button.setFont(font)
        self.add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_button.setAutoFillBackground(False)
        self.add_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #2ecc71;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #27ae60;\n"
"}")

        self.buttons_grid.addWidget(self.add_button, 0, Qt.AlignmentFlag.AlignHCenter)

        self.delete_button = QPushButton(self.gridLayoutWidget)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setMinimumSize(QSize(35, 35))
        self.delete_button.setMaximumSize(QSize(35, 35))
        self.delete_button.setBaseSize(QSize(20, 20))
        self.delete_button.setFont(font)
        self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #2ecc71;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #27ae60;\n"
"}")

        self.buttons_grid.addWidget(self.delete_button, 0, Qt.AlignmentFlag.AlignHCenter)

        self.details_button = QPushButton(self.gridLayoutWidget)
        self.details_button.setObjectName(u"details_button")
        sizePolicy.setHeightForWidth(self.details_button.sizePolicy().hasHeightForWidth())
        self.details_button.setSizePolicy(sizePolicy)
        self.details_button.setMinimumSize(QSize(35, 35))
        self.details_button.setMaximumSize(QSize(35, 35))
        self.details_button.setBaseSize(QSize(20, 20))
        self.details_button.setFont(font)
        self.details_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.details_button.setMouseTracking(True)
        self.details_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #2ecc71;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #27ae60;\n"
"}")

        self.buttons_grid.addWidget(self.details_button, 0, Qt.AlignmentFlag.AlignHCenter)

        self.done_button = QPushButton(self.gridLayoutWidget)
        self.done_button.setObjectName(u"done_button")
        sizePolicy.setHeightForWidth(self.done_button.sizePolicy().hasHeightForWidth())
        self.done_button.setSizePolicy(sizePolicy)
        self.done_button.setMinimumSize(QSize(35, 35))
        self.done_button.setMaximumSize(QSize(35, 35))
        self.done_button.setBaseSize(QSize(20, 20))
        font1 = QFont()
        font1.setFamilies([u".AppleSystemUIFont"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.done_button.setFont(font1)
        self.done_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.done_button.setMouseTracking(True)
        self.done_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #2ecc71;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #27ae60;\n"
"}")

        self.buttons_grid.addWidget(self.done_button, 0, Qt.AlignmentFlag.AlignHCenter)

        self.logout_button = QPushButton(self.gridLayoutWidget)
        self.logout_button.setObjectName(u"logout_button")
        sizePolicy.setHeightForWidth(self.logout_button.sizePolicy().hasHeightForWidth())
        self.logout_button.setSizePolicy(sizePolicy)
        self.logout_button.setMinimumSize(QSize(35, 35))
        self.logout_button.setMaximumSize(QSize(35, 35))
        self.logout_button.setBaseSize(QSize(20, 20))
        self.logout_button.setFont(font1)
        self.logout_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logout_button.setMouseTracking(True)
        self.logout_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #2ecc71;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #27ae60;\n"
"}")

        self.buttons_grid.addWidget(self.logout_button, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttons_grid.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.buttons_grid, 0, 0, 1, 1)

        self.table_grid = QGridLayout()
        self.table_grid.setObjectName(u"table_grid")
        self.task_table = QTableView(self.gridLayoutWidget)
        self.task_table.setObjectName(u"task_table")
        self.task_table.horizontalHeader().setDefaultSectionSize(150)
        self.task_table.horizontalHeader().setStretchLastSection(True)

        self.table_grid.addWidget(self.task_table, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.table_grid, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 50)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.add_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.details_button.setText(QCoreApplication.translate("Form", u"#", None))
        self.done_button.setText(QCoreApplication.translate("Form", u"\u2713", None))
        self.logout_button.setText(QCoreApplication.translate("Form", u"\u25c0\ufe0e", None))
    # retranslateUi

