class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        v=["a","e","i","o","u"]
        lst=s.split()
        count=0
        for c in lst[0]:
            if c in v:
                count+=1
        for i in range(1,len(lst)):
            cu=0
            for c in lst[i]:
                if c in v:
                    cu+=1
            if cu==count:
                lst[i]=lst[i][::-1]
        return " ".join(lst)