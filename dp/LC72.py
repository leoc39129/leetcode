class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Base Cases
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)

        cols = max(len(word1), len(word2))
        dp = [[0]*cols for _ in range(len(word2))]

        end_min = len(word1)
        for row in range(len(dp)):
            track = row
            for col in range(len(dp[0])):
                if col == 0:
                    if word2[row] != word1[0]:
                        dp[row][col] = 1
                    else:
                        track += 1
                else:
                    if track < len(word2) and col < len(word1):
                        if word1[col] == word2[track]:
                            dp[row][col] = dp[row][col-1]
                            track += 1
                        else:
                            dp[row][col] = dp[row][col-1] + 1
                    else:
                        dp[row][col] = dp[row][col-1] + 1

            end_min = min(end_min, dp[row][-1] + (len(word2)-track))
        print(dp)
        return end_min


'''
Valiant effort, but very lost.

The top down approach we tried would have to be a recursion/memoization solution.
The only way to do this problem with dynamic programming is via a bottom up solution:


class Solution(object):
    def minDistance(self, word1, word2):

        # dynamic programming, bottom up
        cache = [[float("inf")]* (len(word2)+1) for _ in range(len(word1)+1)]

        # fill in the bottom row
        for col in range(len(word2)+1): 
            cache[len(word1)][col] = len(word2) - col # base case when word 1 is empty

        # fill in the last column
        for row in range(len(word1)+1): 
            cache[row][len(word2)] = len(word1) - row # base case when word 2 is empty

        for row in range(len(word1) - 1, -1, -1):
            for col in range(len(word2)-1,-1,-1):
                if word1[row] == word2[col]: # char is equal
                    cache[row][col] = cache[row+1][col+1]
                else: # char is not equal
                    cache[row][col] = min(cache[row+1][col],
                                        cache[row][col+1],
                                        cache[row+1][col+1])+1 
                    # check insert, delete, replace, all there directions in the 2d cache array
        # print(cache)
        return cache[0][0]

    

class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        # Create a DP table of size (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters in word1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters in word2
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # Characters match
                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed
                else:
                    # Minimum of insert, delete, or replace
                    dp[i][j] = min(
                        dp[i][j - 1] + 1,  # Insert
                        dp[i - 1][j] + 1,  # Delete
                        dp[i - 1][j - 1] + 1  # Replace
                    )
        
        # The result is in the bottom-right corner of the table
        return dp[m][n]

The table is "flipped" in that usually the bottom up soln will be as the discussion board solution is,
with the answer being in dp[0][0]
'''