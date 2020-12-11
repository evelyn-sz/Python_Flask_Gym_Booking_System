import unittest
from models.booking import Booking
from models.member import Member
from models.activity import Activity

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member_1 = Member("Geralt", "of Rivia")
        self.activity_1 = Activity("Emotions Yoga", "hollistic", False)
        self.booking = Booking(self.member_1, self.activity_1)

    def test_booking_has_member_full_name(self):
        self.assertEqual("Geralt of Rivia", self.booking.member.full_name())

    def test_booking_has_activity_name(self):
        self.assertEqual("Emotions Yoga", self.booking.activity.name)

    