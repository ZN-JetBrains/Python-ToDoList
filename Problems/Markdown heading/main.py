def heading(head, level=0):
    if level < 1:
        level = 1
    else:
        if level > 6:
            level = 6
    return "#" * level + " " + head


# print(heading("A"))
# print(heading("A", 3))
# print(heading("A", 1))
# print(heading("A", 0))
# print(heading("A", 10))
