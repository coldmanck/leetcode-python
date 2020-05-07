class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        length, width = len(matrix), len(matrix[0])
        ans = []
        
        odd = True
        for s in range(width):
            temp_ans = []
            i, j = 0, s
            while j >= 0 and i < length:
                temp_ans.append(matrix[i][j])
                i, j = i + 1, j - 1
            if odd:
                temp_ans.reverse()
            odd ^= True
            ans.extend(temp_ans)
        
        for s in range(1, length):
            temp_ans = []
            i, j = s, width - 1
            while j >= 0 and i < length:
                temp_ans.append(matrix[i][j])
                i, j = i + 1, j - 1
            if odd:
                temp_ans.reverse()
            odd ^= True
            ans.extend(temp_ans)
        
        return ans