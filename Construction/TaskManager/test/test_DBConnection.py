import unittest

from src.dataaccess.DBConnection import DBConnection

class TestDBConnection(unittest.TestCase):

    def setUp(self):
        self.connection = DBConnection()

    def test_connection_is_not_none(self):
        self.assertIsNotNone(self.connection)


if __name__ == '__main__':
    unittest.main()
