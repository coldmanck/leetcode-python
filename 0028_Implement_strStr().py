class Solution:
    def strStr(self, haystack, needle):
        def compute_fail_func(needle):
            fail_func = [0]
            i, j = 1, 0
            n_prefix = 0
            while i < len(needle):
                while i < len(needle) and needle[i] == needle[j]:
                    n_prefix += 1
                    fail_func.append(n_prefix)
                    i, j = i + 1, j + 1
                n_prefix = 0
                fail_func.append(n_prefix)
                i, j = i + 1, 0
            return fail_func
        
        fail_func = compute_fail_func(needle)
        # print(fail_func)
        i, j = 0, 0
        while i < len(haystack):
            orig_i = i
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[i]:
                i, j = i + 1, j + 1
            if i == len(haystack):
                return -1
            if j == len(needle):
                return orig_i
            if j > 0:
                j = fail_func[j - 1]
        return -1
    
    # Time O(nm)
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if not needle:
    #         return 0
    #     for i in range(len(haystack)):
    #         j, k = i, 0
    #         while j < len(haystack) and k < len(needle) and haystack[j] == needle[k]:
    #             j, k = j + 1, k + 1
    #         if k == len(needle):
    #             return i
    #         if j == len(haystack):
    #             return -1
    #     return -1

sol = Solution()
haystack = 'atcamalgamaokvlfpeifjvnbdfs'
needle = 'amalgamation'
sol.strStr(haystack, needle)