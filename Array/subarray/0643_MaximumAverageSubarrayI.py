'''
643. Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum 
average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
'''


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sumAtIndex, minVal, maxVal = 0, 0, float('-inf')
        sumArr = [0]
        for i in range(len(nums)):
            sumAtIndex += nums[i]
            sumArr.append(sumAtIndex)
            if i >= k - 1:
                maxVal = max(maxVal, sumAtIndex - sumArr[i + 1 - k])

        return maxVal / k
