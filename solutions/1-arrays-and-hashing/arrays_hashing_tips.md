# Arrays & Hashing — Big Tips Per Problem

Companion notes to go with the solved code in `solutions/`. Each section is the
core insight worth remembering next time a similar shape shows up — not a full
walkthrough, just the thing that made the problem click.

---

## Contains Duplicate (LC 217)

- The question is pure **existence**, not frequency — so reach for a `set`,
  not a counting `dict`.
- Naive approach is nested loops (compare every pair) → O(n²). A `set` gives
  O(1) average lookup, so a single pass tracking "have I seen this" gets you
  to O(n) time / O(n) space.
- One-liner exists (`len(nums) != len(set(nums))`) but say the explicit loop
  version first in an interview — it shows the reasoning, the one-liner is a
  nice follow-up mention, not the primary answer.

## Valid Anagram (LC 242)

- Easy to mix up with a **palindrome** check (`s == reversed(s)`) — anagram
  means same letters/quantities between *two different* strings, not a
  string matching its own reverse.
- Core pattern: build a frequency `dict` from `s` (`count[char] = count.get(char, 0) + 1`),
  then walk `t` "spending down" each count. Any missing key or count already
  at 0 means an immediate `False`.
- Quick early exit: if `len(s) != len(t)`, they can't be anagrams — check
  this before doing any real work.
- `sorted(s) == sorted(t)` is a valid one-liner but O(n log n); the
  counting-dict version is O(n) and is the one that generalizes to harder
  problems (Group Anagrams, Top K Frequent Elements).

## Two Sum (LC 1)

- Big reframe: don't ask "what do these two numbers sum to" — ask, for each
  number, **"what's the complement I still need?"** (`target - num`).
- Dict maps **value → index** (not just existence) because the problem wants
  positions back, not the numbers themselves.
- Single pass: for each `num`, check if its complement is already a key in
  the dict *before* adding `num` itself — this naturally prevents using the
  same element twice.
- `enumerate(nums)` gives `(index, value)` pairs in one pass instead of
  managing a manual counter — the standard way to get both index and value
  together in Python.

## Group Anagrams (LC 49)

- The unlock: sorting the letters of any word gives a canonical **signature**
  that's identical across all anagrams of that word (`"eat"`, `"tea"`,
  `"ate"` → all sort to `"aet"`).
- Because the signature is shared, you don't need to compare words against
  each other (which would force nested loops) — a single pass with a
  `dict` mapping `signature -> list of words` groups everything in O(n · k log k)
  (k = word length for the sort), no pairwise comparisons.
- Values in the dict are **lists**, not sets — duplicate input words and
  original order both need to be preserved in the output.
- `collections.defaultdict(list)` removes the manual "if key not in dict,
  create empty list" check — worth learning once the manual version feels
  solid.

## Top K Frequent Elements (LC 347)

- Step 1 is always the same counting-dict pattern. Step 2 is the new part:
  you need the **top K**, not just the single max, so a single "current max"
  variable doesn't work.
- Sorting the dict by frequency works but costs O(n log n) — fine as a first
  answer, but not optimal.
- The real trick: frequency is **bounded** (a number can appear at most
  `len(nums)` times), so you can use frequency itself as an array index —
  **bucket sort**. `buckets[freq]` = list of numbers with that exact count.
- Walk the buckets from highest index down to 1, collecting numbers until
  you hit `k`. Needs `len(nums) + 1` buckets (indices `0..len(nums)`,
  inclusive) or the max-frequency case throws an `IndexError`.
- Nested loops here (outer over bucket index, inner over each bucket's
  contents) still total O(n) — every original number lands in exactly one
  bucket and is visited exactly once across the whole walk. Nested loops
  don't automatically mean multiplied complexity; check whether the inner
  loop's *total* work across all outer iterations is bounded.
- `collections.Counter(nums).most_common(k)` is the Pythonic built-in for
  this — good to mention exists, but be ready to derive the bucket-sort
  version yourself.

## Encode and Decode Strings (LC 271)

- This one isn't an algorithm-pattern problem, it's a **format-design**
  problem — that's why it can feel like "nothing is happening." The only
  hard requirement given is `decode(encode(strs)) == strs`, always.
- Naive idea (join with a delimiter like `,`) breaks the moment a string in
  the list already contains that delimiter character — the decoder can't
  tell a real comma from a separator comma.
- Fix: **length-prefix** each string (`"{len}#{string}"`) so decoding never
  searches for a stop character inside the payload — it already knows
  exactly how many characters to consume next.
- General lesson for vague-sounding problems: state the naive idea out loud,
  then actively hunt for the input that breaks it (empty strings, strings
  containing your chosen delimiter, etc.) before trusting it.

## Product of Array Except Self (LC 238)

- Brute force (multiply everything except position `i`, for every `i`) is
  O(n²) no matter how it's reorganized — even "precompute a list of
  remaining numbers per index" still hides an inner loop at multiply time.
- Real insight: `answer[i] = (product of everything left of i) × (product of
  everything right of i)`. Both the left-products and right-products can be
  built with a **single accumulating pass each** — never rescanning.
- No division needed (important since the array can contain zeros).
- Space optimization once the two-array version is solid: build the left
  pass directly into the result array, then do a second pass carrying just
  one running variable for the right-side product, instead of a full second
  array.
- This problem doesn't use a dict at all — it's a different recurring
  pattern (**prefix/suffix accumulation**), worth recognizing as separate
  from the "seen-before" dict/set family.

## Valid Sudoku (LC 36)

- Three *independent* "no duplicates allowed" zones — rows, columns, and
  3×3 squares — need three separate tracking structures. A single global
  "have I seen this digit anywhere" set would incorrectly flag valid boards.
- Each zone only needs existence-tracking (a `set`), not counts.
- `(row // 3, col // 3)` maps any cell to which of the nine 3×3 squares it
  belongs to — a tuple is a fine dict key here since it's immutable/hashable.
  (Equivalent single-int version: `(row // 3) * 3 + (col // 3)`.)
- Still just one pass over all 81 cells, checking/updating three
  dicts-of-sets (`rows[r]`, `cols[c]`, `squares[(r//3, c//3)]`) at once.

## Longest Consecutive Sequence (LC 128)

- Naive version — for every number, walk forward while `num+1` is in the
  set — looks O(n) per lookup but is actually **O(n²) overall**, because
  long runs get redundantly re-walked starting from every number inside
  them.
- Fix: only start a forward walk from a number that's the **true start** of
  its sequence, detected by checking `num - 1 not in num_set`. Every other
  number in that run gets skipped in O(1) before any walk begins.
- Direction rule worth internalizing: the check for "am I a valid starting
  point" looks in the **opposite direction** from the direction your walk
  is about to go. Walking forward (`num + length`) → check backward
  (`num - 1`). If the walk went backward instead, you'd check `num + 1`.
- Because only true sequence-starts ever trigger a walk, and every number
  belongs to exactly one sequence, the total work summed across every walk
  in the whole run is bounded by `n` — true O(n), not just "O(1) lookups
  inside a loop that happens to look expensive."

---

## Cross-problem patterns worth carrying forward

- **Existence only** → `set` (Contains Duplicate, sequence-start check in
  Longest Consecutive Sequence).
- **Existence + extra info** → `dict` mapping value → info (Two Sum: value →
  index; Group Anagrams: signature → word list; Valid Sudoku: zone → seen
  digits).
- **Counting** → `dict` or `Counter` (Valid Anagram, Top K Frequent Elements).
- **Bounded range of a derived quantity** (like frequency) → consider bucket
  sort/direct indexing instead of a general sort.
- **"Everything except me" for every position** → prefix/suffix accumulation
  passes, not per-position recomputation.
- **Nested loops aren't automatically O(n·m)** — check whether the inner
  loop's total work, summed across every outer iteration, is actually
  bounded by something smaller (bucket sort, sequence-start walking).
- **Vague/no-algorithm-given problems** (Encode/Decode Strings) are usually
  testing whether you can find the edge case that breaks the naive design,
  not whether you know a named algorithm.
