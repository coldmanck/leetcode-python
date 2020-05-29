from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''Time: O(m^2*n) Space: O(m^2*n)'''
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        graph = defaultdict(list)
        for word in wordList: # m times
            for i in range(len(word)): # n times
                graph[word[:i] + '*' + word[i + 1:]].append(word) # This takes O(m)!!
        
        queue = deque()
        queue.append((beginWord, 1))
        visited = set([beginWord])
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for neighbor in graph[word[:i] + '*' + word[i + 1:]]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))
                        visited.add(neighbor)
        return 0