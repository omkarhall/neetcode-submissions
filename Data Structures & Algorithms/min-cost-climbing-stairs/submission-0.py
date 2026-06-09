class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #def helper(i, cur):
            #if i >= len(cost):
                #return cur
            #return min(helper(i+1,cur+cost[i]), helper(i+2,cur+cost[i]))
        #return min(helper(0,0), helper(1,0))
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])

        