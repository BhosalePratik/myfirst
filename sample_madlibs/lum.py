def madlib():
    verb1 = input("Verb: ")
    type_of_car = input("Type of car: ")
    luggage = input("Enter Luggage: ")
    state = input("Name of State: ")
    name = input("Name: ")
    direction = input("Enter direction: ")
    favourite_dish = input("Favourite Dish: ")

    madlib = f"On his way {verb1} a {type_of_car} pulled in. There was a roofrack on top, and the {verb1} was " \
             f"piled high with {luggage}. The wagon had {state} plates and the driver,who rolled down his window " \
             f"to ask {name} how to get to US 21 going {direction}, had a New York accent. {name} gave the New York " \
             f"fellow very clear directions on how to get to Highway 21. He also served him and his entire family " \
             f"their {favourite_dish} without even knowing it"
    print(madlib)

