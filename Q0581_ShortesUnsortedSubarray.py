'''
581. Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

Ans:
1. initialize the beginning and ending of subarray indexes.
In case, the whole array is sorted, thus, end - begin + 1 should be 0.
end = -1, begin = 0.
2. iterate i from beginning to end of the array
3. **** min of array is nums[end], after travel through, should be beginning num,
max of array should be initialized as nums[start = 0].
if set min = nums[0], then if the second ele is bigger, and third is bigger however less than second, cannot be detected.
But, max will needs to be increased one by one.
4. if nums[i] < max, meaning is unsorted. that is END of subarray, assuming the rest is fine
nums[end -1] > min, meaning is unsorted, that is BEGINNING of subarray, assuming before that was fine.
'''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        endUnsorted = -1
        begUnsorted = 0
        maxNum = nums[0]  
        # iterate from beginning to end, the end should be max
        minNum = nums[n - 1]  
        # iterate from end to beginning, the beginning should be min
        
        for i in range(1, n):
            if nums[i] < maxNum:
                endUnsorted = i
            else:
                maxNum = nums[i]
            if nums[n - i - 1] > minNum:
                begUnsorted = n - i - 1
            else:
                minNum = nums[n - i - 1]

        return endUnsorted - begUnsorted + 1
 
