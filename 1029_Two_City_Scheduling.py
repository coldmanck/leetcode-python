class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # def helper(countA, countB, idx, cur_cost):
        #     if idx == len(costs):
        #         return cur_cost
        #     if countA < len(costs) // 2 and countB < len(costs) // 2:
        #         return min(helper(countA + 1, countB, idx + 1, cur_cost + costs[idx][0]), 
        #                    helper(countA, countB + 1, idx + 1, cur_cost + costs[idx][1]))
        #     return cur_cost + sum([costs[i][0] for i in range(idx, len(costs))]) if countA < len(costs) // 2 else cur_cost + sum([costs[i][1] for i in range(idx, len(costs))])
        # return helper(0, 0, 0, 0)
        
        a_minus_b = sorted([(a - b, a, b) for a, b in costs])
        return sum([cost[1] for cost in a_minus_b[:len(costs)//2]] + [cost[2] for cost in a_minus_b[len(costs)//2:]])