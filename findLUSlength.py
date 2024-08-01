

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        for x in range(len(strs) - 1):
            count = 0
            eq = 0
            idx = 0
            ltr = 0

            if strs[x] == strs[x + 1]:
                count += 1
                print("eq")
                
            elif len(strs[x]) != len(strs[x+1]):
                if len(strs[x]) > len(strs[x+1]):
                    idx = x
                    min_st = len(strs[x])
                    ltr = strs[x+1][0]
                    opp_idx = x + 1
                else:
                    idx = x + 1
                    min_st = len(strs[x+1])
                    ltr = strs[x][0]
                    opp_idx = x
                
                # find what index shorter string's [0] is in the longer str
                str_idx = strs[idx].index(ltr)

                for l in range(str_idx, len(strs[opp_idx])):        # we need the opposite of idx
                    if strs[x][l] == strs[x+1][l]:
                        eq += 1
                if eq == len(strs[opp_idx]):
                    print("yes")
                    count += 1

                #print(eq)
                #print(len(strs[opp_idx]))
            #print(strs[x][0] == strs[x+1][0])
        #print(count)
        temp = (count == len(strs) - 1)
        if temp:
            return -1
        else:
            return len(strs[0])
