spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]
food_names=get_names(spicy_foods)
print(food_names)
pass

def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food ["heat_level"]>5]
print(get_spiciest_foods(spicy_foods))
pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = food ["heat_level"]
        peppers = '🌶' * heat
        #if heat >5:
        print (f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

print(print_spicy_foods(spicy_foods))
pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'].lower()== cuisine.lower():
            return food
print(get_spicy_food_by_cuisine(spicy_foods,"Sichuan"))
pass
def print_spiciest_foods(spicy_foods):
    """Prints foods with heat_level > 5 formatted with pepper emojis"""
    for food in spicy_foods:
        if food["heat_level"] > 5:
            peppers = '🌶' * food["heat_level"]  # Using regular pepper emoji without variation selector
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

# def print_spiciest_foods(spicy_foods):
#     #def print_spiciest_foods(spicy_foods):
#    # """Prints foods with heat_level > 5 formatted with pepper emojis"""
#     for food in spicy_foods:
#         if food["heat_level"] > 5:
#             peppers = '' * food["heat_level"]
#             print(f"{food['name']} ({food['cuisine']})  | Heat Level: {peppers}")
#     pass

def get_average_heat_level(spicy_foods):
    total=0
    count =0
    for food in spicy_foods:
        total+= food["heat_level"]
        count+=1
    average=total/ count
    return int(average)
   # print(get_average_heat_level(spicy_foods))
    pass

def create_spicy_food(spicy_foods, new_spicy_food):
    new_list =spicy_foods + [new_spicy_food]
    return new_list
new_food = {
    'name': 'Griot',
    'cuisine':'Haitian',
    'heat_level':10
}
updated_list = create_spicy_food(spicy_foods, new_food)
print(updated_list)
pass
