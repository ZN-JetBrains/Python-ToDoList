# the list "meals" is already defined

sum_ = 0
for dictionary in meals:
    sum_ += dictionary.get("kcal", 0)
print(sum_)
