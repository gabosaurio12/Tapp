import unittest

from src.bussinesslogic.ProfileDAOImplementation import ProfileDAOImplementation
from src.model.Profile import Profile

class test_ProfileDAO(unittest.TestCase):

    def setUp(self):
        self.dao = ProfileDAOImplementation()
        self.profile = Profile()
        self.profile.name = "José Sosa"
        self.profile.username = "josejose"
        self.profile.password = "eltriste1973"

    def test_insert_profile(self):
        id_profile = self.dao.insert_profile(self.profile)
        self.assertNotEqual(0, id_profile);
        self.dao.delete_profile_by_username(self.profile.username)

    def test_read_profile(self):
        self.dao.insert_profile(self.profile)
        profile = self.dao.read_profile_by_username(self.profile.username)
        self.assertEqual(self.profile.username, profile.username)
        self.dao.delete_profile_by_username(self.profile.username)

    def test_read_profiles(self):
        self.dao.insert_profile(self.profile)
        profiles = self.dao.read_profiles()
        self.assertNotEqual(0, len(profiles))
        self.dao.delete_profile_by_username(self.profile.username)

    def test_delete_profile(self):
        self.dao.insert_profile(self.profile)
        affected_rows = self.dao.delete_profile_by_username(self.profile.username)
        self.assertNotEqual(0, affected_rows)

if __name__ == '__main__':
    unittest.main()