class Solution(object):
    def findMinFibonacciNumbers(self, k):
        fib=[1,1]
        i=0
        while fib[-1]<k:
            fib.append(fib[-1]+fib[-2])
        i=0
        fib.reverse()
        for el in fib:
            if k>=el:
                k=k-el
                i+=1
            if k==0:
                break
        return i