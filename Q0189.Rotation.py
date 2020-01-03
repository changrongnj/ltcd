'''
Q189.
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method 1:
        swapIndex = 0
        for i in range(1, len(nums)):
            rotateIndex = (i * k) % len(nums) + swapIndex
            nums[swapIndex], nums[rotateIndex] = nums[rotateIndex], nums[swapIndex]
            if rotateIndex == swapIndex:
                swapIndex += 1

        # method 2:
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        # nums[:] is important!  nums = is wrong because it is a new list

        # method 3:
        # 三次翻转法, python needs to write inplace reverse function, because
        # it does not include ending which cause the problem when
        # length of list == k, e.g., [1,2] k = 2, output will be [1,2,1,2]
        def inplaceReverse(self, nums, start, end):
            for i in range(0, (end-start)//2+1):
                nums[start + i], nums[end - i] = nums[end - i], nums[start + i]
    
        def rotate(self, nums: List[int], k: int) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            if len(nums) == 0:
                return
            else:
                k = k % len(nums)
                self.inplaceReverse(nums, 0, len(nums) - k - 1)
                self.inplaceReverse(nums, len(nums) - k, len(nums) - 1)
                self.inplaceReverse(nums, 0, len(nums) - 1)

        
        
