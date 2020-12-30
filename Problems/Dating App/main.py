def select_dates(potential_dates):
    potentials = []
    for dictionary in potential_dates:
        if dictionary["age"] > 30 and "Berlin" in dictionary.values() and "art" in dictionary["hobbies"]:
            potentials.append(dictionary["name"])
    return ", ".join(potentials)
