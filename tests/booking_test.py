import unittest
from models.booking import Booking
from models.member import Member
from models.activity import Activity

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member_1 = Member()
        self.booking = Booking()