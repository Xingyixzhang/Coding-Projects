"""Tokenize a string and count unique words."""
from collections import Counter

message = ('This is a sample sentence with couple words '
           'This is more sample words with some more different text')

counter = Counter(message.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

###########################################################################

print('===========================================================')
message = ('This is a sample sentence with couple words '
           'This is more sample words with some more different text')

word_counts = {}

# counting occurrences of each unique word:
for word in message.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(f'\n{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))