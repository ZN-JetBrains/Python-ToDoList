# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
num_groups = int(input())
group_dict = {}
index = 0
for _ in range(len(groups)):
    if index < num_groups:
        group_dict[groups[index]] = int(input())
    else:
        group_dict[groups[index]] = None
    index += 1
print(group_dict)
