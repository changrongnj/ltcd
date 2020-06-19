'''
719. Find K-th Smallest Pair Distance
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums_sort = sorted(nums)
        #find smallest distance and largest distance
        small = 0
        large = nums_sort[n - 1] - nums_sort[0]
        while small < large:
            mid = small + (large - small) // 2
            j = 0
            count = 0
            for i in range(n):
                while j < n and nums_sort[j] - nums_sort[i] <= mid:
                    j += 1
                count += (j - i - 1)
            if count < k:
                small = mid + 1
            else:
                large = mid
        return small