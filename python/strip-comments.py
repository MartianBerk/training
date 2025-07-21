"""
Solution to "Strip Comments" problem on Codewars (Kata 4).
https://www.codewars.com/kata/51c8e37cee245da6b40000bd
"""


def strip_comments(strng, markers):
    stripped = []
    for line in strng.split("\n"):
        for marker in markers:
            while marker in line:
                line = line[:line.index(marker)]

        line = line.rstrip()
        stripped.append(line)
        
    return "\n".join(stripped)