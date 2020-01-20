'''
674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers, find the length of
longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5],
its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not
a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2],
its length is 1. 
Note: Length of the array will not exceed 10,000.


Ans:
1. iterate the list - nums
2. initialize a variable ans - records the longest subarray so far;
another variable counter - count the continuous numbers in this sequence
3. be careful of empty array.

'''

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            res = 1
            counter = 1
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    counter = 1
                else:
                    counter += 1
                    res = max(res, counter)
            return res
