import logging.config
import os
import json
from bussinesslogic.task.TaskDAO import TaskDAO
from dataaccess.DBConnection import DBConnection
from model.Task import Task

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.normpath(os.path.join(current_dir, "..", "..", "resources", "logging_config.ini"))
logging.config.fileConfig(path)

logger = logging.getLogger(__name__)

class TaskDAOImplementation(TaskDAO):

    def insert_json_task(self, task):
        query = """
        INSERT INTO task (title, status, priority, description, id_schedule, start_date, start_time, end_date, end_time)
        SELECT title, status, priority, description, id_schedule, start_date, start_time, end_date, end_time
        FROM json_populate_record(NULL::task, %s::json)
        RETURNING id_task
        """
        id_task = 0
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (json.dumps(task),))
                id_task = cursor.fetchone()[0]
                
        return id_task
    
    def read_json_task_by_title(self, title):
        query = """SELECT row_to_json(t) FROM
            (SELECT * FROM task WHERE title = %s) as t"""
        
        task: Task
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (title,))
                for row in cursor.fetchone():
                    task = Task(
                        id_task = row['id_task'],
                        title = row['title'],
                        status = row['status'],
                        priority= row['priority'],
                        description = row['description'],
                        id_schedule = row['id_schedule'],
                        start_date = row['start_date'],
                        start_time = row['start_time'],
                        end_date = row['end_date'],
                        end_time = row['end_time']
                    )
        return task
        
    def read_tasks_by_schedule(self, id_schedule):
        query = "SELECT * FROM task WHERE id_schedule = %s;"

        tasks = []
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_schedule,))
                for row in cursor.fetchall():
                    task = Task(
                        id_task = row['id_task'],
                        title = row['title'],
                        status = row['status'],
                        priority= row['priority'],
                        description = row['description'],
                        id_schedule = row['id_schedule'],
                        start_date = row['start_date'],
                        start_time = row['start_time'],
                        end_date = row['end_date'],
                        end_time = row['end_time']
                    )
                    tasks.append(task)
        return tasks
    
    def read_json_tasks(self, id_schedule):
        query = """SELECT row_to_json(t) FROM
          (SELECT * FROM task WHERE id_schedule = %s) as t"""

        tasks = []
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_schedule,))
                for row in cursor.fetchall():
                    task_dict = row[0]
                    task = Task(**task_dict)
                    tasks.append(task)
        return tasks

    def update_task(self, task, old_task):
        query = """UPDATE task SET title = %s, description = %s, start_date = %s, 
        start_time = %s, end_date = %s, end_time = %s, status = %s, priority = %s
        WHERE title = %s AND id_schedule = %s AND priority = %s"""

        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (
                    task.title,
                    task.description,
                    task.start_date,
                    task.start_time,
                    task.end_date,
                    task.end_time,
                    task.status,
                    task.priority,
                    old_task.title,
                    old_task.id_schedule,
                    old_task.priority
                ))

    def delete_task(self, task):
        query = """DELETE FROM task WHERE title = %s AND priority = %s AND id_schedule = %s"""
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (task.title, task.priority, task.id_schedule))

    def conclude_task(self, task):
        query = """UPDATE task SET status = %s WHERE title = %s AND id_schedule = %s"""

        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (
                    "Finalizado",
                    task.title,
                    task.id_schedule,
                ))