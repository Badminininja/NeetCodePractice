"""
LeetCode 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after raining.

Approach: two pointers, left and right, with a running leftMax/rightMax
tracking the tallest bar each side has seen so far. Always settle
(compute trapped water for) whichever side currently has the smaller
running max, then move that pointer inward.

Why that's safe: the water above any position is capped by min(true left
wall, true right wall). Once leftMax <= rightMax, the true right wall
(whatever bar further inward eventually turns out to be tallest) can only
be >= the current rightMax, which is already >= leftMax - so the shorter
of the two true walls at the left position is guaranteed to be leftMax,
and can be settled without ever knowing the true right wall exactly.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        wata = 0

        while left != right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax <= rightMax:
                wata += leftMax - height[left]
                left += 1
            elif leftMax > rightMax:
                wata += rightMax - height[right]
                right -= 1

        return wata


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([5, 4, 1, 2], 1),
        ([1], 0),
        ([1, 2], 0),
        ([3, 3, 3], 0),
    ]
    for height, expected in tests:
        result = sol.trap(height[:])
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: trap({height}) = {result} (expected {expected})")
