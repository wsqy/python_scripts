"""
3. 计算任一长度的字符串中不同的字符以及它的个数，例如”abcdaadbib”，输出: a,3 b,3 c,1 d,2 i,1
"""
import collections
strs = "abcdaadbib"
s = collections.Counter(strs)
print(s)
