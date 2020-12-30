def get_percentage(real_number, round_digits=None):
    if round_digits is None:
        return str(int(round(real_number * 100))) + "%"
    return str(round(real_number * 100, round_digits)) + "%"


# print(get_percentage(0.0123))
# print(get_percentage(0.0123, 0))
# print(get_percentage(0.0123, 1))
# print(get_percentage(0.0123, 10))
# print(get_percentage(0.0296, 1))
