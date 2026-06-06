class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0: 
            return "0"
        m='0123456789abcdef'
        result=""
        if num<0: 
            num+=2**32
        while num>0:
            digit=num%16
            num=(num-digit)//16
            result+=str(m[digit])
        return result[::-1]