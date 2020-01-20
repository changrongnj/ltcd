'''
697. Degree of an Array

Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency
of any one of its elements.

Your task is to find the smallest possible length of a
(contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6


Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.


Ans:
1. left, right, count - three dictionary to record left position, right position, and total occurence of num
2. if num not in left, left[num] = current index of num
3. right[num] will also be updated to current index of num
4. count[num] will be updated + 1, using count.get(num,0)
5. find max occurence: max(count.values())
6. locate what are all the nums with max occurence, find shortest length.

'''

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        left, right, count = {}, {}, {}
        for index, num in enumerate(nums):
            if num not in left:
                left[num] = index
            right[num] = index
            count[num] = count.get(num, 0) + 1
            
        ans = len(nums)
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)
        
        return ans
