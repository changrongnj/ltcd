'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1  # from end to start to find first non-"ascending" point
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:  # last permutation already
            return nums.reverse()

        pivot = i - 1
        # largest index that larger/equal to nums[pivot]
        successor = len(nums) - 1
        while successor > pivot and nums[successor] <= nums[pivot]:
            successor -= 1

        nums[pivot], nums[successor] = nums[successor], nums[pivot]  # swap

        # reverse starting non-"ascending" point
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
