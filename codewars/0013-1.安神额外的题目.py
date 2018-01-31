"""
your_order("is2 Thi1s T4est 3a")
out "Thi1s is2 3a T4est"
"""
import re
from functools import reduce

prog_dig = re.compile(r'\d+')


def your_order(poly):
    return ' '.join(sorted(poly.split(), key=lambda x:int(re.search(r'\d+', x).group())))
# def your_order(poly):
#     result = poly.split()
#     result_dict = {}
#     for x in result:
#         dig = prog_dig.search(x).group()
#         if dig == '':
#             dig = 1
#         dig = int(dig)
#         result_dict[x] = dig
#     return " ".join([x[0] for x in sorted(result_dict.items(), key=lambda d: d[1])])




print(your_order("is2 Thi1s T4est 3a"))
