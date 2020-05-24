class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # time O(nlogn) space O(n)
        if len(hand) % W != 0:
            return False
        from collections import Counter
        c = Counter(hand)
        hand.sort()
        for num in hand:
            if c[num] == 0:
                continue
            for i in range(num, num + W):
                if c[i] > 0:
                    c[i] -= 1
                else:
                    return False
        return True