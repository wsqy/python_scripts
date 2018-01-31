import os,os.path
import shutil
import getFileMd5

def isone(file1,file2):
    if os.path.getsize(file1)>150000000:
        if getFileMd5.bigFile(file1) == getFileMd5.bigFile(file2):
            return True
        else:
            return False
    else:
        if getFileMd5.smallFile(file1) == getFileMd5.smallFile(file2):
            return True
        else:
            return False

#全备份
def backupAll(dir_file,dir_backup):
    filedir = os.path.basename(dir_file)
    dir_backups = dir_backup+os.sep+filedir
    shutil.copytree(dir_file,dir_backups)
    
def backupIncremental(dir_file,dir_backup):
    #进入待备份文件夹
    os.chdir(dir_file)
    #列出所有文件
    files = os.listdir(dir_file) 
    #遍历文件
    for file in files: 
        #如果是文件夹
        if os.path.isdir(file):
            #如果文件夹在需要备份到的目录中已经存在
            if file in os.listdir(dir_backup):  
                #递归备份
                backupIncremental(dir_file+os.sep+file,dir_backup+os.sep+file)
            #如果不存在，对这个文件夹执行全备份
            else:
                backupAll(dir_file+os.sep+file,dir_backup+os.sep+file) 
                
        elif os.path.isfile(file): 
            #如果文件在需要备份到的目录中已经存在
            if file in os.listdir(dir_backup): 
                #如果是同一个文件则跳过
                if isone(dir_file+os.sep+file,dir_backup+os.sep+file):
                    pass
                #如果不是同一个文件，复制并且更名
                else:
                    shutil.copy(dir_file+os.sep+file,dir_backup+os.sep+file+'01')
                    
            #文件不存在
            else:
                shutil.copy(dir_file+os.sep+file,dir_backup+os.sep+file) 
                
                

if __name__=="__main__":
    dir = r'D:\Dev-Cpp'
    backup = r'D:\Dev-Cpp\ddddd'
    
    backupIncremental(dir,backup)   