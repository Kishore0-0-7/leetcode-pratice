class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        sb=['a']
        while len(sb)<k:
            size=len(sb)
            for i in range(size):
                nc=chr(ord('a')+((ord(sb[i]) - ord('a')+1) % 26))
                sb.append(nc)
        return sb[k - 1]
