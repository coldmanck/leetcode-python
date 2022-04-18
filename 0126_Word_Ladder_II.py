class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # improved BFS 
        # time complexity: O(N * M^2)
        if endWord not in wordList:
            return []
        
        from collections import defaultdict
        graph = defaultdict(set)
        for word in wordList: # O(N)
            for i in range(len(word)): # O(M)
                graph[word[:i] + '*' + word[i + 1:]].add(word) # O(M)
        
        from collections import deque
        queue = deque()
        queue.append((beginWord, [beginWord]))
        visited = set()
        min_len = float('inf')
        ans = []
        while queue: # O(N)
            word, path = queue.popleft()
            visited.add(word)
            if len(path) > min_len:
                continue
            if word == endWord:
                min_len = len(path)
                ans.append(path)
            for i in range(len(word)): # O(M)
                for neighbor in graph[word[:i] + '*' + word[i + 1:]]: # O(M)
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return ans