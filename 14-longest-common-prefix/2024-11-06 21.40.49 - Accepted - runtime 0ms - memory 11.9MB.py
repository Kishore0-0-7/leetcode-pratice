class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return "" 
        ml = min(len(s) for s in strs)
        common_prefix = ""
        for i in range(ml):
            current_char = strs[0][i]
            for string in strs:
                if string[i] != current_char:
                    return common_prefix
                    break
            common_prefix += current_char
        return common_prefix