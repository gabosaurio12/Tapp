# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailswindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(390, 524)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 10, 371, 501))
        self.general_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.general_layout.setObjectName(u"general_layout")
        self.general_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout = QFormLayout()
        self.form_layout.setObjectName(u"form_layout")
        self.title_label = QLabel(self.verticalLayoutWidget)
        self.title_label.setObjectName(u"title_label")

        self.form_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.title_label)

        self.title_edit = QLineEdit(self.verticalLayoutWidget)
        self.title_edit.setObjectName(u"title_edit")

        self.form_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.title_edit)

        self.description_label = QLabel(self.verticalLayoutWidget)
        self.description_label.setObjectName(u"description_label")

        self.form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.description_label)

        self.description_edit = QTextEdit(self.verticalLayoutWidget)
        self.description_edit.setObjectName(u"description_edit")

        self.form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.description_edit)

        self.start_label = QLabel(self.verticalLayoutWidget)
        self.start_label.setObjectName(u"start_label")

        self.form_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.start_label)

        self.end_label = QLabel(self.verticalLayoutWidget)
        self.end_label.setObjectName(u"end_label")

        self.form_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.end_label)

        self.status_label = QLabel(self.verticalLayoutWidget)
        self.status_label.setObjectName(u"status_label")

        self.form_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.status_label)

        self.status_combo = QComboBox(self.verticalLayoutWidget)
        self.status_combo.addItem("")
        self.status_combo.setObjectName(u"status_combo")

        self.form_layout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.status_combo)

        self.priority_label = QLabel(self.verticalLayoutWidget)
        self.priority_label.setObjectName(u"priority_label")

        self.form_layout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.priority_label)

        self.priority_combo = QComboBox(self.verticalLayoutWidget)
        self.priority_combo.setObjectName(u"priority_combo")

        self.form_layout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.priority_combo)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.start_time_edit = QDateTimeEdit(self.verticalLayoutWidget)
        self.start_time_edit.setObjectName(u"start_time_edit")
        self.start_time_edit.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.start_time_edit)

        self.start_check = QCheckBox(self.verticalLayoutWidget)
        self.start_check.setObjectName(u"start_check")

        self.horizontalLayout_5.addWidget(self.start_check, 0, Qt.AlignmentFlag.AlignHCenter)


        self.form_layout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.end_time_edit = QDateTimeEdit(self.verticalLayoutWidget)
        self.end_time_edit.setObjectName(u"end_time_edit")
        self.end_time_edit.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.end_time_edit)

        self.end_check = QCheckBox(self.verticalLayoutWidget)
        self.end_check.setObjectName(u"end_check")

        self.horizontalLayout_6.addWidget(self.end_check, 0, Qt.AlignmentFlag.AlignHCenter)


        self.form_layout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_6)


        self.general_layout.addLayout(self.form_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_layout.addItem(self.horizontalSpacer_3)

        self.cancel_button = QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.buttons_layout.addWidget(self.cancel_button)

        self.horizontalSpacer = QSpacerItem(125, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.buttons_layout.addItem(self.horizontalSpacer)

        self.confirm_button = QPushButton(self.verticalLayoutWidget)
        self.confirm_button.setObjectName(u"confirm_button")

        self.buttons_layout.addWidget(self.confirm_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_layout.addItem(self.horizontalSpacer_2)


        self.general_layout.addLayout(self.buttons_layout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"T\u00edtulo", None))
        self.description_label.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n", None))
        self.start_label.setText(QCoreApplication.translate("Form", u"Inicio", None))
        self.end_label.setText(QCoreApplication.translate("Form", u"Final", None))
        self.status_label.setText(QCoreApplication.translate("Form", u"Estatus", None))
        self.status_combo.setItemText(0, "")

        self.priority_label.setText(QCoreApplication.translate("Form", u"Prioridad", None))
        self.start_check.setText(QCoreApplication.translate("Form", u"Inicio", None))
        self.end_check.setText(QCoreApplication.translate("Form", u"Final", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.confirm_button.setText(QCoreApplication.translate("Form", u"Ok", None))
    # retranslateUi

