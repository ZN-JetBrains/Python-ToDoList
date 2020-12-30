people = {"Jackie": 176, "Wilson": 185, "Saersha": 165, "Roman": 185, "Abram": 169}


def tallest_people(**kwargs):
    for key, value in sorted(kwargs.items()):
        if value == max(kwargs.values()):
            print(f"{key} : {value}")


# tallest_people(**people)
