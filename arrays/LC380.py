import random

class RandomizedSet(object):

    def __init__(self):
        self.randomset = []
        self.randomhash = {}
        self.len = 0
        # print(self.randomset)
        # print(self.randomhash)
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.randomhash.keys() or self.randomhash[val] == -1:
            self.randomset.append(val)
            self.randomhash[val] = self.len
            self.len += 1
            # print(self.randomset)
            return True
        else:
            return False
        
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randomhash.keys() and self.randomhash[val] != -1:
            for idx in range(self.randomhash[val]+1, self.len):
                self.randomhash[self.randomset[idx]] -= 1
            self.randomset.remove(val)
            self.randomhash[val] = -1
            self.len -= 1
            # print(self.randomset)
            return True
        else:
            return False
        
        

    def getRandom(self):
        """
        :rtype: int
        """
        # print(self.randomset)
        # print(self.randomhash)
        # print(self.len)
        random_index = random.randint(0, self.len-1)
        return self.randomset[random_index]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
Technically passes, but very slow. Technically I guess the remove function averages to O(1), but
I'm not so sure about that. Here's a creative discussion board solution:

Note that you can del self.idx_map[val] from the dictionary, rather than having to use the -1 as I
did in my solution. On the precipice of having this type of solution, not quite.

import random

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.idx_map = {}

    def search(self, val):
        return val in self.idx_map

    def insert(self, val):
        if self.search(val):
            return False

        self.lst.append(val)
        self.idx_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        idx = self.idx_map[val]
        self.lst[idx] = self.lst[-1]
        self.idx_map[self.lst[-1]] = idx
        self.lst.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)


'''