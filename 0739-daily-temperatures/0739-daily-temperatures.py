class Solution:
      def dailyTemperatures(self, temps):
        res = [0] * len(temps)
        stack = deque()
        for index, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                cur = stack.pop()
                res[cur] = index - cur
            stack.append(index)

        return res