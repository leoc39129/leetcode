from collections import defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Base Case: s will never be empty, nor will words
        # If s is shorter than the length of a word in words, we'll never find a
        # concatenated substring

        ret = []

        if len(s) < len(words[0]):
            return ret

        # Make a dictionary of the original words in words
        words_dict = defaultdict(int)
        for st in words:
            words_dict[st] += 1

        # Look through each "chunk" of the sliding window in s (incrementing by one)
        
        chunk = len(words[0])*len(words)
        word = len(words[0])

        # Don't forget about falling off the edge - the chunk can only be
        # a concatened string up to a point

        for ch in range(len(s) - chunk + 1):

            cur_subst = s[ch:ch+chunk]

            # COME BACK TO IT: How to format so range goes 0, 4, 8, ... or 0, 3, 6, ..
    
            # For each possible mini word in the substring that could possibly
            # be in words...
            complete_substring = True

            subst_words = words_dict.copy()

            for idx in range(len(cur_subst) / word):

                # We can't just check if the mini word is in words or not,
                # we have to keep track of whether it's been used or not -- we
                # can't repeat a mini word from words

                # But, words can have duplicates

                mini_word = cur_subst[(idx*word) : (idx*word) + word]

                if subst_words.get(mini_word, 0) != 0:
                    subst_words[mini_word] -= 1
                else:
                    complete_substring = False

            if complete_substring and sum(subst_words.values()) == 0:
                ret.append(ch)

        return ret
        

'''
GPT SOLUTION:

Walk through the following examples to see how this code works and is more efficient than your solution above

s = "barfoothefoobarman", words = ["foo","bar"]

s = "barfoofoobar", words = ["foo", "bar"]

-------------------------------------------------

from collections import defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        ret = []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        words_dict = defaultdict(int)
        
        for word in words:
            words_dict[word] += 1
        
        # Iterate through each offset
        for i in range(word_len):
            left = i
            right = i
            cur_dict = defaultdict(int)
            count = 0
            
            while right + word_len <= len(s):
                mini_word = s[right:right + word_len]
                right += word_len
                
                if mini_word in words_dict:
                    cur_dict[mini_word] += 1
                    count += 1
                    
                    while cur_dict[mini_word] > words_dict[mini_word]:
                        left_word = s[left:left + word_len]
                        cur_dict[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == num_words:
                        ret.append(left)
                else:
                    cur_dict.clear()
                    count = 0
                    left = right
        
        return ret

'''