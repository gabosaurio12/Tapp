from PySide6.QtWidgets import *
from PySide6.QtCore import QDate, QTime, QDateTime
from gui.forms.addtaskwindow import Ui_Form
from PySide6.QtCore import Signal
from bussinesslogic.catalog.CatalogDAOImplementation import CatalogDAOImplementation
from bussinesslogic.task.TaskDAOImplementation import TaskDAOImplementation
from model.Task import Task

class DetailsWindowController(QMainWindow):
    task_updated = Signal()

    def __init__(self, task):
        super().__init__()
        self.task: Task = task

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.set_info()

        self.ui.start_check.clicked.connect(self.enable_start_time)
        self.ui.end_check.clicked.connect(self.enable_end_time)
        self.ui.confirm_button.clicked.connect(self.update_task)
        self.ui.cancel_button.clicked.connect(self.close_window)


    def close_window(self):
        self.close()

    def set_info(self):
        task = self.task
        self.ui.title_edit.setText(task.title)
        self.ui.description_edit.setText(task.description)
        if task.start_time != None:
            self.set_start_time()
        if task.end_time != None:
            self.set_end_time()

        self.set_status_combo(task.status)
        self.set_priority_combo(task.priority)

    def set_status_combo(self, task_status):
        dao = CatalogDAOImplementation()
        status = dao.read_status_catalog()
        for i in status:
            self.ui.status_combo.addItem(i)
        index = self.ui.status_combo.findText(task_status)
        if index >= 0:
            self.ui.status_combo.setCurrentIndex(index)

    def set_priority_combo(self, task_priority):
        dao = CatalogDAOImplementation()
        priorities = dao.read_priority_catalog()
        for i in priorities:
            self.ui.priority_combo.addItem(i)
        index = self.ui.priority_combo.findText(task_priority)
        if index >= 0:
            self.ui.priority_combo.setCurrentIndex(index)

    def set_start_time(self):
        check_box = self.ui.start_check
        start_time = self.ui.start_time_edit
        date_str = self.task.start_date
        time_str = self.task.start_time

        year, month, day = map(int, date_str.split("-"))
        hour, minute, second = map(int, time_str.split(":"))

        date = QDate(year, month, day)
        time = QTime(hour, minute, second)

        date_time = QDateTime(date, time)

        if (self.task.start_date != None or self.task.start_time != None):
            check_box.setChecked(True)
            start_time.setEnabled(True)
            start_time.setDateTime(date_time)
        else:
            start_time.setEnabled(False)
            check_box.setChecked(False)

    def set_end_time(self):
        check_box = self.ui.end_check
        end_time = self.ui.end_time_edit
        date_str = self.task.end_date
        time_str = self.task.end_time

        year, month, day = map(int, date_str.split("-"))
        hour, minute, second = map(int, time_str.split(":"))

        date = QDate(year, month, day)
        time = QTime(hour, minute, second)

        date_time = QDateTime(date, time)

        if (self.task.end_date != None or self.task.end_time != None):
            check_box.setChecked(True)
            end_time.setEnabled(True)
            end_time.setDateTime(date_time)
        else:
            end_time.setEnabled(False)
            check_box.setChecked(False)

    def enable_start_time(self):
        check_box = self.ui.start_check
        start_time = self.ui.start_time_edit
        if (check_box.isChecked()):
            start_time.setEnabled(True)
        else:
            start_time.setEnabled(False)

    def enable_end_time(self):
        check_box = self.ui.end_check
        end_time = self.ui.end_time_edit
        if (check_box.isChecked()):
            end_time.setEnabled(True)
        else:
            end_time.setEnabled(False)


    def get_info(self):
        title = self.ui.title_edit.text()
        description = self.ui.description_edit.toPlainText()
        start_date = None
        start_time = None
        if (self.ui.start_check.isChecked()):
            start_edit = self.ui.start_time_edit
            start_date = start_edit.date().toPython()
            start_time = start_edit.time().toPython()
        
        end_date = None
        end_time = None
        if (self.ui.end_check.isChecked()):
            end_edit = self.ui.end_time_edit
            end_date = end_edit.date().toPython()
            end_time = end_edit.time().toPython()

        status = self.ui.status_combo.currentText()
        priority = self.ui.priority_combo.currentText()
        id_schedule = self.task.id_schedule

        task: Task = Task(
            0,
            title,
            status,
            priority,
            start_date,
            start_time,
            end_date,
            end_time,
            description,
            id_schedule
        )

        return task

    def update_task(self):
        task = self.get_info()
        dao = TaskDAOImplementation()
        dao.update_task(task, self.task)
        self.task_updated.emit()
        self.close()
