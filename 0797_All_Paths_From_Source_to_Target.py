from collections import OrderedDict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        Solution 1: DFS with stack
        - time: O((2^(V-1) - 1 *) V) = O(2^(V-1) * V)
        - space: O(2^(V-1) * V) # (usually same as time complexity for DFS/BFS)
        '''

        src, des = 0, len(graph) - 1
        stack = [([src], src, set([src]))] # for storing tuples of (path, cur_node, visited)
        all_paths = []
        while stack:
            path, cur_node, visited = stack.pop()
            visited.add(cur_node)
            for neighbor in graph[cur_node]:
                if neighbor in visited:
                    continue
                if neighbor == des:
                    all_paths.append(path + [neighbor])
                else:
                    stack.append((path + [neighbor], neighbor, visited))
            visited.remove(cur_node)
        return all_paths
    
        '''
        Solution 2: DFS with recursion (backtracking)
        - time: O(2^(v-1)-1)
        - space: O(V) in addition to the answer's O(2^(V-1)-1)
        '''
        # src, des = 0, len(graph) - 1
        # results = []
        # def backtrack(path, cur_node):
        #     if cur_node == des:
        #         results.append(path)
        #         return
        #     for neighbor in graph[cur_node]:
        #         backtrack(path + [neighbor], neighbor)
        # backtrack([src], src)
        # return results
    
        '''Solution 3: BFS'''
        # src, des = 0, len(graph) - 1
        # results = []
        # from collections import deque
        # queue = deque([([src], src, set([src]))]) # (path, cur_node, visited)
        # while queue:
        #     path, cur_node, visited = queue.popleft()
        #     visited.add(cur_node)
        #     for neighbor in graph[cur_node]:
        #         if neighbor in visited:
        #             continue
        #         if neighbor == des:
        #             results.append(path + [neighbor])
        #         else:
        #             queue.append((path + [neighbor], neighbor, visited))
        #     visited.remove(cur_node)
        # return results
        
        