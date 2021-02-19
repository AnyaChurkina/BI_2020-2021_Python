import random


'''
Input text without punctuation marks.
'''
old_text = input().split()
shuffle_text = []
for word in old_text:
    if len(word) <= 3:
        shuffle_text.append(word)
    else:
        middle_letters = list(word[1:-1])
        random.shuffle(middle_letters)
        shuffle_text.append(word[0] + ''.join(middle_letters) + word[-1])
print(' '. join(shuffle_text))
