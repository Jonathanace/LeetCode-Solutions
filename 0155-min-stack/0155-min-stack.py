class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        minimum = val
        if self.getMin() is not None:
            minimum = min(minimum, self.getMin())
        self.stack.append((val, minimum));

    # @return nothing
    def pop(self):
        self.stack.pop()


    # @return an integer
    def top(self):
        return self.stack[-1][0] if self.stack else None


    # @return an integer
    def getMin(self):
        return self.stack[-1][1] if self.stack else None