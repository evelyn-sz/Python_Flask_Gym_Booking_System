import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member("Geralt", "of Rivia", "premium")

    def test_member_has_full_name(self):
        self.assertEqual("Geralt of Rivia", self.member.full_name())

    def test_member_has_membership(self):
        self.assertEqual("premium", self.member.membership_type)

