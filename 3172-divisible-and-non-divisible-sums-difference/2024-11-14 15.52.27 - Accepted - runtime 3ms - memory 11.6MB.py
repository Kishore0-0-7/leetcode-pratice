class Solution(object):
    def differenceOfSums(self, n, m):
        ae=[i for i in range(n+1)]
        di,ndi=0,0
        for i in ae:
            if(i%m==0):
                di+=i
            else:
                ndi+=i
        return ndi-di
        