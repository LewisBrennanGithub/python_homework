from src.drink import Drink

class Pub:
    
    def __init__(self, name, till, beverage):
        self.name = name
        self.till = till
        # self.drinks_list = drinks_list
        self.drinks = {}
        self.beverage = beverage
        self.stock = {}
        

    def sell_drink(self, customer, drink):
        if customer.age >= 18 and customer.drunkenness <= 15:
            customer.wallet -= drink.price
            self.till += drink.price
            customer.drunkenness += drink.alcohol_units

    def sell_food(self, customer, food):
        customer.drunkenness -= food.rejuvination_level

    def drink_names(self, drink_name):
        for drink in drink_name:
            return drink
        
    def drinks_customer_can_afford(self, customer, drink_name):
        for punter in customer:
            if punter.wallet >= drink_name.price:
                return self.drinks




        # else:
        #     print("YOU'RE BARRED")

        # def drink_drink(self, drink):
        # self.drunkenness += drink.alcohol_units
