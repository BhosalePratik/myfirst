def madlib():
    time_of_day = input("Time of Day: ")
    body_part_plural = input("Body Part (plural): ")
    color = input("color: ")
    verb_past_tense = input("Verb (past tense): ")
    food = input("Food: ")
    noun1 = input("Noun: ")
    noun_plural_1 = input("Noun (plural): ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")

    madlib = f"It was a {adj1}summer {time_of_day} when we realized that the medicine to stop" \
             f"spread of the disease did not work. Instead, it produces ZOMBIES!!! They were thirsty for" \
             f"{body_part_plural} and the streets were lined with these monsters holding " \
             f"{noun_plural_1} in their hands. Their eyes were {color} with hunger as they {verb_past_tense}" \
             f"around the city looking for {food}. They were {adj2} and {adj3}, unknowing how to act in this human " \
             f"world...except eat {body_part_plural}!!!! That was their sole mission and they were dedicated towards" \
             f"achieving it for the sake of {noun1}."
    print(madlib)

