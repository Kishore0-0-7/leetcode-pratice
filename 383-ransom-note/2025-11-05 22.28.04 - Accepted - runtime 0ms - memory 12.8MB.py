class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        alphabet=[0]*26
        for c in ransomNote:
            idx=ord(c)-ord('a')
            i=magazine.find(c,alphabet[idx])
            if i==-1:
                return False
            alphabet[idx]=i+1
        return True