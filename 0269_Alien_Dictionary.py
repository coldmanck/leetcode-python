class Solution:
    def alienOrder(self, words: List[str]) -> str:
        from collections import defaultdict, deque
        graph = defaultdict(set)
        # in_deg = defaultdict(int)
        in_deg = {ch:0 for ch in set([ch for word in words for ch in word])}
        
        for first_word, second_word in zip(words, words[1:]):
            for a, b in zip(first_word, second_word):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        in_deg[b] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""
        
        topo_order = []
        queue = deque([k for k, v in in_deg.items() if v == 0])
        # print(graph)
        # print(in_deg)
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for nbr in graph[node]:
                in_deg[nbr] -= 1
                if in_deg[nbr] == 0:
                    queue.append(nbr)
        
        print(in_deg)
        print(topo_order)
        return ''.join(topo_order) if len(topo_order) == len(in_deg) else ''