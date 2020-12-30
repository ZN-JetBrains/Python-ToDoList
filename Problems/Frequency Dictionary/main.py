# put your python code here
words = input().lower().split()
frequency_dict = {}

for word in words:
    if word not in frequency_dict:
        frequency_dict[word] = words.count(word)

for key, value in frequency_dict.items():
    print(f"{key} {value}")
