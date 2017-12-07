import collections

# The following assumes that we already have the text file on disk.
# Start by splitting the file into lowercase words.
k = 10
words = open('data.txt').read().lower().split()

# Get the set of unique words.

# Make a list of (count, unique) tuples.

count = collections.Counter(words)
candidates = count.keys()
candidates.sort(key = lambda w: (-count[w], w))
for word in candidates[:k]:
    print word

#
# counts = []
# for unique in uniques:
#   count = 0              # Initialize the count to zero.
#   for word in words:     # Iterate over the words.
#     if word == unique:   # Is this word equal to the current unique?
#       count += 1         # If so, increment the count
#   counts.append((count, unique))
#
# counts.sort()            # Sorting the list puts the lowest counts first.
# counts.reverse()         # Reverse it, putting the highest counts first.
# # Print the 50k words with the highest counts.
# for i in range(min(50000, len(counts))):
#   count, word = counts[i]
#   print('%s' % word)
