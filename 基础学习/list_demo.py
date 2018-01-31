def print_list(list):
    for i in list:
        print(i)
def list_demo_dir():
    print_list(dir(list))
#     ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
#     '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
#     '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', 
#     '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
#      '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', 
#      '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
#     'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    
#列表可以是任意的类型，数字，字符串，变量和另外一个列表
def list_demo_creat():
    a="python"
    lists  = ['py',1,[1,2,a]]
    print(lists)

#在数组中添加一个元素,默认会添加到列表的最后一面
def list_demo_append(): 
    lists  = ['py',1,[1,2]]
    lists.append("sb!")
    print(lists)
    
#自定义添加到第几个,下标从0开始
def list_demo_insert(): 
    lists  = ['py',1,[1,2]]
    lists.insert(1,"sb!")
    print(lists)

#插入一个列表,case1是将每个元素都添加进去，case2是插入一个列表
def list_demo_extend():
    lists  = ['py',1,[1,2]]
    #case 1：
    lists.extend([2,3])#<===>lists+[2,3]
    #case 2:
    lists.extend([[2,3]])
    print(lists)

#删除列表中的一个元素
def list_demo_remove():
    lists  = ['py',1,[1,2]]
    lists.remove('py') #删除列表中出现的第一个“py”，如果不存在则抛出ValueError
    print(lists)
    
#以下标的形式删除元素
def list_demo_pop():
    #L.pop([index]) Raises IndexError if list is empty or index is out of range
    lists  = ['py',1,[1,2]]
    s = lists.pop()#默认会删除列表的最后一个元素,它的返回值是删除的内容
    #s = lists.pop(0)#删除特定位置的元素,它的返回值是删除的内容
    #del lists[0]  这是一个BIF 不仅仅对列表有效
    print(s)

#清空列表，但不从内存中删除;del lists 会将lists从内存中删除
def list_demo_clear():
    lists  = ['py',1,[1,2]]
    lists.clear()
    print(lists)

#返回在列表中出现的次数
def list_demo_count():
    lists  = ['py',1,[1,2]]
    s = lists.count(2)#如果不存在则返回0
    print(s)
    
#返回在列表中首次出现的位置
def list_demo_index():
    #L.index(value, [start, [stop]]) 可选参数包括起始与结束位置
    lists  = ['py',1,[1,2],5,9]
    s = lists.index(2) #如果不存在则抛出ValueError:
    print(s)

#原地反转列表
def list_demo_reverse():
    lists  = ['py',1,[1,2],5,9]
    lists.reverse()
    print(lists) 

#元素排序
def list_demo_sort():
    #L.sort(key=None, reverse=False)
    lists  = [11,23,1,5,9]
    lists.sort()#注意不同类型的元素并不能排序,会抛出TypeError
    print(lists)#key参数指定排序函数，默认为ascill
    #reverse参数指定排序顺序  默认正序，设置为True则反序

#列表的分片
def list_demo_slice():
    lists  = [11,23,1,5,9]
    s = lists[1:3]#注意 [1,3)前闭后开区间
    print(s)

#列表的一些操作
def list_demo_operate():  
    #列表比较大小
    l1=[123,234]
    l2=[234,123]
    l3=[123,234]
    print((l1<l2)and(l1==l3))
    
    #列表的相加
    l4=l1+l2
    print(l4)
    #列表的相乘
    l5=l1*3
    print(l5)
    
    #成员操作符
    print(123 in l1)
#列表的内置复制操作
def list_demo_copy():
    lists  = ['py',1,[1,2]]
    s = lists.copy()
    print(lists,id(lists))
    print(s,id(s))
    del lists
    print(s,id(s))

#对列表复制的实验
def list_demo_fuzhi():
    l1 = [123,234]
    l2 = l1[:]#<==>L.copy
    l3=l1 #本质上只是添加了一个指向,一个变另一个也变了
    print(l1,id(l1))
    print(l2,id(l2))
    print(l3,id(l3))
    l1.append('12345')
    print(l1,id(l1))
    print(l2,id(l2))
    print(l3,id(l3)) 

#列表推导式    
def list_demo_tuidao():
    #一层列表的推导式<==>一位数组
    lists = [x**2 for x in range(10)]
    print(lists)
#     当然上式如果不用列表推导式表述，那就写法如下：
#     lists = []
#     for i in range(10):
#         lists.append(i**2)
#     print(lists)

    #多层列表推导式即多维数组的形成即写多个for...in...
    lists = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    print(lists)
    #当然上式如果不用列表推导式表述，那就写法如下：
    lists = []
    for i in [1,2,3]:
        for j in [3,1,4]:
            if (i!=j):
                lists.append((i,j))
    print(lists)
    
    
if __name__ == "__main__":
    list_demo_tuidao()