class Solution(object):
    def minimumTime(self, d, r):
        """
        :type d: List[int]
        :type r: List[int]
        :rtype: int
        """
        d1,d2=d
        r1,r2=r
        def gcd(a,b):
            return a if b==0 else gcd(b,a%b)
        def lcm(a,b):
            return (a*b)//gcd(a,b)
        def cancomp(t):
            av1=t-t//r1
            av2=t-t//r2
            # br=t//lcm(r1,r2)
            # ta=t-br
            if av1<d1 or av2<d2:
                return False
            bb=t//lcm(r1,r2)
            #ol=t-t//r1-t//r2+t//lcm(r1,r2)
            md=t-bb
            return md>=d1+d2            
        left,right=1,2*(d1+d2+max(r1,r2))
        
        while left<right:
            mid=(left+right)//2
            if cancomp(mid):
                right=mid
            else:
                left=mid+1
        return left
        # queue=deque()
        # queue.append((0,d1,d2))
        # visited=set()
        # while queue:
        #     t,d1left,d2left=queue.popleft()
        #     if d1left==0 and d2left==0:
        #         return t
        #     if (t,d1left,d2left) in visited:
        #         continue
        #     visited.add((t,d1left,d2left))
        #     t+=1
        #     can1=(t%r1!=0 and d1left>0)
        #     can2=(t%r2!=0 and d2left>0)
        #     if can1:
        #         queue.append((t,d1left-1,d2left))
        #     if can2:
        #         queue.append((t,d1left,d2left-1))
        #     if not can1 and not can2:
        #         queue.append((t,d1left,d2left))