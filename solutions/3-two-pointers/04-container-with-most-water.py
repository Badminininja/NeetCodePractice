"""
LeetCode 11. Container With Most Water

Given an array height where height[i] is the height of a vertical line at
index i, find two lines that, together with the x-axis, form a container
that holds the most water. Area between lines i and j is
min(height[i], height[j]) * (j - i).

Approach: two pointers starting at opposite ends. Move whichever pointer
points at the shorter line, inward. The container's height is always
capped by the shorter wall, so moving the taller wall's pointer can only
shrink the width without any chance of raising that cap - only moving the
shorter wall's pointer has a chance of finding a taller line and
increasing the max area.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        maxSize = 0
        left = 0
        right = len(heights) - 1

        while True:
            if left >= right:
                return maxSize

            currentSize = min(heights[left], heights[right]) * (right - left)
            if currentSize > maxSize:
                maxSize = currentSize

            if heights[left] <= heights[right]:
                left += 1
                continue
            right -= 1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([1, 2, 1], 2),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 4, 3], 4),
        ([2, 3, 4, 5, 18, 17, 6], 17),
    ]
    for heights, expected in tests:
        result = sol.maxArea(heights)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: maxArea({heights}) = {result} (expected {expected})")
