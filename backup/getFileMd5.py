import io,sys,string,hashlib

def smallFile(name):
    m =hashlib.md5()
    a_file = open(name,'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()

def bigFile(name):
    m = hashlib.md5()
    file = io.FileIO(name,'r')
    bytes = file.read(8024)
    while(bytes != b''):
        m.update(bytes)
        bytes = file.read(8024)
    file.close()
    return m.hexdigest()
    
 

if __name__ == '__main__':
    filename = r'C:\C盘文件\14暑假备份\新建文本文档.txt'
    fileMd5 = bigFile(filename)
    print(fileMd5)
    print('..........')
    