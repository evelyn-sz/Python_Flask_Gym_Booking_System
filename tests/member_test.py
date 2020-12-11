import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member("Geralt", "of Rivia")

    def test_member_has_full_name(self):
        self.assertEqual("Geralt of Rivia", self.activity.member.full_name())

