# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, money):
    pet_shop["admin"]["total_cash"] += money

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets):
    pet_shop["admin"]["pets_sold"] += pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
    return pet_list

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    x = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].pop(x)
        x += 1

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    # count = 0
    # for pet in customer["pets"]:
    #     count += 1
    # return count
    return(len(customer["pets"]))

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    #move new_pet to customer
    #remove new pet from new_pet
    #remove cash from customer
    #add cash to shop cash   
    if pet == None:
        return
    if customer_can_afford_pet(customer, pet):
            remove_customer_cash(customer, pet["price"])    
            add_or_remove_cash(pet_shop, pet["price"])
            add_pet_to_customer(customer, pet)
            remove_pet_by_name(pet_shop, pet)
            increase_pets_sold(pet_shop, 1)

        
        

