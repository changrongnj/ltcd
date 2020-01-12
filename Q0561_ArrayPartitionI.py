'''
561. Array Partition I

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].


Ans:
1. creates 20001 buckets that store every element that equals to index + 10000
(-10000 ~ 10000, index is 0 ~ 20000)
2. travel through the bucket;
3. set another boolean variable - odd; because every first element of two is the
min of two, therefore odd = True, meaning this number will be used for sum up.
'''

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        bucket = [0] * 20001 #for use of index
        for num in nums:
            bucket[num + 10000] += 1
            # occurence of element in the list
        
        odd = True
        res = []
        i = 0
        while i < len(bucket):
            if bucket[i] > 0:
                if odd == True:
                    res.append(i - 10000)
                bucket[i] -= 1
                odd = not odd
            else:
                i += 1
        return sum(res)
