"""
Part 1
https://adventofcode.com/2024/day/3

Given corrupted input, find instances within it of `mul(x,y)`, multiplying x & y and summing all matches.
Note, the numbers in `mul()` can be a maximum of 3 digits.
For example, "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))" has 4 matches:

- mul(2,4) = 2 * 4 = 8
- mul(5,5) = 5 * 5 = 25
- mul(11,8) = 11 * 8 = 88
- mul(8,5) = 8 * 5 = 40

The sum of all these is 161.

Part 2
https://adventofcode.com/2024/day/3#part2

As above, but the corrupted input contains the strings `do()` and `don't()` within it.
Where these are encountered, they enable/disable future `mul()` instructions.
It's enabled to begin with.

For example, "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
disables `mul(5,5)` and `mul(11,8)` due to the `don't()` instruction after `mul(2,4)`.
It enables with `do()` before the last `mul(8,5)` instruction.

The sum therefore is 48.
"""
import re
import sys


def multiply_with_corruption(in_str: str, disable: bool = False) -> int:
    result = 0
    regex = re.compile(r"(do\(\))|(don't\(\))|mul\((\d{1,3},\d{1,3})\)")

    enabled: bool = True
    match: str
    for match in regex.findall(in_str):
        do, dont, mul = match
        if disable and do:
            enabled = True
        elif disable and dont:
            enabled = False
        elif mul and enabled:
            x, y = mul.split(",")
            result += int(x) * int(y)

    return result


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else None
    infile = sys.argv[2] if len(sys.argv) > 2 else None

    part = "2"

    if not part or part not in ("1", "2",):
        print("Usage: day3.py <part> [<infile>]")
        print("Usage: Where <part> equal to 1 or 2 (mul or ??)")
        exit()

    if not infile:
        if part == "1":
            in_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        elif part == "2":
            in_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    else:
        with open(infile, "r") as fh:
            in_str = fh.read()

    res = multiply_with_corruption(in_str, disable=part == "2")
    print(f"Result: {res}")
