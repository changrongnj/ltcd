'''
Q18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

# M1: using 2Sum method
# 1. dictionary with the key is the sum of two numbers, and values are the set of two numbers reach to this sum
# 2. sum up two keys to the target

# M2: using Q15.3Sum
#. two pointers together. the other two pointers are left and right.
#. be careful of duplicates: nums[i] == nums[i-1], nums[j] == nums[j - 1], and nums[left/right] == nums[left +1/right -1]

#M1
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = dict()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum2 = nums[i] + nums[j]
                if sum2 in d:
                    d[sum2].append((i, j))
                else:
                    d[sum2] = [(i, j)]
        res = set()
        for sum2val in d:
            other2val = target - sum2val
            if other2val in d:
                sum2index = d[sum2val]
                other2index = d[other2val]
                for (i, j) in sum2index:
                    for (m, n) in other2index:
                        if i != m and i != n and j != m and j != n:
                            tmp = [nums[i], nums[j], nums[m], nums[n]]
                            tmp.sort()
                            res.add(tuple(tmp))
        return list(res)

#M2
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
            
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                remain = target - nums[i] - nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] > remain:
                        right -= 1
                    elif nums[left] + nums[right] < remain:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1  # keep testing the other two numbers
                        right -= 1
        return res