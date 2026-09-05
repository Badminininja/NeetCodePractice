"""
LC 739 - Daily Temperatures

Given a list of daily temperatures, return an array where answer[i] is the
number of days you'd have to wait after day i for a warmer temperature. If
no future day is ever warmer, answer[i] is 0.

Approach (monotonic stack):
    Brute force scans forward from every index until it finds a warmer day
    - O(n^2), since a long decreasing run gets rescanned from every index
    inside it.

    Key insight: walk left to right keeping a stack of indices whose
    warmer day hasn't been found yet. At any point, every index still on
    the stack must have a temperature >= today's temperature - otherwise
    today would already have resolved it. So the stack's temperatures are
    always non-increasing from bottom (oldest waiting) to top (newest
    waiting, lowest temp). That's exactly why a stack works: when today
    finally beats something, it's guaranteed to beat the top of the stack
    first (lowest bar to clear) - pop it, record the gap, then keep
    checking the new top in case today beats that one too. Stop popping
    the moment today doesn't beat the current top, then push today's own
    index (it hasn't found its warmer day yet either).

    Every index is pushed exactly once and popped at most once across the
    whole run, so total work is O(n) despite the nested while loop.

Time:  O(n) - each index pushed once, popped at most once.
Space: O(n) worst case (strictly decreasing temperatures - nothing ever
       pops until the end, so every index sits on the stack at once).
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)

        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    assert sol.dailyTemperatures([90, 60, 30]) == [0, 0, 0]  # strictly decreasing
    assert sol.dailyTemperatures([55]) == [0]
    assert sol.dailyTemperatures([50, 50, 50]) == [0, 0, 0]  # equal temps never count

    print("All tests passed.")
