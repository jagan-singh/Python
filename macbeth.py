import requests
macbeth = requests.get('http://www.gutenberg.org/cache/epub/2264/pg2264.txt').text

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

# Pseudo-code outline
words = macbeth.split()
counting = {}
for word in words:
    if word in counting:
        counting[word] += 1
    else:
        counting[word] = 1

sort_words = sorted(counting.items(), key = lambda x : x[1], reverse = True)

y = []
labels = []
for i in range(26):
    y.append(sort_words[i][1])
    labels.append(sort_words[i][0])

x = np.arange(len(y))
plt.figure(figsize =(15, 10))
plt.bar(x, y)
plt.title('Project: Analyzing Macbeth')
plt.ylabel('Number of Words')
plt.xlabel('Words')
plt.xticks(x, labels)
plt.show()

# Split the transcript into words
# Create a dictionary
# Iterate through the text of Macbeth
# Update word counts
# Sort words by counts in descending order
# Create Bar Graph
# Include descriptive titles and labels
