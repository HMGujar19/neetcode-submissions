class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                stack_t, stack_ind = stack.pop()
                output[stack_ind] = i - stack_ind
            stack.append([val,i])
        return output