class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        char_costs={}
        total=0
        for i in range(len(s)):
          char=s[i]
          total+=cost[i]
          if char in char_costs:
              char_costs[char]=cost[i]
          else:
              char_costs[char]=cost[i]
        max_total=max(char_costs.values())
        return total-max_total