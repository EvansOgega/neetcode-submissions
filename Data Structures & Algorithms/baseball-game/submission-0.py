class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for ops in operations:
            if ops == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                num3 = num1 + num2
                stack.append(num3)
            elif ops == "C":
                stack.pop()
            elif ops == "D":
                num = stack[-1]
                stack.append(num * 2)
            else:
                stack.append(int(ops))
        for num in stack:
            total += num
        return total