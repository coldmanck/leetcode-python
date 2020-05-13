class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # brute-force: time O(n^2) space O(1)
        
        # Use hash table: Time O(n) Space O(n)
        targets = set() # target
        for num in arr:
            if num in targets:
                return True
            targets.add(num * 2)
            if num % 2 == 0:
                targets.add(num // 2)
        return False