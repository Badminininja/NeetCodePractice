"""
LC 150 - Evaluate Reverse Polish Notation

Evaluate an arithmetic expression given in Reverse Polish Notation (RPN):
operators come after their operands (e.g. "2 1 +" instead of "2 + 1"), so
the expression can be evaluated left to right with no parentheses or
operator-precedence rules needed.

Approach:
    Walk the tokens left to right (no need to reverse anything - a stack
    naturally gives LIFO pop order regardless of scan direction). Push
    numbers. On an operator, pop the top two values (b popped first since
    it was pushed most recently, then a), apply the operator to (a, b) in
    that order, push the result back. One value left on the stack at the
    end is the answer.

    Operator dispatch uses a dict mapping each operator string to a
    function (operator.add/sub/mul, plus a lambda for division) instead of
    an if/elif chain per operator.

Bugs caught along the way:
    - Detecting "is this a number" with str.isdigit() breaks on negative
      numbers ("-3".isdigit() is False) - checking membership in the fixed
      operator set instead avoids this entirely.
    - Division must truncate toward zero, not floor - Python's // floors
      toward negative infinity, which disagrees with truncation for
      negative results (-7 // 2 == -4, but truncation wants -3). Fixed
      with int(a / b) instead of a // b.
    - A single-number input with no operators (e.g. ["18"]) never gets
      popped through the int(stack.pop()) conversion inside the operator
      branch, so the raw string token was returned unconverted. Fixed by
      wrapping the final return in int(...) - the function's only exit
      point, so that's sufficient here (converting at push time instead
      would be the more generally robust habit, just not required for
      this problem).

Time:  O(n) - one pass over tokens.
Space: O(n) worst case (all operands, no operators until the end).
"""

import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(ops[i](a, b))
            else:
                stack.append(i)
        return int(stack.pop())


if __name__ == "__main__":
    sol = Solution()
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert sol.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ) == 22
    assert sol.evalRPN(["-7", "2", "/"]) == -3  # truncation toward zero, not floor
    assert sol.evalRPN(["18"]) == 18  # single-token input, no operators
    assert sol.evalRPN(["-18"]) == -18

    print("All tests passed.")
