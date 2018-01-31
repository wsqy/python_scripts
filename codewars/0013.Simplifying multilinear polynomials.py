"""
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function:

simplify(poly)
that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"


All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.

Good Work :)
"""
import re
from functools import reduce

prog = re.compile(r'-?\d*[a-z]+')
prog_letter = re.compile(r'[a-z]+')
prog_dig = re.compile(r'-?\d*')


def simplify(poly):
    result = prog.findall(poly)
    result_dict = {}
    for x in result:
        letter = ''.join(sorted(prog_letter.search(x).group()))
        dig = ''.join(sorted(prog_dig.search(x).group()))
        if dig == '':
            dig = 1
        elif dig == '-':
            dig = -1
        dig = int(dig)
        if letter in result_dict:
            result_dict[letter] += dig
        else:
            result_dict[letter] = dig
    # print(result_dict)
    result_str = ""
    for key in sorted(sorted(result_dict.keys()), key=len):
        if result_dict[key] == 0:
            pass
        elif result_dict[key] == 1:
            result_str += ('+' + key)
        elif result_dict[key] == -1:
            result_str += '-' + key
        elif result_dict[key] > 0:
            result_str += ('+' + str(result_dict[key]) + key)
        elif result_dict[key] < 0:
            result_str += (str(result_dict[key]) + key)
    return result_str.lstrip('+')



print(simplify("-a+5ab+3a-c-2a"))
