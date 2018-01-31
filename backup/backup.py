import shutil
import os,os.path
import sys
import datetime
import getFileMd5
#  todaydate = datetime.datetime.now().strftime("%y%m%d")   

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



def backupPath():
    global dir_file 
    global dir_backup
    dir_file = input("请输入要求备份的目录(默认为管理员桌面)：").strip()
    if len(dir_file) == 0:
        dir_file = r'C:\Users\Administrator\Desktop'
    dir_backup = input("备份到那个目录(默认为D:\Backup)?").strip()
    if len(dir_backup) == 0:
        dir_backup = r'D:\Backup'
        
def backupType():
    backuptype = input("请输入备份类型1.全备份/2.增量备份/输入其他则退出：").strip()
    if backuptype == '1': 
        backupAll(dir_file,dir_backup) 
    elif backuptype == '2':
        backupIncremental(dir_file,dir_backup) 
    else:
        sys.exit()
 
#全备份
def backupAll(dir_file,dir_backup):
    filedir = os.path.basename(dir_file)
    dir_backups = dir_backup+os.sep+filedir
    shutil.copytree(dir_file,dir_backups)

#增量备份
def backupIncremental(dir_file,dir_backup):
# if os.path.isdir(dir_file):
#    osModulehutil.copytree(dir_file,dir_backup)
# else:
#     shutil.copy(dir_file,dir_backup)
    files = os.listdir(dir_file)




if __name__=="__main__":
    backupPath() 
    backupType() 
    