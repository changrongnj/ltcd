'''
605. Sequence Reconstruction

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 \leq n \leq 10^41≤n≤10
​4
​​ . Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example
Example 1:

Input:org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output:true

'''

'''
Corner case:
[1]
[[],[]]
True
'''


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # reconstruction node count == original count
        # every level needs to be only unique one possibility

        # build graph index + 1 = node
        graph = [[] for _ in range(len(org))]
        indegree = [0 for _ in range(len(org))]
        queue = set([i for i in range(1, len(org) + 1)])  # start point for bfs
        for seq in seqs:
            if len(seq) > 1:
                first, second = seq
                graph[first - 1].append(second)
                if first in queue:
                    queue.remove(first)

        # bfs
        res = []
        queue = list(queue)
        while queue:
            size = len(queue)
            if size != 1:
                return False
            el = queue.pop(0)
            res.append(el)
            for nei in graph[el - 1]:
                indegree[nei - 1] -= 1
                if indegree[nei - 1] == 0:
                    queue.append(nei)

        if len(res) == len(org):
            return True
        return False
