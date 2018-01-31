def tuple_demo_dir():
    print(dir(tuple))
#     ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
#       '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
#       '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', 
#       '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
#      '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


#元祖的创建
def tuple_demo_creat():
    #元祖的创建
    Tuples = (1,2,3)
    print(type(Tuples))
    
    #空元祖的创建
    Tuples = ()
    print(type(Tuples))
    
    #一个元素的元祖的创建
    Tuples = (1)
    print(type(Tuples))
    Tuples = (1,)
    print(type(Tuples))
    
    Tuples = 1,2,3,4,5
    print(type(Tuples))
    print(Tuples)
    #以上的实验可以看出元祖的关键字是逗号而不是一对小括号
    
    #把其他类型转化为元祖类型
    Tuples = tuple([1,2,3,4])
    print(type(Tuples))
    print(Tuples)
    
    #元祖的赋值
    Tuples = (1,2,3)
    x,y,z = Tuples
    print(x,y,z)
    
    x,y = y,x
    print(x,y,z)

#元祖的赋值
def tuple_demo_init():
    Tuples = (1,2,3)
    x,y,z = Tuples
    print(x,y,z)
    
    x,y = y,x
    print(x,y,z)



if __name__ =='__main__':
    tuple_demo_init()
    