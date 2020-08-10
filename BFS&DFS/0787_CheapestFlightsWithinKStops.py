'''
787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
'''


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if not flights:
            return -1

        # build graph {src: [(dst, dst_price)]}
        graph = {i: [] for i in range(n)}
        for city, stop, price in flights:
            graph[city].append((stop, price))

        if src not in graph or dst not in graph:
            return -1

        # BFS
        queue = [(src, 0)]
        visited = set([src])
        count = 0
        totalprice = float('inf')
        while queue:
            if count > K + 1:
                break
            count += 1
            level = queue
            queue = []
            for node, nprice in level:
                if node == dst:
                    totalprice = min(totalprice, nprice)
                    continue
                if nprice > totalprice:
                    continue
                for neighbor, neiprice in graph[node]:
                    queue.append((neighbor, nprice + neiprice))
                    visited.add(neighbor)

        return totalprice if totalprice != float('inf') else -1
