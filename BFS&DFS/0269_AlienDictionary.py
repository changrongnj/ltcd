'''
LintCode 892. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"

Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
Notice
You may assume all letters are in lowercase.
The dictionary is invalid, if a is prefix of b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order
'''


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here

        if len(words) < 2:
            return ""

        '''
        find the first different letter between two words
        '''
        def locateFirstDiff(w1, w2):
            i = 0
            size = min(len(w1), len(w2))
            while i < size:
                l1Code = ord(w1[i])
                l2Code = ord(w2[i])
                if l1Code == l2Code:
                    i += 1
                else:
                    return [chr(l1Code), chr(l2Code)]
            if len(w1) < len(w2):
                return [" ", w2[len(w1)]]
            return []

        wordsOrder = []
        for i in range(len(words) - 1):
            diff = locateFirstDiff(words[i], words[i + 1])
            if diff:
                wordsOrder.append(diff)

        if not wordsOrder:
            return ""
        '''
        find all letters in the word list
        '''
        def findAllLetters(lst):
            visited = set()
            for word in lst:
                for letter in word:
                    if letter not in visited:
                        visited.add(letter)
            return visited

        letters = findAllLetters(words)

        # build graph {letter : [next letters]}
        wordsGraph = {letter: [] for letter in letters}
        indegree = {letter: 0 for letter in letters}
        for first, second in wordsOrder:
            if first != " ":
                wordsGraph[first].append(second)
                indegree[second] += 1

        # BFS
        queue, res = [], []
        for letter in indegree:
            if indegree[letter] == 0:
                queue.append(letter)

        while queue:
            queue.sort()
            letter = queue.pop(0)
            res.append(letter)
            for nextLetter in wordsGraph[letter]:
                print(letter, nextLetter)
                indegree[nextLetter] -= 1
                if indegree[nextLetter] == 0:
                    queue.append(nextLetter)

        if len(res) == len(letters):
            return "".join(res)
        return ""
