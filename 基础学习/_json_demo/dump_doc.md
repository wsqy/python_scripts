### dump
```
obj, fp,
skipkeys=False,  是否跳过非基础类型的校验
ensure_ascii=True,
check_circular=True,
allow_nan=True,
cls=None,
indent=None,
separators=None,
default=None,
sort_keys=False, **kw
```
### skipkeys
是否跳过非基础类型(str,int,float,bool,None),否则将会抛出TypeError

### ensure_ascii
非ascill字符是否需要转义

### check_circular 未理解
是否进行循环引用检查, 如果产生了循环引用将会导致 OverflowerError

### allow_nan
使用js相等的数替代,或者是抛出ValueError

### cls
自定义编码/解码器

### indent
缩进级别, 默认None不进行缩进以减少体积;

### separators
压缩 目的是去掉 ~,:~后面的空格

### default
指定函数 解析自定义类型为可序列化的基本类型

### sort_keys
指定是否按字母顺序排序
