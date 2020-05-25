def maxSumSubmatrix(matrix, k):
    # DP: 2D Kadane's algorithm
    
    def max_subarray(arr, k):
        max_sub = float('-inf')
        min_cum = cur_cum = start = end = 0
        for i, num in enumerate(arr):
            if cur_cum < min_cum:
                min_cum = min(min_cum, cur_cum)
                start = i
            cur_cum += num
            cur_max_sub = cur_cum - min_cum
            if cur_max_sub > k:
                continue
            if cur_max_sub > max_sub:
                max_sub = max(max_sub, cur_max_sub)
                end = i
            if max_sub == k:
                break
        return max_sub, start, end
    
    max_sum = float('-inf')
    left = right = top = down = -1
    for i in range(len(matrix[0])):
        arr = [0] * len(matrix)
        for j in range(i, len(matrix[0])):
            for m in range(len(matrix)):
                arr[m] += matrix[m][j]
            if i == 0 and j == 2:
                import pdb; pdb.set_trace()
            cur_sum, start, end = max_subarray(arr, k)
            if cur_sum > k:
                continue
            elif cur_sum == k:
                return k
            if cur_sum > max_sum:
                max_sum = cur_sum
                left, right, top, down = i, j, start, end
    print(left, right, top, down)
    return max_sum

matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
k = 8
print(maxSumSubmatrix(matrix, k))