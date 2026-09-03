"""
LC 271 - Encode and Decode Strings

Design an algorithm to encode a list of strings into a single string, and
decode that single string back into the original list of strings.

This is a format-design problem, not an algorithm-pattern problem. The only
hard requirement: decode(encode(strs)) == strs, always - including when
individual strings contain any character (including whatever delimiter
you might be tempted to use, like a comma).

Approach:
    Length-prefix each string: "{length}#{string}". Decoding never searches
    for a stop character inside the payload - it reads the length first, so
    it knows exactly how many characters to consume next, regardless of
    what those characters are.
"""


def encode(strs: list[str]) -> str:
    result = ""
    for s in strs:
        result += str(len(s)) + "#" + s
    return result


def decode(s: str) -> list[str]:
    result = []
    i = 0
    while i < len(s):
        # find the '#' to know where the length prefix ends
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])

        # the actual string starts right after '#', for exactly `length` chars
        result.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length

    return result


if __name__ == "__main__":
    cases = [
        ["hello", "world"],
        ["hello", "wor,ld"],   # embedded comma should not break decoding
        [""],
        ["", ""],
        ["a", "", "abc"],
        [],
    ]

    for strs in cases:
        encoded = encode(strs)
        decoded = decode(encoded)
        assert decoded == strs, f"Failed round-trip for {strs!r}: got {decoded!r}"

    print("All tests passed.")
