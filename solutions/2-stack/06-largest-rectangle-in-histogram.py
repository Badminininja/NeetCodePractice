"""
LC 84 - Largest Rectangle in Histogram

Given an array of bar heights forming a histogram (each bar has width 1,
sitting side by side), find the area of the largest rectangle that can be
formed entirely within the histogram's outline.

Approach (monotonic increasing stack):
    For any single bar, ask: "what's the biggest rectangle where THIS bar's
    height is the limiting (minimum) height?" The answer is bounded by the
    nearest bar to its left that's strictly shorter, and the nearest bar to
    its right that's strictly shorter - anything taller in between can't
    cap the height, only something shorter can. Every possible rectangle's
    limiting height belongs to exactly one bar (or a tie of equal-height
    bars), so taking the max of this per-bar answer over every bar covers
    every possible rectangle.

    A single left-to-right pass with a stack of indices gets both
    boundaries at once, instead of two separate passes. The stack
    invariant: heights at the stacked indices are always increasing from
    bottom to top. Walking forward, if the current bar is shorter than
    whatever's on top of the stack, that top bar can never extend any
    further right - pop it and finalize its rectangle:
        - right boundary = the current index i (first shorter bar to the
          right)
        - left boundary = whatever index is now exposed on top of the
          stack after the pop (or -1 if the stack goes empty, meaning the
          run extends all the way to the start)
        - width = i - left_boundary - 1
        - area = heights[popped_index] * width
    Popping is a `while`, not an `if` - one shorter bar can retire several
    taller bars in a row. After the `while` loop drains however many bars
    it needs to (zero or more), the current index always gets pushed -
    it hasn't found its own right boundary yet.

    Sentinel trick for the leftover stack: at the end of the array, any
    bar still sitting on the stack never found a shorter bar to its right
    within the array - meaning it's free to extend all the way to the end.
    Rather than writing a second cleanup loop with different boundary
    logic, append one extra height-0 bar to the end before the main loop
    runs. Being shorter than literally everything, it forces the existing
    `while` loop to drain the entire stack during the final iteration,
    reusing the exact same pop/width/area logic instead of duplicating it.

    Debugging story:
    - First attempt looped with `for i in enumerate(heights)`, forgetting
      that `enumerate()` yields (index, value) pairs - so `i` itself was a
      tuple, and pushing it onto the stack meant `stack[-1]` was a tuple
      too. `heights[i]` and `heights[stack[-1]]` both broke with
      "list indices must be integers, not tuple".
    - After unpacking with `for i, j in enumerate(heights)`, a second bug
      surfaced: `area = width * height` referenced a `height` variable
      that was never assigned - needed `heights[currentHeight]`, the
      actual height of the popped bar (`currentHeight` held an index, not
      a height value, despite the name).
    - A structural bug followed: the code had `if not stack: push` and
      the popping `if` as two separate top-level `if`s rather than
      `if`/`elif`, so right after pushing into an empty stack, the very
      next `if` immediately compared the just-pushed bar's height against
      itself (always true) and popped it right back off - the stack could
      never actually accumulate more than one element at a time.
    - Restructuring to `if <empty or shorter>: push; continue` fixed that,
      but exposed the next bug: the popping branch used a single `if`
      instead of a `while`, so only one pop could happen per index even
      when multiple taller bars needed to retire in the same step (the
      same "possibly pop several times per index" shape as Daily
      Temperatures) - and worse, after that one pop, the current index was
      never pushed onto the stack at all (push only happened in the
      separate `if`/`continue` branch), so it silently vanished from
      future width calculations.
    - Final fix: drop the separate `if <empty or shorter>: push` branch
      entirely. Just `while stack and heights[stack[-1]] >= heights[i]:
      pop and compute`, followed by an *unconditional* `stack.append(i)`
      after the loop - exactly the Daily Temperatures shape. The push
      isn't a separate case from popping; it's just "always happens once
      the while loop is done popping, however many times that was."
    - Verified against the official example, a single-element case, a
      strictly increasing sequence, and 2000 randomized trials
      cross-checked against a brute-force O(n^2) reference, all passing.

Time:  O(n) - each index is pushed once and popped at most once.
Space: O(n) worst case (strictly increasing heights - nothing pops until
       the sentinel forces it, so every index sits on the stack at once).
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # sentinel: forces the stack fully empty by the end
        largest = 0
        stack = []
        for i, _ in enumerate(heights):
            while stack and heights[stack[-1]] >= heights[i]:
                currentHeight = stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                area = width * heights[currentHeight]
                if area > largest:
                    largest = area
            stack.append(i)

        return largest


if __name__ == "__main__":
    sol = Solution()
    # Official LC examples
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    # Edge / regression cases
    assert Solution().largestRectangleArea([5]) == 5
    assert Solution().largestRectangleArea([1, 2, 3, 4, 5]) == 9  # strictly increasing
    assert Solution().largestRectangleArea([5, 4, 3, 2, 1]) == 9  # strictly decreasing
    assert Solution().largestRectangleArea([3, 3, 3, 3]) == 12  # all equal
    assert Solution().largestRectangleArea([0, 0]) == 0

    print("All tests passed.")
