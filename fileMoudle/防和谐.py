import re
import os,os.path

extension=['.swf','.htm','.mht','.torrent','.txt']  #定义要删除的类型

#文件内容防和谐
def edit(fileName):
    with open(fileName,'ab') as f:
        f.write(b'000')

#递归进入文件夹
def search_file(dirctory):
    os.chdir(dirctory)
    print(os.getcwd())
    list=os.listdir(os.curdir)
    for file in list:  
        print(file)
        if os.path.isdir(file):   #如果是文件夹
            newFileName = '.'.join(file) #执行文件改名操作 
            os.rename(file,newFileName)
            search_file(newFileName)   #递归执行 
            os.chdir(os.pardir) #执行完返回上一级
        #如果是文件，文件名更改，内容修改
        else: 
            (f_name, f_extension) = os.path.splitext(file)   #分离文件名与文件类型 
            if f_extension in extension:   #如果是不需要的类型，则删除
                os.remove(file)
            else:
                f_name = '.'.join(f_name) #文件名防和谐
                newFileName = f_name+f_extension
                os.rename(file , newFileName) 
                edit(newFileName)  #内容修改
            
if __name__ == "__main__":
    dirctory = r'1'
    search_file(dirctory)   
    print("完成")

