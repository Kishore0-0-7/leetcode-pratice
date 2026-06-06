class Solution(object):
    def completePrime(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s=str(num)
        n=len(s)
        for i in range(1,n+1):
            if not self.isprime(int(s[:i])): return False
        for i in range(n):
            if not self.isprime(int(s[i:])): return False
        return True
    def isprime(self,n):
        if n<2: return False
        if n%2==0: return n==2
        r=int(n**0.5)
        for i in range(3,r+1,2):
            if n%i==0: return False
        return True