class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = cur_gas = start_idx = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                start_idx = i + 1
                cur_gas = 0
        return start_idx if total_gas >= 0 else -1