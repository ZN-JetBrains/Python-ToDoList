# use the function blackbox(lst) that is already defined
original_list = [1, 2, 3]
original_id = id(original_list)
new_list = blackbox(original_list)
new_id = id(new_list)

if original_id == new_id:
    print("modifies")
else:
    print("new")
