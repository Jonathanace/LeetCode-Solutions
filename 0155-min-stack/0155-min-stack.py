class MinStack:
    def __init__(self):
        self.q = []

    def push(self, val):
        minimum = val
        if self.getMin() is not None:
            minimum = min(minimum, self.getMin())
        self.q.append((val, minimum));

    # @return nothing
    def pop(self):
        self.q.pop()


    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]


    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]