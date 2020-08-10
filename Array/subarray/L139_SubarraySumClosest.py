'''
139. Subarray Sum Closest

Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

Example1
Input: 
[-3,1,1,-3,5] 
Output: 
[0,2]
Explanation: [0,2], [1,3], [1,1], [2,2], [0,4]
Challenge
O(nlogn) time

Notice
It is guaranteed that the sum of any numbers is in [-2^{31},2^{31}-1][−2
​31
​​ ,2
​31
​​ −1].
'''


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):

        # [-3,1,1,3,5] -> [0,-3,-2,-1,-2,1]->subarray i-j = index j - index i-1
        if not nums or len(nums) == 0:
            return

        if len(nums) == 1:
            return [0, 0]

        sumAtIndex = 0
        summ = [(0, -1)]
        for key, val in enumerate(nums):
            sumAtIndex += val
            summ.append((sumAtIndex, key))

        # sort the list of tuple based on their sum at index
        sumSort = sorted(summ, key=lambda el: el[0])

        closest = float('inf')
        res = []
        for i in range(1, len(sumSort)):
            diff = sumSort[i][0] - sumSort[i - 1][0]
            if diff >= closest:
                continue
            else:
                closest = diff
                if sumSort[i][1] < sumSort[i-1][1]:
                    res = [sumSort[i][1] + 1, sumSort[i-1][1]]
                else:
                    res = [sumSort[i - 1][1] + 1, sumSort[i][1]]

        return res
