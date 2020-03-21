'''
167. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

#1 two pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]

#M2 = TwoSum -64ms -68.35%
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for index, n1 in enumerate(numbers):
            n2 = target - n1
            if n2 in res:
                return [res[n2], index + 1]
            res[n1] = index + 1

#M3 = binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, n1 in enumerate(numbers):
            n2 = target - n1
            l = index + 1
            r = len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == n2:
                    return [index + 1, mid + 1]
                elif numbers[mid] < n2:
                    l = mid + 1
                else:
                    r = mid - 1
