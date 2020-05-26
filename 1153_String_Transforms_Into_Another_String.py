# 1153. String Transforms Into Another String

class Solution:
    def canConvert(self, str1, str2):
        if len(str1) != len(str2) or (str1 != str2 and len(set(str1)) == len(set(str2)) == 26):
            return False
        map = {} # key of ch in str1 : value of ch in str2
        for i in range(len(str1)):
            if str1[i] not in map:
                map[str1[i]] = str2[i]
            else:
                if map[str1[i]] != str2[i]:
                    return False
        return True

sol = Solution()

str1 = "aabcc"
str2 = "ccdee"
print(sol.canConvert(str1, str2)) # True

str1 = "leetcode"
str2 = "codeleet"
print(sol.canConvert(str1, str2)) # False

str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "bcdefghijklmnopqrstuvwxyza"
print(sol.canConvert(str1, str2)) # False

str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "bbcdefghijklmnopqrstuvwxyz"
print(sol.canConvert(str1, str2)) # True

str1 = "aa"
str2 = "cd"
print(sol.canConvert(str1, str2)) # False