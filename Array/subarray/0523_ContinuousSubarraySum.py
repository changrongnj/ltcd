'''
523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Constraints:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''

# corner case: [XX, X, 0, 0,0, X] | k < 0 | k == 0
# dictionary to store remainder not sumAtIndex - because if n*k, n is different, but remove remainder, it works.


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        if not nums or len(nums) < 2:
            return False

        sumAtIndex = 0
        dic = {0: -1}
        for i in range(len(nums)):
            if i > 0 and nums[i] == 0 and nums[i - 1] == 0:
                return True
            sumAtIndex += nums[i]
            if k != 0:
                rem = sumAtIndex % k
                if rem in dic and abs(i - dic[rem]) >= 2:
                    return True
                if rem not in dic:
                    dic[rem] = i
        return False
