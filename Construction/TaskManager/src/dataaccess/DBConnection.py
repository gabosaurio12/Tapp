from .DatabaseConfig import DatabaseConfig
import psycopg2

class DBConnection:

    def get_connection():
        config_loader = DatabaseConfig()
        properties = config_loader.load_properties()
        return psycopg2.connect(
            database = properties.get("database").data,
            user = properties.get("username").data,
            password = properties.get("password").data,
            host = properties.get("host").data,
            port = properties.get("port").data
        )
