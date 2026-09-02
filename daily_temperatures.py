class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                old = stack.pop()
                result[old] = i - old

            stack.append(i)

        return result

