"""
Part 1
https://adventofcode.com/2024/day/2

Given a list of reports, where each report is a list of levels (ints), determine how many are safe.
To be considered safe, each report must satisfy:

- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.

[
    [7, 6, 4, 2, 1]  # safe
    [1, 2, 7, 8, 9]  # unsafe
    [9, 7, 6, 2, 1]  # unsafe
    [1, 3, 2, 4, 5]  # unsafe
    [8, 6, 4, 4, 1]  # unsafe (equal levels don't satisfy)
    [1, 3, 6, 7, 9]  # safe
]

Part 2
https://adventofcode.com/2024/day/2#part2

As above, but each report is allowed to have one unsafe level that can be removed, making it safe.

[
    [7, 6, 4, 2, 1]  # safe
    [1, 2, 7, 8, 9]  # unsafe
    [9, 7, 6, 2, 1]  # unsafe
    [1, 3, 2, 4, 5]  # safe, by removing the second level (3)
    [8, 6, 4, 4, 1]  # safe, by removing the third level (4)
    [1, 3, 6, 7, 9]  # safe
]
"""

import sys

from typing import List


def distance(x, y):
    return abs(x - y)
    

def inline(x, y, d):
    return x < y if d == 0 else x > y


def compare_levels(x, y, d = None):
    result = True
    l_distance = distance(x, y)

    if l_distance == 0:
        result = False
    elif l_distance > 3:
        result = False
    
    if not result or d is None:
        return result
    
    return inline(x, y, d)


def calculate_safe(report: List[int], dampner: bool = False, debug: bool = False):
    direction = None
    result = None

    i = 0
    while i < len(report) - 1:
        i += 1

        if i == 1:
            direction = 0 if report[i] < report[i-1] else 1
            result = compare_levels(report[i], report[i-1])
        else:
            result = compare_levels(report[i], report[i-1], direction)
            
        if result is False:
            break

    i = 0
    while dampner and result is False:
        # Here we need to check recursively each report with a level missing until one is SAFE
        new_report = [report[j] for j in range(len(report)) if j != i]
        dampner = i < len(report) - 1
        result = calculate_safe(new_report, debug=debug)
        if result:
            if debug:
                print(f"Report {str(report)} made safe by removing {report[i]}")
            break

        i += 1
            
    return result


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else None
    infile = sys.argv[2] if len(sys.argv) > 2 else None
    debug = sys.argv[3] if len(sys.argv) > 3 else None

    part = "2"

    if not part or part not in ("1", "2",):
        print("Usage: day2.py <part> [<infile>]")
        print("Usage: Where <part> equal to 1 or 2 (safety or ??)")
        exit()

    if not infile:
        reports = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]

    else:
        reports = []
        with open(infile, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                   reports.append([int(i) for i in line.split(" ")])

    if part == "1":
        safe = 0
        for report in reports:
            result = calculate_safe(report, debug=debug)
            if debug:
                print(f"Report {str(report)} is {'SAFE' if result else 'UNSAFE'}")
            if result:
                safe += 1
        print(f"{safe} reports are safe")
    elif part == "2":
        safe = 0
        for report in reports:
            result = calculate_safe(report, dampner=True, debug=debug)
            if debug:
                print(f"Report {str(report)} is {'SAFE' if result else 'UNSAFE'}")
            if result:
                safe += 1
        print(f"{safe} reports are safe")
    