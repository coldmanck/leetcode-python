class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        ans = 0
        processing = False
        sign = 1
        while i < len(str):
            if not processing:
                if str[i] != ' ':
                    if str[i] == '+' or str[i] == '-' or 0 <= ord(str[i]) - ord('0') <= 9:
                        processing = True
                        if str[i] == '-':
                            sign = -1
                        elif 0 <= ord(str[i]) - ord('0') <= 9:
                            ans = ord(str[i]) - ord('0')
                    else:
                        return 0
            else:
                if 0 <= ord(str[i]) - ord('0') <= 9:
                    ans = ans * 10 + ord(str[i]) - ord('0')
                else:
                    return sign * ans
                if sign * ans > (1 << 31) - 1:
                    return (1 << 31) - 1
                elif sign * ans < -(1 << 31):
                    return -(1 << 31)
            i += 1
        return sign * ans