sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'ashamed']


def starts_(lists=None, chrs='sh'):
    res = []
    if not lists:
        lists = sent
    for i in lists:
        if i.startswith(chrs):
            res.append(i)
    return res


def len_than_4(lists=None, len_word=4):
    res = []
    if not lists:
        lists = sent
    for i in lists:
        if len(i) > 4:
            res.append(i)
    return res


if __name__ == '__main__':
    # print(starts_())
    print(len_than_4())
