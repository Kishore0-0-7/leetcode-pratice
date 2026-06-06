class Solution(object):
    def minimumTime(self, d, r):
        """
        :type d: List[int]
        :type r: List[int]
        :rtype: int
        """
        d1,d2=d
        r1,r2=r
        queue=deque()
        queue.append((0,d1,d2))
        visited=set()
        while queue:
            t,d1left,d2left=queue.popleft()
            if d1left==0 and d2left==0:
                return t
            if (t,d1left,d2left) in visited:
                continue
            visited.add((t,d1left,d2left))
            t+=1
            can1=(t%r1!=0 and d1left>0)
            can2=(t%r2!=0 and d2left>0)
            if can1:
                queue.append((t,d1left-1,d2left))
            if can2:
                queue.append((t,d1left,d2left-1))
            if not can1 and not can2:
                queue.append((t,d1left,d2left))