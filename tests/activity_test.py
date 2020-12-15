import unittest
from models.activity import Activity

class TestActivity(unittest.TestCase):

    def setUp(self):
        self.activity = Activity("Emotions Yoga", "Djinn's Bottle", "hollistic", 12, False)

    def test_activity_has_name(self):
        self.assertEqual("Emotions Yoga", self.activity.name)

    def test_activity_has_category(self):
        self.assertEqual("hollistic", self.activity.category)

    def test_activity_finished_starts_false(self):
        self.assertEqual(False, self.activity.finished)

    def test_activity_has_capacity(self):
        self.assertEqual(12, self.activity.capacity)