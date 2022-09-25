class MyCircularQueue:

    def __init__(self, k: int):
        self.max = k
        self.queue = []

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.max:
            self.queue.append(value)
            # print(self.queue)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            return True
        else:
            return False

    def Front(self) -> int:
        return self.queue[0] if self.queue else -1
        

    def Rear(self) -> int:
        return self.queue[-1] if self.queue else -1
        

    def isEmpty(self) -> bool:
        return False if self.queue else True
        

    def isFull(self) -> bool:
        return True if len(self.queue) == self.max else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()