import logging.config
import os
import json
from bussinesslogic.profile.ProfileDAO import ProfileDAO
from dataaccess.DBConnection import DBConnection
from model.Profile import Profile

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.normpath(os.path.join(current_dir, "..", "..", "resources", "logging_config.ini"))
logging.config.fileConfig(path)

logger = logging.getLogger(__name__)

class ProfileDAOImplementation(ProfileDAO):

    def insert_profile(self, profile):
        query = """
        INSERT INTO profile (username, password, name)
        SELECT username, encode(digest(password, 'sha256'), 'hex'), name
        FROM json_populate_record(NULL::profile, %s::json)
        RETURNING id_profile;
        """
        id_profile = 0
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query, 
                    (json.dumps(profile),)
                )
                id_profile = cursor.fetchone()[0]
        
        return id_profile
    
    def read_profile_by_username(self, username):
        query = "SELECT * FROM profile WHERE username = %s;"
        profile = Profile()
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (username,))
                row = cursor.fetchone()
                if row is not None:
                    profile.id_profile = row[0]
                    profile.username = row[1]
                    profile.password = row[2]
                    profile.name = row[3]

        return profile
    
    def read_profile_by_id(self, id):
        query = "SELECT * FROM profile WHERE id_profile = %s;"
        profile = Profile()
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row is not None:
                    profile.id_profile = row[0]
                    profile.username = row[1]
                    profile.password = row[2]
                    profile.name = row[3]

        return profile
    
    def read_profiles(self):
        query = "SELECT * FROM profile;"

        profiles = []
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, ())
                for row in cursor.fetchall():
                    profile = Profile(
                        id_profile = row[0],
                        username = row[1],
                        password = row[2],
                        name = row[3],
                        schedules = []
                    )
                    profiles.append(profile)

        return profiles
    
    def update_profile_by_username(self, profile):
        query = """UPDATE profile SET username = %s,
        password = encode(digest(%s, 'sha256'), 'hex'), name = %s 
        WHERE username = %s;"""

        affected_rows = 0
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (profile.username, profile.password, profile.name, profile.username))
                affected_rows = cursor.rowcount

        return affected_rows
    
    def delete_profile_by_username(self, username):
        query = "DELETE FROM profile WHERE username = %s;"

        affected_rows = 0
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (username,))
                affected_rows = cursor.rowcount

        return affected_rows
    
    def update_current_profile(self, id):
        query = "UPDATE current_profile SET id_profile = %s"
        affected_rows = 0
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id,))
                affected_rows = cursor.rowcount

        return affected_rows
    
    def read_current_profile(self):
        query = "SELECT * FROM current_profile;"

        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    id = row[0]

        return id