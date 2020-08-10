'''
604. Window Sum

Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, 
find the sum of the element inside the window at each moving.

Example
Example 1

Input：array = [1,2,7,8,5], k = 3
Output：[10,17,20]
Explanation：
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
'''


class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        if not nums:
            return nums

        # if k - 1 > len(nums):  # k = 1,2,3,....k, i = 0,1,2...
        #     return []

        sumAtIndex, sumsArr = 0, [0]
        for i in range(len(nums)):
            sumAtIndex += nums[i]
            sumsArr.append(sumAtIndex)

        i, res = k, []
        while i < len(nums) + 1:
            res.append(sumsArr[i] - sumsArr[i - k])
            i += 1
        return res
