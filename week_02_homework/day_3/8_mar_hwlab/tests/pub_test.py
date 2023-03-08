import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("Boozer", 1000.0, {"Martini": 20, "White Russian": 20, "Shot": 20, "Pint": 20})
        self.customer1 = Customer("Clive", 50.0, 32)
        self.customer2 = Customer("Jemima", 500, 16)
        self.customer3 = Customer("Burt", 0, 89)
        self.drink1 = Drink("Martini", 9.99, 5)
        self.drink2 = Drink("White Russian", 7.50, 3)
        self.drink3 = Drink("Shot", 2.50, 5)
        self.drink4 = Drink("Pint", 6.00, 2)
        self.food1 = Food("Nuts", 1, 5)
        self.food2 = Food("Paela", 10, 20)
        self.pub = Pub("Boozer", 1000.0)
        # print(self.pub.drinks)
        # {self.drink1: 20, self.drink2: 20, self.drink3: 20, self.drink4: 20}

    def test_pub_has_name(self):
        self.assertEqual("Boozer", self.pub.name)

    def test_till_value(self):
        self.assertEqual(1000.0, self.pub.till)

    def test_drink_purchase(self):
        drink1 = Drink("Martini", 9.99, 5)
        self.pub.sell_drink(self.customer1, drink1)
        self.assertEqual(40.01, self.customer1.wallet)
        self.assertEqual(1009.99, self.pub.till)
        self.assertLessEqual(18, self.customer1.age)

    def test_customer(self):
        self.pub.sell_drink(self.customer1, self.drink1)
        self.pub.sell_drink(self.customer1, self.drink1)
        self.pub.sell_drink(self.customer1, self.drink1)
        print(self.customer1.drunkenness)
        self.assertEqual(20.029999999999994, self.customer1.wallet)
        self.assertEqual(1029.97, self.pub.till)
        # print(self.pub.drinks)
        self.assertEqual(15, self.customer1.drunkenness)

    def test_customer_underage(self):
        self.pub.sell_drink(self.customer2, self.drink2)
        self.assertEqual(500, self.customer2.wallet)
        self.assertEqual(1000, self.pub.till)
        self.assertEqual(0, self.customer2.drunkenness)

    def test_food_impact(self):
        self.pub.sell_drink(self.customer1, self.drink3)
        self.pub.sell_drink(self.customer1, self.drink3)
        self.pub.sell_drink(self.customer1, self.drink3)
        self.pub.sell_drink(self.customer1, self.drink3)
        self.pub.sell_drink(self.customer1, self.drink3)
        self.pub.sell_drink(self.customer1, self.drink3)
        print(self.customer1.drunkenness)
        self.pub.sell_food(self.customer1, self.food2)
        print(self.customer1.drunkenness)
        self.assertEqual(0, self.customer1.drunkenness)
        


    


    
