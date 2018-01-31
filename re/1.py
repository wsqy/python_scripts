import re


def print_list(List):
    for i in List:
        print(i)


def re_demo_1():
    # 解析价格
    txt = 'if you purchase|more?than 100 sets,the price of product A is $9.90.'
    # /string/MathObject
    m = re.search(r'(\w*)', txt)
    print(m.group())


def re_demo_2():
    txt = "aaabbb\naabb"
    m = re.search(r"a{2}", txt)
    print(m.group())


def re_demo_sub():
    txt = txt = 'if you purchase|more?than 100 sets,the price of product A is $9.90.'
    s = re.sub(r'\d+\.?\d*', '<qy>', txt)
    print(s)

if __name__ == "__main__":
    re_demo_2()
