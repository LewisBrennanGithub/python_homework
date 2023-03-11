class Guest:

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def guest_can_afford_entry(self, item):
        if self.cash >= item.entry_fee:
            return self.cash
        
    def guest_can_afford_drink(self, drink):
        if self.cash >= drink.price:
            return self.cash
        
    def guest_buy_entry(self, venue):
        if self.guest_can_afford_entry(venue):
            self.cash -= venue.entry_fee

    def guest_buy_drink(self, drink):
        if self.guest_can_afford_drink(drink):
            self.cash -= drink.price
    
    # def guest_can_afford_entry(self, item):
    #     if self.cash >= item.entry_fee:
    #         return self.cash 

    # def guest_can_buy_entry(self, venue):
    #     if self.guest_can_afford_entry(venue):
    #         self.cash -= venue.entry_fee