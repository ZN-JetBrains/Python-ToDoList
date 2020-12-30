def find_my_list(lists, my_list):
    for i, lst in enumerate(lists):
        # Change the next line
        if my_list is lst:
            return i
    return None
