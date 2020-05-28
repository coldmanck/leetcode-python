from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = list(set(wordList) | set([beginWord]))
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + '*' + word[i + 1:]].append(word)
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