from dataaccess.DBConnection import DBConnection
from bussinesslogic.catalog.CatalogDAO import CatalogDAO

class CatalogDAOImplementation(CatalogDAO):

    def read_priority_catalog(self):
        query = "SELECT * FROM priority_catalog"
        priorities = []
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, ())
                for row in cursor.fetchall():
                    priorities.append(row[0])

        return priorities
    
    def read_status_catalog(self):
        query = "SELECT * FROM status_catalog"
        status = []
        with DBConnection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, ())
                for row in cursor.fetchall():
                    status.append(row[0])
                    
        return status
