from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx, eq in enumerate(equations):
            a, b = eq
            graph[a].append((b, values[idx]))
            graph[b].append((a, 1/values[idx]))

        def calculate(query):
            src, dst = query
            if src not in graph or dst not in graph:
                return -1
            queue = deque([(src, 1)])
            visited = set()
            visited.add(src)

            while queue:
                node, weight = queue.popleft()
                if node == dst:
                    return weight
                for neigh, neigh_wt in graph[node]:
                    if neigh not in visited:
                        queue.append((neigh, neigh_wt*weight))
                        visited.add(neigh)
            return -1
        
        results = [calculate(query) for query in queries]
        return results

