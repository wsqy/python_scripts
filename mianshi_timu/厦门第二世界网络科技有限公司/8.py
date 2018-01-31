"""
8. 有30个人，其中有男人，女人和小孩，在一家饭馆吃饭，一共花费50元，
其中每个男人3元，每个女人2元，每个小孩1元，问男人，女人，小孩各有几个？
"""
for man in range(30 // 3):
    for woman in range((50 - man * 3) // 2):
        if 3 * man + 2 * woman + (30 - man - woman) == 50:
            print("man:%s\twoman:%s\tchild:%s" % (man, woman, (30 - man - woman)))
