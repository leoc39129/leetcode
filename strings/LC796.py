class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        
        if(len(s) != len(goal)):
            return False
        s_arr = list(s)
        
        for k in range(0, len(s_arr)):
            s_arr = list(s_arr[1:]) + list(s_arr[0])
            s_str = "".join(s_arr)
            if s_str == goal:
                return True
        return False

        # Slow solution, 
        """
        return len(s) == len(goal) and goal in s+s


