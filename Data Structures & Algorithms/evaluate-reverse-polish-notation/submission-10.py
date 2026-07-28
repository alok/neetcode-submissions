from operator import add, mul, sub
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # UNOPS=
        # always be defining maps
        OPS = {"+": add, "-": sub, "*": mul, "/": lambda a, b: math.trunc(a / b)}
        for t in tokens:
            if t not in OPS:  # num
                # print(t)

                i = int(t)
                stack.append(i)
            else:
                # pop 2
                # print(stack)
                r, l = stack.pop(), stack.pop()
                fn = OPS[t]
                res = fn(l, r)
                # print(res)
                stack.append(res)
        # assert len(stack) == 1, stack
        return stack.pop()
