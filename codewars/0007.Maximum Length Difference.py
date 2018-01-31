"""
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

#Example:

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(s1, s2) --> 13
Bash note:
input : 2 strings with substrings separated by ,

output: number as a string
"""


def mxdiflg(a1, a2):
    if not all((a1, a2)):
        return -1
    else:
        aa1, bb1 = min([len(x) for x in a1]), max([len(x) for x in a1])
        aa2, bb2 = min([len(x) for x in a2]), max([len(x) for x in a2])
        return max(bb1-aa2, bb2-aa1)
s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))
