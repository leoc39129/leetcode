class BrowserHistory(object):    
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.step = 0        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.step += 1
        while(self.step < len(self.history)):
            self.history.pop()
        self.history.append(url)

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.step = max(0, self.step - steps)
        return self.history[self.step]


        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.step = min(len(self.history) - 1, self.step + steps)
        return self.history[self.step]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)