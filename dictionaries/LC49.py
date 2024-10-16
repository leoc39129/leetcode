class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Base Case:
        if len(strs) == 1:
            return [[strs[0]]]

        indices = [0 for _ in range(len(strs))]
        counters = [Counter(i) for i in strs]

        ret = []
        #print(indices)
        for i in range(len(strs)):
            if indices[i] != 0:
                continue
            else:
                cur = [strs[i]]
                indices[i] += 1
                for j in range(i+1, len(strs)):
                    if len(strs[j]) != len(strs[i]):
                        continue
                    elif indices[j] == 0 and counters[i] == counters[j]:
                        indices[j] += 1
                        cur.append(strs[j])
                
                ret.append(cur)

        return ret


'''
Technically passes all test cases, but O(n^2) RT for an input size 10^4
shouldn't pass. 

There is an O(n*mlog(m)) solution shown below, that leverages
sorting each word in the original array so that you only have to 
loop over the original array once

(where I'm assuming mlog(m) is the time to sort a word, where m <= 100)

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
'''