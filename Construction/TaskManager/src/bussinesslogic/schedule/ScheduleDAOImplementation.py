import logging.config
import os
from bussinesslogic.schedule.ScheduleDAO import ScheduleDAO
from dataaccess.DBConnection import DBConnection
from model.Profile import Profile
from model.Schedule import Schedule

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.normpath(os.path.join(current_dir, "..", "..", "resources", "logging_config.ini"))
logging.config.fileConfig(path)

logger = logging.getLogger(__name__)

class ScheduleDAOImplementation(ScheduleDAO):

    def insert_schedule(self, schedule):
        schedule: Schedule = Schedule()
        query = "INSERT INTO schedule (id_profile) VALUES (%s) RETURNING id_schedule"
        id_schedule = 0
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (schedule.id_schedule))
                id_schedule = cursor.fetchone()[0]

        return id_schedule
    
    def read_schedule_by_profile(self, profile):
        profile: Profile
        query = """SELECT row_to_json(s) FROM 
        (SELECT * FROM schedule WHERE id_profile = %s) as s"""

        schedule = Schedule
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (profile.id_profile,))
                row = cursor.fetchone()
                schedule_dict = row[0]
                schedule = Schedule(**schedule_dict, tasks = None)

        return schedule
    
    def read_schedule_id_by_profile(self, profile):
        query = "SELECT id_schedule FROM schedule WHERE id_profile = %s"
        id_schedule = 0
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (profile.id_profile,))
                row = cursor.fetchone()
                if row is not None:
                    id_schedule = row[0]
                    
            return id_schedule

    def delete_schedule_by_id(self, schedule_id):
        pass