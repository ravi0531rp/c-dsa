from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,time in times:
            graph[u].append((time, v))

        heap = [(0, k)]
        min_times = {}

        while heap:
            time_k_to_i, i = heappop(heap)

            if i in min_times:
                continue
            
            min_times[i] = time_k_to_i

            for nei_time, neighbour in graph[i]:
                if neighbour not in min_times:
                    heappush(heap, (time_k_to_i + nei_time, neighbour))
        if len(min_times) == n:
            return max(min_times.values())
        return -1

        
