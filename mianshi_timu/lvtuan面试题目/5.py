numbers = [1, 3, 5, 7, 8, 25, 4, 20]


def median(lists=None):
    if not lists:
        lists = numbers
    sum_list = sum(numbers)
    balance = 0
    for num in numbers:
        if balance < (sum_list - num) / 2:
            balance += num
        else:
            break
    if balance == (sum_list - num) / 2:
        return num


if __name__ == '__main__':
    res = median() or "No Fond"
    print(res)
