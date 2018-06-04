from multiprocessing import Process
from multiprocessing import Pool,Manager      #Manager有管理Queue
from multiprocessing import Queue
import random
import os
import time

######################### 子进程拷贝，主进程读取 #####################

def copyFile(filename, source_fold, destin_fold,queue):
    # print(filename)
    f_read = open(source_fold + '\\' + filename, 'rb')
    file_content = f_read.read()
    f_write = open(destin_fold + '\\' + filename, 'wb')
    f_write.write(file_content)

    f_read.close()
    f_write.close()

    queue.put(filename)        #将文件放到queue里

def main():
    os.chdir('D:\\python')
    source_fold = input('输入源文件夹的名字')  # 复制的文件夹
    destin_fold = source_fold + '复件'  # 复制的文件夹

    if os.path.exists(destin_fold):
       # os.chdir(destin_fold)
        for name in os.listdir(destin_fold):
            os.remove(name)
            print('删除%s结束'%name)

    #if not os.path.exists(destin_fold):      #查看文件夹中是否存在这个文件/文件夹
    else:
        file_name = os.listdir(source_fold)  # 获取source所有文件名
        os.mkdir(destin_fold)

        count = len(file_name)

        print(file_name)
        
        print('*' * 50)
        pool = Pool(5)
        queue = Manager().Queue()

        for name in file_name:
            pool.apply_async(copyFile, args=(name, source_fold, destin_fold,queue))

        num = 0

        while num < count:
            print(queue.get())
            num += 1
            copyRate = num/count
            print('copy的进度是:%0.2f%%'%(copyRate*100),end='')



        pool.close()
        pool.join()

    #print(os.listdir(destin_fold))


if __name__ == '__main__':
    main()