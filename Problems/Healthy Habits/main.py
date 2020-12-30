# the list "walks" is already defined
# walks = [
#     {"day": "Monday", "distance": 2000},
#     {"day": "Tuesday", "distance": 3000},
#     {"day": "Wednesday", "distance": 3500},
#     {"day": "Thursday", "distance": 2500},
#     {"day": "Friday", "distance": 2500},
#     {"day": "Saturday", "distance": 1000},
#     {"day": "Sunday", "distance": 5600}]

total_distance = 0
for dictionary in walks:
    total_distance += dictionary.get("distance", 0)
mean = total_distance // len(walks)
print(mean)
