class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        i=0
        count=0
        number=str(num)
        while i<len(number):
            if i+k<=len(number):
                s=number[i:i+k]
                if int(s)!=0 and num% int(s)==0:
                    count+=1
                i+=1
            else:
                break
        return count