'''
792. Number of Matching Subsequences

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
'''

# M1: brute force reduce to binary search
'''
1. build alphabetical dictionary
2. go through each word in the words list
3. for every character appears in the word, first character - identify the minPosition for next character
4. use binary search to find the minPosition if avaiable in the alphabetical dictionary
'''
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:

        # build dictionary of characters in S
        charDict = {}
        for index, char in enumerate(S):
            if char in charDict:
                charDict[char].append(index)
            else:
                charDict[char] = [index]
        
        # travel through every word in words
        # if character in word found in key of charDict, take the smallest
        # occurence of this character, and record the least index for next character
        count = len(words)
        
        for word in words:
            char_first = word[0]
            if char_first in charDict:
                minPos = charDict[char_first][0] + 1
                for i in range(1, len(word)):
                    char_i = word[i]
                    if char_i not in charDict or charDict[char_i][-1] < minPos:
                        count -= 1
                        break
                    else:
                        char_pos = charDict[char_i][bisect_left(charDict[char_i], minPos)]
                        minPos = char_pos + 1
            else:
                count -= 1
                        
        return count


# M2: parrallel the character in each word
'''
1. first character to build dictionary, with key as the character, value as a list of word[i][1:]
2. go through character in S, if match any first character, for every word[i][1:] put to the corresponding first characeter dictionary
'''
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        waiting = {}
        for word in words:
            if word[0] in waiting:
                waiting[word[0]].append(word[1:])
            else:
                waiting[word[0]] = [word[1:]]
        counter = 0
        for char in S:
            if char in waiting:
                length = len(waiting[char])
                for i in range(length):
                    word = waiting[char][i]
                    if word == "":
                        counter += 1
                    else:
                        if word[0] in waiting:
                            waiting[word[0]].append(word[1:])
                        else:
                            waiting[word[0]] = [word[1:]]
                waiting[char] = waiting[char][length:]
        return counter
