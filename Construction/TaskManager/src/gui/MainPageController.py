from PySide6.QtWidgets import *
from PySide6.QtGui import *
from gui.forms.mainpage import Ui_Form
from gui.AddTaskWindowController import AddTaskWindowController
from gui.DetailsWindowController import DetailsWindowController
from model.Profile import Profile
from model.Task import Task
from bussinesslogic.task.TaskDAOImplementation import TaskDAOImplementation
from bussinesslogic.schedule.ScheduleDAOImplementation import ScheduleDAOImplementation
from bussinesslogic.profile.ProfileDAOImplementation import ProfileDAOImplementation

class MainPageController(QMainWindow):
    def __init__(self, profile):
        super().__init__()
        self.profile = profile
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        headers = ["Tarea","Prioridad", "Estado", "Final"]
        self.model.setHorizontalHeaderLabels(headers)
        self.ui.task_table.setModel(self.model)
        self.ui.task_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.task_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.load_tasks()
        self.ui.add_button.clicked.connect(self.open_add_task_window)
        self.ui.delete_button.clicked.connect(self.delete_task)
        self.ui.details_button.clicked.connect(self.open_task_details_window)
        self.ui.done_button.clicked.connect(self.finish_task)
        self.ui.logout_button.clicked.connect(self.logout)

    def order_tasks(self, tasks):
        status_order = {
            "Pendiente": 0,
            "Iniciado": 1,
            "En proceso": 2,
            "": 3
        }

        priority_order = {
            "Baja": 0,
            "Media": 1,
            "Alta": 2
        }

        tasks.sort(key = lambda t: (
            -priority_order[t.priority],
            t.end_date is None,
            t.end_date,
            status_order.get(
                t.status if t.status else "", 0
            )
        ))

        return tasks

    def load_tasks(self):
        dao = TaskDAOImplementation()
        schedule_dao = ScheduleDAOImplementation()
        id_schedule = schedule_dao.read_schedule_id_by_profile(self.profile)
        tasks: list[Task] = dao.read_json_tasks(id_schedule)

        tasks = self.order_tasks(tasks)
    
        for task in tasks:
            row = [
                QStandardItem(task.title),
                QStandardItem(task.priority),
                QStandardItem(task.status),
                QStandardItem(task.end_date)
            ]
            self.model.appendRow(row)

    def open_add_task_window(self):
        dao = ScheduleDAOImplementation()
        schedule = dao.read_schedule_by_profile(self.profile)
        self.add_task_window = AddTaskWindowController(schedule)
        self.add_task_window.task_added.connect(self.refresh_table)
        self.add_task_window.show()

    def get_task_from_table(self):
        selection_model = self.ui.task_table.selectionModel()
        indexes = selection_model.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            model = self.ui.task_table.model()
            title = model.index(row, 0).data()
            dao = TaskDAOImplementation()
            task = dao.read_json_task_by_title(title)

        return task


    def open_task_details_window(self):
        task = self.get_task_from_table()
        self.task_details_window = DetailsWindowController(task)
        self.task_details_window.task_updated.connect(self.refresh_table)
        self.task_details_window.show()

    def delete_task(self):
        task = self.get_task_from_table()
        dao = TaskDAOImplementation()
        dao.delete_task(task)
        self.refresh_table()

    def refresh_table(self):
        self.model.removeRows(0, self.model.rowCount())
        self.load_tasks()

    def finish_task(self):
        dao = TaskDAOImplementation()
        task = self.get_task_from_table()
        dao.conclude_task(task)
        self.refresh_table()

    def logout(self):
        from gui.LoginController import LoginController
        id = 0
        dao = ProfileDAOImplementation()
        dao.update_current_profile(id)
        self.loginWindow = LoginController()
        self.loginWindow.show()
        self.close()