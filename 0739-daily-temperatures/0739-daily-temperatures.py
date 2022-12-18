class Solution:
      def dailyTemperatures(self, temps):
        ans = [0] * len(temps)
        stack = deque()
        for index, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                cur = stack.pop()
                ans[cur] = index - cur
            stack.append(index)

        return ans