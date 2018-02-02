import collections

# 定义一个 namedtupld
User = collections.namedtuple('User', ['name', 'sex', 'age'])


# 创建一个 User 对象
user1 = User(name="user1", sex="male", age=2)


# 已可迭代对象的方式创建一个 User 对象
user2 = User('user2','male', 4)


# 修改 属性值
user1._replace(age=3)


# 转成 字典
user1._asdict()
