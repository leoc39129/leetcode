class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Base Case:
        if len(gas) == 1:
            if gas[0] < cost[0]:
                return -1 
            else:
                return 0
        
        poss_starts = []
        for idx in range(len(gas)):
            if gas[idx] >= cost[idx]:
                poss_starts.append(idx)

        return self.check_starts(gas, cost, poss_starts)

    def check_starts(self, gas, cost, starts):
        tank = 0
        n = len(gas)

        print(starts)

        for idx in starts:
            tank = 0
            print("idx")
            print(idx)
            temp = idx
            tank += gas[idx]
            tank -= cost[idx]
            temp += 1
            complete = False

            while temp != idx:
                print(tank)
                if temp == n:
                    temp = 0
                tank += gas[temp]
                tank -= cost[temp]
                if tank < 0:
                    break
                temp += 1
                if temp == n:
                    temp = 0
                if temp == idx:
                    complete = True

            if complete:
                return idx

        return -1


'''
Not the full 45 mins on this attempt, come back to it

Not sure if this is Kadane's algorithm but some of the posts say it is
Missed the insight that if the sum of the gas is less than the sum of
costs, then the journey isn't possible. You don't need to traverse the 
solution from the starting index to the finish!

Discussion board solution:

class Solution:
    def canCompleteCircuit(self, gas, cost):
        #gas =  [2,3,4]
        #cost = [3,4,3]
        #total =-1,-1,1
        #sum of gas>= sum cost array
        sum_cost = sum(cost)
        sum_gas = sum(gas)
        # Check if it is possible to complete the journey
        if sum_cost > sum_gas:
            return -1

        current_gas = 0
        starting_index = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                starting_index = i + 1
        return starting_index
        
'''