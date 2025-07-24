"""
Part 1
https://adventofcode.com/2024/day/1

Two lists of unique integers are given, such as:
1   4
4   2
2   10
8   9
7   8
4   18

Find the distance between the lists as ordered pairs.
For example, find the distance between the smallest number in each list,
then the second smallest, and so on.
The output should be the sum of those distances, to get the total distance between the two lists.

Part 2
https://adventofcode.com/2024/day/1#part2

Simalar to part 1, but here we address similarity.
1   4
4   2
2   8
8   9
4   8
5   1

The similarity score is based of the times the number in the left appears in the right.
The number of the left is multiplied by the number of times that number appears on the right.
For example, for the above:
1 appears once so 1 * 1 = 1
4 appears once so 4 * 1 = 4
2 appears once so 2 * 1 = 2
8 appears twice so 8 * 2 = 16
4 appears again but once so 4 * 1 = 4
5 appears never so 5 * 0 = 0
So here the similarity score would be 1 + 4 + 2 + 16 + 4 + 0 = 27
"""
import sys


def calculate_distance(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    total_distance = 0
    for num1, num2 in zip(sorted_list1, sorted_list2):
        total_distance += abs(num2 - num1)

    return total_distance

def calculate_similarity(list1, list2):
    seen = {}
    for i in list1:
        if i not in seen:
            seen[i] = 0

        seen[i] += 1

    total_similarity = 0
    for i, j in enumerate(list2):
        if j not in seen:
            continue
        total_similarity += (j * seen[j])

    return total_similarity


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else None
    infile = sys.argv[2] if len(sys.argv) > 2 else None

    if not part or part not in ("1", "2",):
        print("Usage: day1.py <part> [<infile>]")
        print("Usage: Where <part> equal to 1 or 2 (distance or similarity)")
        exit()

    if not infile:
        list1 = [3, 4, 2, 1, 3, 3]
        list2 = [4, 3, 5, 3, 9, 3]

    else:
        list1 = []
        list2 = []
        with open(infile, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    num1, num2 = line.split("   ")  # this file comes with three spaces separator
                    list1.append(int(num1))
                    list2.append(int(num2))

    if part == "1":
        result = calculate_distance(list1, list2)
        print(f"The total distance between the two lists is: {result:,}")
    elif part == "2":
        result = calculate_similarity(list1, list2)
        print(f"The total similarity between the two lists is: {result:,}")
    