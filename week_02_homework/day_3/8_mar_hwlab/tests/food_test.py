import unittest

from src.food import Food

class TestFood(unittest.TestCase):

        def setUp(self):
                self.food1 = Food("Nuts", 1, 5)
                self.food2 = Food("Paela", 10, 20)

        def test_food_name(self): 
           self.assertEqual("Nuts", self.food1.name)
           self.assertEqual("Paela", self.food2.name)       

        def test_food_price(self):
           self.assertEqual(1, self.food1.price)
           self.assertEqual(10, self.food2.price)  
            
        def test_rejuvination(self):
            self.assertEqual(5, self.food1.rejuvination_level)
            self.assertEqual(20, self.food2.rejuvination_level)  
