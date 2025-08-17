from PySide6.QtWidgets import *
from gui.forms.addtaskwindow import Ui_Form
from PySide6.QtCore import Signal
from bussinesslogic.catalog.CatalogDAOImplementation import CatalogDAOImplementation
from bussinesslogic.task.TaskDAOImplementation import TaskDAOImplementation
from model.Task import Task
from model.Schedule import Schedule
from datetime import date, time

class AddTaskWindowController(QMainWindow):
    task_added = Signal()

    def __init__(self, schedule):
        super().__init__()
        self.schedule: Schedule = schedule

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.set_status_combo()
        self.set_priority_combo()

        self.ui.start_check.clicked.connect(self.set_start_time)
        self.ui.end_check.clicked.connect(self.set_end_time)
        self.ui.confirm_button.clicked.connect(self.add_task)
        self.ui.cancel_button.clicked.connect(self.close_window)


    def close_window(self):
        self.close()

    def set_status_combo(self):
        dao = CatalogDAOImplementation()
        status = dao.read_status_catalog()
        for i in status:
            self.ui.status_combo.addItem(i)

    def set_priority_combo(self):
        dao = CatalogDAOImplementation()
        priorities = dao.read_priority_catalog()
        for i in priorities:
            self.ui.priority_combo.addItem(i)

    def set_start_time(self):
        check_box = self.ui.start_check
        start_time = self.ui.start_time_edit
        if (check_box.isChecked()):
            start_time.setEnabled(True)
        else:
            start_time.setEnabled(False)

    def set_end_time(self):
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
        id_schedule = self.schedule.id_schedule

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

    def add_task(self):
        task = self.get_info()
        task_dict = task.to_clean_dict()
        task_dict.pop('id_task', None)
        dao = TaskDAOImplementation()
        dao.insert_json_task(task_dict)
        self.task_added.emit()
        self.close()
