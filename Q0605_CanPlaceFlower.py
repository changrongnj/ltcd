'''
605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.


Ans:
1. extend first and end elements as 0s
2. if [i-1] and [i] and [i+1] are 0, thus plant is good!
3. change[i] == 1
4. compare counter and n input
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbedLength = len(flowerbed)
        counter = 0
        flowerbed.insert(0, 0)
        flowerbed.insert(flowerbedLength + 1, 0)
        for i in range(1, flowerbedLength + 1):
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                counter += 1
                flowerbed[i] = 1
        if counter>= n:
            return True
        else:
            return False

 
