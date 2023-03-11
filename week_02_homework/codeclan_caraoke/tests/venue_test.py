import unittest
from src.venue import *
from src.room import *
from src.guest import *
from src.drink import *

class TestVenue(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("IPA", 10)
        self.drink2 = Drink("Buckfast", 40)
        self.guest1 = Guest("Clive", 50)
        self.guest2 = Guest("Burt", 20)
        self.guest3 = Guest("Barnabus", 5)
        self.guest4 = Guest("Otto", 25)
        self.guest5 = Guest("Palmer", 4)
        self.room1 = Room("Funk Bunk", "Funk", 5)
        self.room2 = Room("Folkin Hell", "Folk", 2)
        self.venue1 = Venue("Funkin Folk", 5, 500)
        self.venue1.add_rooms_to_venue(self.room1)
        self.venue1.add_rooms_to_venue(self.room2)

    def test_venue__has_name(self):
        self.assertEqual("Funkin Folk", self.venue1.name)

    def test_venue__has_rooms(self):
        self.assertEqual(2, len(self.venue1.rooms))

    def test_venue__room_capacity(self):
        self.venue1.add_customer_to_venue(self.guest1)
        self.venue1.add_customer_to_venue(self.guest2)
        self.venue1.add_customer_to_venue(self.guest3)
        self.venue1.add_customer_to_venue(self.guest4)
        self.venue1.add_customer_to_room(self.room2)
        self.venue1.add_customer_to_room(self.room2)
        self.venue1.add_customer_to_room(self.room2)
        self.venue1.add_customer_to_room(self.room2)
        self.room2.find_guest_in_attendance(self.room2.attendance)
        self.assertEqual(2, len(self.room2.attendance))

    def test_venue__can_add_customer_to_venue(self):
        self.venue1.add_customer_to_venue(self.guest1)
        self.venue1.add_customer_to_venue(self.guest5)
        self.assertEqual(1, len(self.venue1.hub_guests))
        self.assertEqual(505, self.venue1.till)

    def test_venue__can_add_drink(self):
        self.venue1.add_drink_to_stock(self.drink1.name, 5)
        self.venue1.add_drink_to_stock(self.drink2.name, 10)
        self.venue1.add_drink_to_stock(self.drink2.name, 4)
        self.venue1.add_drink_to_stock(self.drink2.name, 4)
        self.assertIn("Buckfast", self.venue1.stock)
        print(self.venue1.stock)

    def test_venue__can_sell_drink(self):
        self.venue1.add_drink_to_stock(self.drink1.name, 5)
        print(self.venue1.stock)
        self.venue1.venue_can_sell_drink(self.guest1, self.drink1.name)
        print(self.venue1.till)
        self.assertEqual(510, self.venue1.till)





    

    
        
