pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ]
}
customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]



#     def sell_pet_to_customer(shop, pet, customer):
#         shop_counter = 0
#         pet_profile = pet_shop["pets"][shop_counter]
#         while shop_counter < len(shop["pets"]):
#             shop_counter += 1
#         customer_counter = 0
#         while customer_counter < len(customers):
#             customer_counter += 1
#         customer_pet_list = customers[customer_counter]["pets"]
#         if pet_names == pet:
#             customer_pet_list = pet_profile.pop()

# sell_pet_to_customer(pet_shop, "Arthur", "Alice")
# print(customers)

def sell_pet_to_customer(shop, pet_name, customer):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            pet_to_sell = pet

    # Find the customer in the list of customers
    for c in customers:
        if c["name"] == customer:
            customer_to_buy = c

    if customer_to_buy["cash"] < pet_to_sell["price"]:
        print("Customer does not have enough cash to buy the pet.")
        return

    customer_to_buy["pets"].append(pet_to_sell)
    shop["pets"].remove(pet_to_sell)
    customer_to_buy["cash"] -= pet_to_sell["price"]

# def test(shop):
#     int = 0
#     while int < len(shop["pets"]):
#         print(shop["pets"][int]["name"])
#         int += 1

# test(pet_shop)

# # for insert
# if name == .pop

# list_two.append(list_one.pop(list_one.index(item)))


# print(pet_shop["pets"][0]["name"])
# print(customers[0]["pets"])
# print(pet_shop["pets"][3])
# customers[0]["pets"] = pet_shop["pets"][3].copy()
# print(customers[0]["pets"])