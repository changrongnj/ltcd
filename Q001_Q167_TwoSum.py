'''
Q01
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):

    def twoSum(self, nums, target):
    
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = {}  #convert nums to dictionary for retrieve
        for index, num in enumerate(nums): #iterate the nums(list)
            num2 = target - num  #the complement num
            if num2 in numsDict:  #if the complement num already visited(stored)
                return(numsDict[num2], index)  #indexs for complement and current
            else:
                numsDict[num] = index  #if not, stored the visited num
                
 
'''
Q167
167. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        remainsDct = {}
        for index, number in enumerate(numbers, start = 1):
            if target - number in remainsDct:
                return remainsDct[target - number], index
            else:
                remainsDct[number] = index 
