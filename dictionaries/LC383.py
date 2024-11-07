class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        mydict = {}
        for ch in range(len(magazine)):
            if magazine[ch] not in mydict.keys():
                mydict[magazine[ch]] = 1
            else:
                mydict[magazine[ch]] += 1
        for x in range(len(ransomNote)):
            if ransomNote[x] not in mydict.keys() or mydict[ransomNote[x]] == 0:
                return False
            else:
                mydict[ransomNote[x]] -= 1
        return True
        
        # Time: O(m) -- m being the length of magazine, as magazine must be longer if the problem can be solved
        # Space: O(1) -- there can only be 26 chars in the dict


'''
Revisited this problem, came up with a similar optimal solution, though it does pass through ransomNote
twice. Still...

RT: O(n + m)
Space: O(n) 

Since the problem specifies lower case letters, you could use an array of size 26 instead of a HashMap, 
making space O(26) = O(1), but I wanted to practice dictionaries, so I did. Plus, it has more extentible use
cases -- what if the problem changes to having characters without ASCII values? What if the inputs are very small?
There are tradeoffs on each side, as with any problem.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Base Case
        if len(magazine) < len(ransomNote):
            return False
            
        ransom_dict = {}
        for ch in ransomNote:
            if ch not in ransom_dict:
                ransom_dict[ch] = 1
            else:
                ransom_dict[ch] += 1

        for ch in magazine:
            if ch not in ransom_dict:
                pass
            else:
                ransom_dict[ch] -= 1

        for key in ransom_dict:
            if ransom_dict[key] > 0:
                return False

        return True
        


'''
        