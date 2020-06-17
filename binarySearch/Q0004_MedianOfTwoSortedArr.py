'''
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = math.ceil((m + n) / 2)
        if (m + n) % 2 == 1:
            return self.getKth(nums1, nums2, k)
        else:
            median1 = self.getKth(nums1, nums2, k)
            median2 = self.getKth(nums1, nums2, k + 1)
            return (median1 + median2) / 2
    
    def getKth(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.getKth(nums2, nums1, k)
        if m == 0:
            return nums2[k - 1] #kth 's element index is k - 1
        if k == 1:
            return min(nums1[0], nums2[0])
        
        i = min(m, k // 2)
        j = min(n, k // 2)
        if nums1[i - 1] <= nums2[j - 1]:
            return self.getKth(nums1[i:], nums2, k - i)
        else:
            return self.getKth(nums1, nums2[j:], k - j)        