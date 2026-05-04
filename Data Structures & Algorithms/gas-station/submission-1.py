class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # minus to get a realgas [-1,0,1,-3]
        # starting from largest index?

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start_idx = 0

        for i in range(len(gas)):
            total += gas[i]-cost[i]

            if total < 0:
                start_idx = i+1
                total = 0
        
        return start_idx