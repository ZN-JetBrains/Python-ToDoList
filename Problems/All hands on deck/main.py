cards_dict = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
}

card_list = [input(), input(), input(), input(), input(), input()]
average = 0.0
for card in card_list:
    average += cards_dict[card]
average = average / len(card_list)
print(average)
