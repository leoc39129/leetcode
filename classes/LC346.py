import collections

class MovingAverage(object):


    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        queue = self.queue
        queue.append(val)
        #print(queue)
        return float(sum(queue))/len(queue)
    '''
    def __init__(self, size):
        """
        :type size: int
        """
        self.avg = [0] * size
        self.count = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.avg.pop()
        self.avg.insert(0, val)
        #print(self.avg)
        if self.count < len(self.avg):
            self.count += 1
            return sum(self.avg) / float(self.count)
        else:
            return sum(self.avg) / float(len(self.avg))
    '''
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)