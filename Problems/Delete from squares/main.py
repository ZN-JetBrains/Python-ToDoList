key = int(input())
value = squares.get(key, None)

if value is None:
    print("There is no such key")
else:
    print(value)
    del squares[key]

print(squares)
