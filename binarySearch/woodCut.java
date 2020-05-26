import jdk.internal.perf.Perf.GetPerfAction;

'''
Description
Given n pieces of wood with length L[i] (integer array). 
Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. 
What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

Notice
You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.


Example
For L=[232, 124, 456], k=7, return 114.


Challenge
O(n log Len), where Len is the longest length of the wood.
'''
 public class Solution {

    public int woodCut(int[] L, int k) {
        if (L == null || L.length == 0 || k < 0) {
            return 0;
        }
        int start = 1;
        int end = 1;
        // the max possible length that could cut
        for (int el : L) {
            end = Math.max(end, el);
        }

        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (getPieces(L, mid) >= k) {
                start = mid;
            }
            else {
                end = mid;
            }
        }

        if (getPieces(L, end) >= k) {
            return end;
        }

        if (getPieces(L, start) >= k) {
            return start;
        }
        return 0;
    }

    public int getPieces(int[] L, int length) {
        int count = 0;
        for (int el : L) {
            count += el / length;
        }
        return count;
    }

 }