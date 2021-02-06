import random
'''
You can input text with simple punctuation: ".", ",", ";", ":", "!", "?"
'''
old_text = input().split()
punctuations = (".", ",", ";", ":", "!", "?")
shuffle_text = []
for word in old_text:
    if word.endswith(punctuations):
        if len(word) <= 4:
            shuffle_text.append(word)
        else:
            middle_letters = list(word[1:-2])
            random.shuffle(middle_letters)
            shuffle_text.append(word[0] + ''.join(middle_letters) + word[-2:])
    else:
        if len(word) <= 3:
            shuffle_text.append(word)
        else:
            middle_letters = list(word[1:-1])
            random.shuffle(middle_letters)
            shuffle_text.append(word[0] + ''.join(middle_letters) + word[-1])

print(' '.join(shuffle_text))

'''
Input text: Murphys Law does not mean that something bad will happen, what it means is whatever can happen will happen.
Output text: Mhpyrus Law does not maen that sotmhineg bad will hpeapn, waht it manes is wveaehtr can hpaepn will hpepan.

Interstellar <3
'''