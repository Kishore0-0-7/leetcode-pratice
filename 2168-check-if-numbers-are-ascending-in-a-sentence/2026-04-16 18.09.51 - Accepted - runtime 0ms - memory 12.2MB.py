class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev=-1
        for ch in s.split(" "):
            if ch.isdigit():
                if int(ch)<=prev:
                    return False
                prev=int(ch)
        return True