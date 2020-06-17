'''
1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
'''

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # least capacity should be the max of weights[i], otherwise that package even alone cannot be shipped
        # max capacity can be the sum of weights, that shipp all packages in one day
        leastCapacity = 0
        mostCapacity = 0
        for weight in weights:
            leastCapacity = max(leastCapacity, weight)
            mostCapacity += weight
        
        #binary search finding the LEAST weight capacity
        while leastCapacity + 1 < mostCapacity:
            midCapacity = leastCapacity + (mostCapacity - leastCapacity) // 2
            days = self.calculatingDays(weights, midCapacity)
            if days <= D: # could reduce capacity
                mostCapacity = midCapacity
            else:
                leastCapacity = midCapacity
        if self.calculatingDays(weights, leastCapacity) <= D:
            return leastCapacity
        return mostCapacity
            
            
    def calculatingDays(self, weights, capacity):
        days = 1
        capacityRemain = capacity
        for weight in weights:
            if capacityRemain >= weight: 
                capacityRemain -= weight
            else:
                days += 1
                capacityRemain = capacity - weight
        return days