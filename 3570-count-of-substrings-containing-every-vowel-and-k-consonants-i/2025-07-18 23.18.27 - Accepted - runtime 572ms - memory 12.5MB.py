class Solution(object):
    def countOfSubstrings(self, s, k):
        ans = 0
        n = len(s)
        for i in range(n):
            a = e = i_count = o = u = c = 0
            
            for j in range(i, n):
                if s[j] == 'a':
                    a += 1
                elif s[j] == 'e':
                    e += 1
                elif s[j] == 'i':
                    i_count += 1
                elif s[j] == 'o':
                    o += 1
                elif s[j] == 'u':
                    u += 1
                else:
                    c += 1
                    
                    
                if a > 0 and e > 0 and i_count > 0 and o > 0 and u > 0 and c == k:
                    ans += 1

        return ans       