class Solution(object):
    def sq(self,n):
            p=0
            while n!=0:
                p+=(n%10)**2
                n/=10
            return p
    def isHappy(self, n):
        h=set()
        while n not in h:
            h.add(n)
            n=self.sq(n)
            if n==1:
                return True
        return False
        