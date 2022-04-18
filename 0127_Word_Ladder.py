class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        # N: len(wordList)
        # M: length of maximum words in wordList or beginWord
        # time complexity: O(N^2 * M)
        '''
        if endWord not in wordList:
            return 0
        
        def is_neighbor(word1, word2):
            count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    count += 1
                if count > 1:
                    return False
            return True if count == 1 else False
        
        # construct graph adjacency list
        from collections import defaultdict
        graph = defaultdict(set)
        for word in wordList: # O(N)
            if is_neighbor(beginWord, word): # O(M)
                graph[beginWord].add(word)
        for i in range(len(wordList)): # O(N)
            for j in range(i + 1, len(wordList)): # O(N)
                word1, word2 = wordList[i], wordList[j]
                if is_neighbor(word1, word2): # O(M)
                    graph[word1].add(word2)
                    graph[word2].add(word1)
        
        # BFS
        from collections import deque
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        while queue:
            s, dist = queue.popleft()
            if s == endWord:
                return dist
            for neighbor in graph[s]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return 0
        '''
        
        # improved BFS 
        # time complexity: O(N * M^2)
        # Runtime: 139 ms, faster than 90.39% of Python3 online submissions for Word Ladder.
        # Memory Usage: 19.7 MB, less than 7.29% of Python3 online submissions for Word Ladder.
        if endWord not in wordList:
            return 0
        
        from collections import defaultdict
        graph = defaultdict(set)
        for word in wordList: # O(N)
            for i in range(len(word)): # O(M)
                graph[word[:i] + '*' + word[i + 1:]].add(word) # O(M)
        
        from collections import deque
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        while queue: # O(N)
            word, dist = queue.popleft()
            ''' 
            The `visited` array can also be updated here but will be much slower
            as it's essentially adding all possible paths to the queue instead of the shortest
            '''
            # visited.add(word) 
            if word == endWord:
                return dist
            for i in range(len(word)): # O(M)
                for neighbor in graph[word[:i] + '*' + word[i + 1:]]: # O(M)
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
        return 0