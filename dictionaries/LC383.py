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


        