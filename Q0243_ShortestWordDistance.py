'''
243.Shortest Word Distance
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

def shortWordDistance(words, word1, word2):
    wordsDct = {}
    for index, word in enumerate(words):
        if word not in wordsDct:
            wordsDct[word] = [index]
        else:
            wordsDct[word].append(index)
    posWord1 = wordsDct.get(words1)
    posWord2 = wordsDct.get(words2)
    
    shortest = float("inf")
    i = 0
    j = 0
    while i < len(posWord1) and j < len(posWord2):
        if posWord1[i] < posWord2[j]:
            shortest = min(shortest, posWord2[j] - posWord1[i])
            i += 1
        else:
            shortest = min(shortest, posWord1[i] - posWord2[j])
            j += 1
    return shortest
