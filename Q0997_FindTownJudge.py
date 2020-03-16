'''
997. Find the Town Judge
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
'''

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted = [0] * (N + 1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1
        for i in range(1, N + 1):
            if trusted[i] == N - 1:  # N people judge gets N-1 trusts
                return i
        return -1