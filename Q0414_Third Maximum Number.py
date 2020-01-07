'''
414
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

class Solution:
    # method 1: set to remove duplicates, and pop the two max, return max of rest
    def thirdMax(self, nums: List[int]) -> int:
        dupsRemoved = set()
            for val in nums:
                dupsRemoved.add(val)
            if len(dupsRemoved) < 3:
                return max(dupsRemoved)
            else:
                dupsRemoved.remove(max(dupsRemoved))
                dupsRemoved.remove(max(dupsRemoved))
                return max(dupsRemoved)
    # method 2: initialize the first three max, travel through the list;
    #           if reps cause not fulfill three max, return max of nums
    def thirdMax(self, nums: List[int]) -> int:
        maxLst = [-float("inf"), -float("inf"), -float("inf")]
        for i in range(len(nums)):
            if nums[i] > maxLst[0]:
                maxLst[0], maxLst[1], maxLst[2] = nums[i], maxLst[0], maxLst[1]
            elif nums[i] < maxLst[0] and nums[i] > maxLst[1]:
                maxLst[1], maxLst[2] = nums[i], maxLst[1]
            elif nums[i] < maxLst[1] and nums[i] > maxLst[2]:
                maxLst[2] = nums[i]
        if -float("inf") in maxLst:
            return max(nums)
        else:
            return maxLst[2]
                
        
