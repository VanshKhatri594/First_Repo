import re
text = "apple banana apple orange banana apple grape orange apple"
word_count = {}

# 1)Print the word with the highest frequency.
# 2)Find and print all words that appear more than once.
# 3)Sort the dictionary based on word frequency in descending order.

# 1)
''' StackOverflow Solutions'''
count = re.findall(r'\w+', text)

for word in count:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"Word with highest frequency : {max(word_count, key=word_count.get)} : {max(word_count.values())}")

# 2)
more_than_once = [word for word, count in word_count.items() if count > 1]
print(f"Words that appeared more than once {more_than_once}")

# 3)
sorted_dict = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(f"Sorted dictionary based on word frequency : {sorted_dict}")