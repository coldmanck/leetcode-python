class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1
            else:
                digits[i] = digits[i] + carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
        return digits if not carry else [1] + digits