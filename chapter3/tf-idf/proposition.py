# tasks your code should perform:

# 1. split the text into words, and get a list of unique words that appear in it
# a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
# despite casing) can be done with 
# docs = [line.lower().split() for line in text.split('\n')]

# 2. go over each unique word and calculate its term frequency, and its document frequency

# 3. after you have your term frequencies and document frequencies, go over each line in the text and 
# calculate its TF-IDF representation, which will be a vector

# 4. after you have calculated the TF-IDF representations for each line in the text, you need to
# calculate the distances between each line to find which are the closest.

import numpy as np
import re, math

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def tf_idf(word, doc, docs):
    word_in_doc = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), doc))
    total_words_in_doc = len(doc.split())
    word_in_docs = sum(1 if word in d else 0 for d in docs)
    if word_in_docs != 0:
        return (word_in_doc / total_words_in_doc) * math.log((len(docs) / word_in_docs), 10)
    else:
        return 0

def distance(line1, line2):
    if np.array_equal(np.asarray(line1), np.asarray(line2)):
        return np.inf
    else:
        return sum([abs(line1[i] - line2[i]) for i in range(len(line1))])

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)

    for index, line1 in enumerate(data):
        dist[index] = [distance(line1, line2) for line2 in data]

    return np.unravel_index(np.argmin(dist), dist.shape)


def main(text):
    docs = text.splitlines()
    words = [*set(text.split())]
    N = len(docs)
    M = len(words)
    
    data = np.empty((N, M), dtype = float)

    for i, doc in enumerate(docs):
        data[i] = [tf_idf(w, doc, docs) for w in words]

    print(find_nearest_pair(data))

main(text)
