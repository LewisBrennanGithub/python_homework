import unittest
from src.venue import *
from src.room import *
from src.guest import *
from src.drink import *
from src.song import *

class TestVenue(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("IPA", 10)
        self.drink2 = Drink("Buckfast", 40)
        self.songfunk1 = Song("Can't be funked", "Funk")
        self.songfunk2 = Song("Funkless task", "Funk")
        self.songfolk1 = Song("When the folk will that be", "Folk")
        self.songfolk2 = Song("The folk you talking about", "Folk")
        self.guest1 = Guest("Clive", 50, self.songfunk1)
        self.guest2 = Guest("Burt", 20, self.songfunk2)
        self.guest3 = Guest("Barnabus", 5, self.songfolk1)
        self.guest4 = Guest("Otto", 25, self.songfolk2)
        self.guest5 = Guest("Palmer", 4, self.songfunk1)
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
        self.venue1.add_drink_to_stock(self.drink1, 5)
        self.venue1.add_drink_to_stock(self.drink2, 10)
        self.venue1.add_drink_to_stock(self.drink2, 4)
        self.venue1.add_drink_to_stock(self.drink2, 4)
        self.assertIn("Buckfast", self.venue1.stock)
        print(self.venue1.stock)
        # self.assertIn('Buckfast', self.venue1.stock.keys())

    def test_venue__has_stock(self):
        self.venue1.add_drink_to_stock(self.drink1, 5)
        self.venue1.add_drink_to_stock(self.drink2, 4)
        self.venue1.venue_find_total_stock_value(self.drink1)
        self.assertEqual(5, self.venue1.stock[self.drink1.name])
        print(self.venue1.stock)

    # def test_venue__can_sell_drink(self):
    #     self.venue1.add_drink_to_stock(self.drink1, 5)
    #     print(self.venue1.stock[self.drink1.price])
        # self.venue1.venue_can_sell_drink(self.guest1, self.drink1, 1)
        # print(self.venue1.stock)
        # self.assertEqual(4, self.venue1.stock[self.drink1])
    #     self.venue1.venue_can_sell_drink(self.guest1, self.drink1, 1)
    #     self.assertEqual(3, self.venue1.stock[self.drink1])
    
    # def test_venue__has_stock_value(self):
    #     self.venue1.add_drink_to_stock(self.drink1, 5)
    #     self.assertEqual(50, self.venue1.stock_value())

    # def test_pub_has_stock_value(self):
    #     self.venue1.add_drink_to_stock(self.drink1, 5)
    #     self.assertEqual(2.00, self.venue1.stock_value())
        # self.venue1.add_drink_to_stock(self.drink2, 4)   

    # def test_venue__can_sell_drink(self):
    #     self.venue1.add_drink_to_stock(self.drink1, 5)
    #     print(self.venue1.stock[self.drink1.price])
        # self.venue1.venue_can_sell_drink(self.guest1, self.drink1, 1)
        # print(self.venue1.stock)
        # self.assertEqual(4, self.venue1.stock[self.drink1])
    #     self.venue1.venue_can_sell_drink(self.guest1, self.drink1, 1)
    #     self.assertEqual(3, self.venue1.stock[self.drink1])

    # def test_venue__cant_sell_drink_poor_customer(self):
    #     self.venue1.add_drink_to_stock(self.drink1, 5)
    #     self.venue1.venue_can_sell_drink(self.guest3, self.drink1, 1)
    #     self.assertEqual(5, self.venue1.stock[self.drink1])

    # def test_venue__cant_sell_drink_no_stock(self):
    #     self.venue1.add_drink_to_stock(self.drink1, 1)
    #     self.venue1.venue_can_sell_drink(self.guest3, self.drink1, 1)
    #     self.assertEqual(0, self.venue1.stock[self.drink1])






    

    
        
