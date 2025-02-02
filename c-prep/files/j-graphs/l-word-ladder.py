from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        graph = defaultdict(list)

        for word in wordList:
            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index+1:]
                graph[pattern].append(word)

        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        res = 1
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                if curr_node == endWord:
                    return res

                for index in range(len(curr_node)):
                    pattern = curr_node[:index] + "*" + curr_node[index+1:]
                    for nei in graph[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            
            res += 1
        
        return 0
