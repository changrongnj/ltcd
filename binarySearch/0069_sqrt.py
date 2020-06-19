# 69. Sqrt(x)
# Implement int sqrt(int x).

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        start = 1
        end = x
        while start + 1 < end:
            mid = math.floor(start + (end - start) / 2)
            if mid > x/mid:
                end = mid
            elif mid < x/mid:
                start = mid
            else:
                return mid
        if end <= x/end:
            return end
        else:
            return start
