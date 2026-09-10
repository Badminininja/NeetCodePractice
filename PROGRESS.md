# Progress Log

Tracking problems worked through, organized by NeetCode's roadmap categories. Each entry notes the actual approach taken, bugs caught along the way, and where the code lives in this repo.

## Arrays & Hashing

_Worked through in a separate chat and imported here. Full per-problem write-ups live in `solutions/1-arrays-and-hashing/arrays_hashing_tips.md` — this is the condensed version._

- [x] **Contains Duplicate** (LC 217) — existence check, so reach for a `set` not a counting `dict`. Naive nested-loop comparison is O(n²); a single pass tracking "have I seen this" is O(n).
- [x] **Valid Anagram** (LC 242) — build a frequency `dict` from one string, then "spend down" counts while walking the other; any missing/zeroed key fails it. Not the same as a palindrome check.
- [x] **Two Sum** (LC 1) — reframe as "what complement do I still need," not "what do these sum to." Dict maps value → index; check for the complement before inserting the current value, which naturally prevents reusing an element.
- [x] **Group Anagrams** (LC 49) — sorting a word's letters gives a canonical signature shared by every anagram of it; a dict keyed by signature groups everything in one pass instead of pairwise comparisons.
- [x] **Top K Frequent Elements** (LC 347) — frequency is bounded by `len(nums)`, so use frequency itself as an array index (bucket sort) instead of sorting by count. The nested loop over buckets is still O(n) total since every element is visited exactly once.
- [x] **Encode and Decode Strings** (LC 271) — a format-design problem, not an algorithm one. Length-prefixing each string (`"{len}#{string}"`) avoids ambiguity when a string contains whatever delimiter you'd otherwise pick.
- [x] **Product of Array Except Self** (LC 238) — `answer[i]` = (product left of i) × (product right of i), each built with a single accumulating pass — no division needed, works fine with zeros in the array.
- [x] **Valid Sudoku** (LC 36) — rows, columns, and 3×3 boxes are three independent "no duplicates" zones, each needing its own tracking set; a single global seen-set would be wrong. `(r // 3, c // 3)` keys the box.
- [x] **Longest Consecutive Sequence** (LC 128) — walking forward from every number is O(n²) from redundant re-walks of the same run. Only start a walk from a true sequence start (`num - 1 not in set`) to make it O(n).

## Two Pointers

- [x] **Valid Palindrome** (LC 125) — 2026-09-09
  - Initial plan was a manual index loop (`i` vs `length - i`) rather than named pointers; walking through it by hand exposed the off-by-one immediately (`length - i` overruns valid indices at `i = 0`), which pushed the reframe to explicit `left`/`right` pointers converging toward each other — the mental model that generalizes to the rest of this category.
  - First full draft had a run of small syntax slips caught one at a time: `len(str)` (indexing the builtin type instead of the parameter `s`), `.isalum()` (typo for `.isalnum()`), a stray dot in `s.[right]`, and a missing `:` on the comparison line.
  - Real logic bug once it ran: forgot to advance `left`/`right` after a successful character match, so the loop spun forever on any matching pair instead of progressing.
  - Second logic bug: the `left > right` bounds check was ordered after the skip-non-alnum branches, so a string of nothing but punctuation (e.g. `",,"`) could walk `left` straight past `right` and off the end of the string before the bounds check ever ran. Fixed by checking bounds first, before touching either index.
  - Misread the prompt's "case-insensitive" as "case-sensitive" on first pass, so `s[left] != s[right]` was left as a strict comparison. Caught by tracing the problem's own canonical example, `"A man, a plan, a canal: Panama"`: under a strict comparison the very first pair (`'A'` vs `'a'`) would fail it, contradicting the expected `True`, which forced a re-read of the prompt.
  - Added `.lower()` only at the comparison line rather than lowercasing the whole string up front — by that point in the loop both characters have already passed the `isalnum()` filter, so nothing gets lowered that didn't need to be.
  - Verified against the official example, the official negative example (`"race a car"`), and edge cases: empty string, all-punctuation string, single character, and a mismatched-case digit/letter pair (`"0P"`).
  - Code + self-tests: `solutions/3-two-pointers/01-valid-palindrome.py`

- [x] **Two Integer Sum II** (LC 167) — 2026-09-10
  - Two pointers again, but the sorted-array structure replaces the hashmap from the original Two Sum: moving `left` up only increases the sum and moving `right` down only decreases it, so comparing the current sum to target tells you unambiguously which pointer to move.
  - Two bugs on the first pass: `while true` (lowercase — Python's boolean is `True`), and once that was fixed, the "sum too big" branch moved `index1` instead of `index2` — so the right pointer never actually moved, and the search wasn't converging from both ends at all.
  - Reasoned through two edge cases before coding them in, and both held up: no explicit "no solution" fallback needed, since the problem guarantees exactly one valid pair; and no explicit `index1 == index2` check needed either, since a correctly-converging two-pointer walk is guaranteed to land on the (distinct-index) answer before the pointers could ever meet.
  - Also caught that the answer needed to be returned 1-indexed, not as the raw 0-indexed positions the loop naturally produces.
  - Verified against the official examples plus a duplicate-values case, and fuzz-tested the pointer convergence itself (20,000 random trials against a brute-force reference) once the pointer-movement bug was fixed.
  - Code + self-tests: `solutions/3-two-pointers/02-two-integer-sum-ii.py`

## Sliding Window
_(none yet)_

## Stack

- [x] **Valid Parentheses** (LC 20) — 2026-09-03
  - Initial instinct was a counter per bracket type (up on open, down on close, fail on negative or non-zero at the end). Worked out that this fails on interleaved-but-invalid strings like `([)]`, because counting throws away ordering information — it only tracks totals, not which bracket is currently "open."
  - Rebuilt with a stack: push each opening bracket; on a closing bracket, check the top of the stack against a dict of matching pairs (`{')': '(', ']': '[', '}': '{'}`) — pop on a match, return `False` on a mismatch or an empty stack. String is valid only if the stack is empty once the loop ends.
  - Caught a real bug mid-build: an early version's mismatch branch had no `else: return False`, so a genuinely invalid closer (the `]` in `"(])"`) was silently skipped instead of failing the whole string — it came back `True` when it should've been `False`.
  - Also benchmarked the dict-lookup version against a chained triple-OR condition with `timeit` — dict version came out ~1.4-2x faster in practice, mainly because the OR-chain version was doing two independent, unconditional `if` checks (not `if`/`elif`) per character rather than one dict membership test.
  - Code + self-tests: `solutions/2-stack/01-valid-parentheses.py`

- [x] **Min Stack** (LC 155) — 2026-09-03
  - Two parallel stacks: `minStack` holds real values, `ActualMin` holds two entries per push so it stays index-synced with `minStack` and always ends with the correct running min on top.
  - First bug: forgot `self.` entirely in the initial draft — local variables assigned in `__init__` don't persist past that call, so every other method was reading names that didn't exist in their scope.
  - Second bug, after fixing `self.`: cached the running min in `self.smallest`, but `pop()` never updated it, so popping the current minimum off the stack left `self.smallest` stuck on a value no longer in the stack.
  - Replaced the cached variable with `self.getMin()` (reads `ActualMin[-1]` live) so there's nothing left to go stale — but this introduced a third, subtler bug: `self.getMin()` is a live read, so calling it after already appending `val` to `ActualMin` in the same branch returns the value just appended, not the true prior minimum. Fixed by capturing `self.getMin()` into a local variable before mutating the list, not after.
  - Verified against the official LeetCode example, a hand-built pop-then-push regression case, and 200 randomized trials fuzzed against a plain `min()` reference implementation.
  - Code + self-tests: `solutions/2-stack/02-min-stack.py`

- [x] **Evaluate Reverse Polish Notation** (LC 150) — 2026-09-04
  - Walk tokens left to right (no need to reverse the list first - a stack gives LIFO pop order regardless of scan direction). Push numbers; on an operator, pop the top two (`b` first since it's most recent, then `a`), apply the operator to `(a, b)`, push the result back.
  - Operator dispatch via a dict mapping each operator string to a function (`operator.add`/`sub`/`mul` plus a lambda for `/`) instead of an if/elif chain - same pattern as the `pairs` dict in Valid Parentheses.
  - Avoided a classic trap: detecting numbers with `str.isdigit()` breaks on negatives (`"-3".isdigit()` is `False`); checking membership in the fixed operator set sidesteps it entirely.
  - Division needs to truncate toward zero, not floor - Python's `//` floors toward negative infinity, which disagrees with truncation on negative results (`-7 // 2 == -4`, truncation wants `-3`). Used `int(a / b)` instead.
  - Caught one real bug via testing: a single-number input with no operators (e.g. `["18"]`) never passes through the `int(stack.pop())` conversion that happens inside the operator branch, so the raw string token was returned unconverted (`'18'` instead of `18`). Fixed by wrapping the final `return` in `int(...)` - sufficient since it's the function's only exit point.
  - Code + self-tests: `solutions/2-stack/03-evaluate-reverse-polish-notation.py`

- [x] **Daily Temperatures** (LC 739) — 2026-09-04
  - The hardest conceptual jump so far on the roadmap - took several rounds of tracing a concrete example to find the insight, rather than one clean bug fix.
  - Brute force scans forward from every index until it finds a warmer day (O(n^2)) - a long decreasing run gets rescanned from every index inside it.
  - Key insight found by tracing `[73,74,75,71,69,72,76,73]` by hand: increasing runs resolve immediately (each day's answer is just the next day), but decreasing runs pile multiple days up waiting for the *same* future day - e.g. both 71 and 69 end up resolved by the same later 72.
  - That means a running "waiting list" of unresolved indices is always non-increasing in temperature from oldest to newest, which is exactly why a stack (not a queue) is the right structure: a new warm day is guaranteed to beat the most-recently-added (lowest-temp) waiting entry first, so pop-and-check from the top, continuing to pop while the new temperature keeps beating the entries beneath it.
  - First code attempt had three separate issues, fixed one at a time: `for i, t in temperatures` (crashes - a plain list of ints isn't a list of pairs to unpack; needed `enumerate(temperatures)`), writing the resolved answer to `result[i]` (today, the index that just found a warmer day) instead of `result[index]` (the popped index that was actually waiting and just got its answer), and a missing `return result` at the end (silently returned `None`).
  - Verified against the official examples, edge cases (strictly decreasing, all-equal temperatures, single element), and 500 randomized trials cross-checked against a brute-force reference implementation.
  - Code + self-tests: `solutions/2-stack/04-daily-temperatures.py`

- [x] **Car Fleet** (LC 853) — 2026-09-07
  - Reframed each car's motion as a "solo travel time" to the target: `(target - position) / speed`. A car merges into the fleet ahead of it exactly when its solo time is <= the time of the car currently leading; otherwise it arrives later and starts a new fleet.
  - First hand-traced version happened to land on the right answer (3 fleets) for the example traced by hand, but that turned out to be a coincidence, not a correct algorithm - fuzz-testing against a reference implementation across 2000 random trials found 576 mismatches. A minimal counterexample (`target=14, position=[2,9,7], speed=[3,1,3]`) exposed a wrong traversal direction and a wrong tracked-time update rule; corrected both (walk from closest-to-target outward, only update the tracked time on a strictly greater value) and re-verified with zero mismatches across 5000 trials.
  - Translating the corrected idea into code introduced a second, more subtle bug: sorted `cars` descending by position (closest first) and consumed the resulting `times` list with `stack.pop()` - but `pop()` removes from the *end* of a list, so the descending sort put the farthest car last, meaning `pop()` grabbed it *first* and silently reversed the walk again. Fuzz-testing caught it immediately (1433/2000 mismatches). Fixed by sorting ascending instead (no `reverse=True`), so the closest car ends up last and gets popped first, matching the intended direction.
  - Verified against the official LeetCode examples, an empty-input edge case, and both fuzz-found counterexamples, plus the earlier 2000/5000-trial randomized runs.
  - Code + self-tests: `solutions/2-stack/05-car-fleet.py`

## Binary Search
_(none yet)_

## Linked List
_(none yet)_

## Trees
_(none yet)_

## Tries
_(none yet)_

## Heap / Priority Queue
_(none yet)_

## Backtracking
_(none yet)_

## Graphs
_(none yet)_

## Advanced Graphs
_(none yet)_

## 1-D Dynamic Programming
_(none yet)_

## 2-D Dynamic Programming
_(none yet)_

## Greedy
_(none yet)_

## Intervals
_(none yet)_

## Math & Geometry
_(none yet)_

## Bit Manipulation
_(none yet)_
