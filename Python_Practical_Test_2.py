numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]

dict = {}

for count in numbers:
    if count in dict:
        dict[count] += 1
    else:
        dict[count] = 1

for key, value in dict.items():
    print(f"{key} appears {value} times")