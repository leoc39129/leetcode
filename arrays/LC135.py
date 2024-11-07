class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Base Case:
        if len(ratings) == 1:
            return 1

        candies = [1]*len(ratings)

        if ratings[0] > ratings[1]:
            candies[0] += 1
        for idx in range(1, len(ratings)-1):
            if ratings[idx] > ratings[idx-1] or ratings[idx] > ratings[idx+1]:
                candies[idx] += candies[idx-1]

        if ratings[-1] > ratings[-2]:
            candies[-1] += candies[-2]
        
        return sum(candies)

        
'''
Got through half of the test cases, but didn't get the problem conceptually -- it is a LC hard.
It was a good attempt, it just didn't click. These won't be what you come across in interviiews most of the time.
Failed to realize this is an optimization problem - in the future, if you get another, there is a greedy approach!

Here's a very conceptually easy to understand solution. Go from the left and from the right determining how many
candies each kid should get, take the max of each index, sum it together and you've got your answer

RT: O(n)
Space: O(n)

class Solution:
    def candy(self, ratings):
        n = len(ratings)
        left = [1] * n
        right = [1] * n

        # Fill the left array
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # Fill the right array
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        # Calculate the total candies needed
        ans = sum(max(left[i], right[i]) for i in range(n))

        return ans



Here's a discussion board solution, using the concept of peaks and valleys, not tracking how many
candies go to each kid, but rather keeping track of the total candies distributed. Clever soln

RT: O(n)
Space: O(1)

class Solution:
    def candy(self, ratings):
        n = len(ratings)
        total_candies = n
        i = 1

        while i < n:
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue

            current_peak = 0
            while i < n and ratings[i] > ratings[i - 1]:
                current_peak += 1
                total_candies += current_peak
                i += 1
            
            if i == n:
                return total_candies

            current_valley = 0
            while i < n and ratings[i] < ratings[i - 1]:
                current_valley += 1
                total_candies += current_valley
                i += 1

            total_candies -= min(current_peak, current_valley)

        return total_candies
'''