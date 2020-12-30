# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
# test_dict = {"a": 43, "b": 1233, "c": 8}

# Work with the 'test_dict'
values = test_dict.values()
minimum = min(values)
maximum = max(values)

min_key = None
max_key = None

for key, value in test_dict.items():
    if value == minimum:
        min_key = key
    if value == maximum:
        max_key = key

print(f"min: {min_key}")
print(f"max: {max_key}")
