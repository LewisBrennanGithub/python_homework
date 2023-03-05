# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(name):
    return name["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, amount): 
    shop["admin"]["total_cash"] += amount
    # shop["admin"]["total_cash"] - amount 

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, amount):
    shop["admin"]["pets_sold"] += amount

    # return pet_sales
    # pet_sales = shop["admin"]["pets_sold"] + pets_bought
    # return pet_sales

    # pets_sold = 0
    # pets_sold += pets_bought
    # return pets_sold

# if len(shop["pets"])

def get_stock_count(shop):
    return len(shop["pets"])

# def get_pets_by_breed(shop, animal):
#     pet_counter = 0
#     if shop["pets"]["breed"][animal] == True:
#         pet_counter += 1
#     return pet_counter

def get_pets_by_breed(shop, animal):
    breeds_in_stock = []
    # new list created above
    pets = shop["pets"]
    # new variable created above, purpose of which is to allow the below for loop to iterate, with pet essentially representing [0][1]etc
    for pet in pets:
        if pet["breed"] == animal:
           breeds_in_stock.append(pet)
    return breeds_in_stock
        
    # if shop["pets"]["name"] == "Sir Percy" or "King Badgemagus" or "Tristan" or "Merlin":
    #     return shop["pets"]["pet_type"]["cat"]
    # elif shop["pets"]["name"] == "Sir Lancelot" or "Arthur"
    #     return shop["pets"]["name"]["dog"]

def find_pet_by_name(shop, animal):
    pets = shop["pets"]
    for pet in pets: 
        if pet["name"] == animal:
            return pet
    return None

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, name):
    shop["pets"].append(name)

def get_customer_cash(shoppers):
    shopper = 0
    return [shoppers][shopper]["cash"]

def remove_customer_cash(shoppers, amount):
    shopper = 0
    [shoppers][shopper]["cash"] -= amount

# def get_customer_pet_count(shoppers):
#     list = 0
#     shopper = 0
#     if [shoppers][shopper]["pets"] == []:
#         list = 0
#     elif [shoppers][shopper]["pets"] != []:
#         return list 

def get_customer_pet_count(customer):
    return len(customer["pets"])

# def add_pet_to_customer(shoppers, new_animal):
#     list = 0
#     shopper = 0
#     if [shoppers][shopper]["pets"] == [new_animal]:
#         list = 1
#         print([shoppers][shopper]["pets"])
#     return list

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customers, new_animal):
    customer_cash = customers["cash"]
    animal_price = new_animal["price"]
    if customer_cash >= animal_price:
        return True
    else:
        return False

def sell_pet_to_customer(shop, pet_name, customer):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            pet_to_sell = pet

    for c in customer:
        if c["name"] == customer:
            customer_to_buy = c

    customer_to_buy["pets"].append(pet_to_sell)
    shop["pets"].remove(pet_to_sell)
    customer_to_buy["cash"] -= pet_to_sell["price"]