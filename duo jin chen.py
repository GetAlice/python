from multiprocessing import Process
from multiprocessing import Pool,Manager      #Manager有管理Queue
from multiprocessing import Queue
import random
import os
import time
'''
import os
import time
###################################     主/子进程的结束不影响  子/主进程的运行
ret = os.fork()    #新建子进程，只能在unix,linux,mac上使用,运行的时候返回值是0
print('os.fork()返回值是 %d'%ret)
print('当前进程ID是：%s'%os.getpgid())                #返回当前进程ID
if ret < 0:
	print('fork 调用失败')
	time.sleep(1)
elif ret == 0:
	print('我是子进程%d,父进程是 %d  ----1---'%(os.getpid(),os.getppid()))          #返回当前进程的父进程ID
	time.sleep(1)
else:
	print('我是父进程  %s,我的子进程是:%i ---2----'%(os.getpgid(),ret))
	time.sleep(1)
###################################
'''
########## multiprocessing跨平台#############  主进程会等所有子进程结束后才结束

'''
def run_proc(name):       #子进程要运行的代码
	print('子进程运行中，name=%s,pid=%s'%(name,os.getpid()))
	print('run_proc执行结束')
	time.sleep(10)

if __name__ == '__main__': 
	print('父进程%d'%os.getpid())
				#target表示这个进程实例所调用对象
	p = Process(target=run_proc,args=('test',))   #创建一个process类实例对象，一个实例就是一个进程
	print('子进程要执行')
	p.start()    #执行子进程代码
	#p.join()     #等待子进程结束后再继续执行，一般用于进程同步，也可以填等待几秒
	print('子进程执行结束')

	for i in range(5):
		print(i,end=' ')
'''
#################  当前进程实例别名，默认为Process-N，N为从1开始递增的整数
'''
def run_proc(name,age,**kwargs):
	for i in range(10):
		print('子进程进行中，name =%s,age=%d,pid=%d'%(name,age,os.getpid()))
		print(kwargs)
		time.sleep(1)

if __name__ == '__main__':
	print('父进程%d'%os.getpid())
	p = Process(target=run_proc,args=('test',18),kwargs={'m':20})
	print('子进程要执行')
	p.start()
	time.sleep(1)
	#p.terminate()     #终止子进程

	p.join()
	print('子进程结束')
'''
###########################################  如果不指定name参数，默认的进程对象名称为Process-N，N为一个递增的整数
'''
def work_1(inteval):
	print('work_1,父进程(%s),当前进程(%s)'%(os.getppid(),os.getpid()))
	t_start = time.time()
	time.sleep(inteval)
	t_end = time.time()
	print('work_1 执行时间为%0.2f秒'%(t_end-t_start))

def work_2(inteval):
	print('work_2,父进程(%s),当前进程(%s)'%(os.getppid(),os.getpid()))
	t_start = time.time()
	time.sleep(inteval)
	t_end = time.time()
	print('work_2 执行时间为%0.2f秒'%(t_end-t_start))

if __name__ == '__main__':

	print('当前（父）进程id:%s'%os.getpid())
	p1 = Process(target=work_1,args=(2,))
	p2 = Process(target=work_2,name='dd',args=(1,))

	p1.start()
	p1.join()
	p2.start()
	p2.join()

	print('p2.is_alive=%s'%p2.is_alive())

	#输出P1和p2进程的别名和pid
	print('p1.name is %s'%p1.name)
	print('p1.pid = %s'%p1.pid)

	print('p1.name is %s'%p2.name)
	print('p1.pid = %s'%p2.pid)

	p1.join()
	print('p1.is_alive=%s'%p1.is_alive())
'''
####################################
'''
class Sub_Process(Process):       #这是继承Process类的子类
	def __init__(self,inteval):
		Process.__init__(self)
		self.inteval = inteval

	def run(self):				#重写Process子类的run方法
		print('子进程%s开始执行,父进程id是%s'%(os.getpid(),os.getppid()))
		time_start = time.time()
		time.sleep(self.inteval)
		time_stop = time.time()
		print('子进程%s结束，耗时%0.2f秒'%(os.getpid(),time_stop-time_start))

if __name__ == '__main__':
	time_start = time.time()
	p1 = Sub_Process(2) 	#如果没有给定target属性就会自动执行p1.run()
	p1.start()				#如果没有给定target属性就会自动执行p1.run(),run要自己在def编辑规则
	p1.join()
	time_stop =time.time()
	print('父进程%s结束，耗时%0.2f秒'%(os.getpid(),time_stop-time_start))
'''
############################################

##################    进程池   #####################
'''
def worker(msg):
	t_start = time.time()
	print('%s开始执行,进程号为%d'%(msg,os.getpid()))
	time.sleep(random.random()*2)
	t_stop = time.time()
	print(msg,'执行完毕，耗时%0.2f'%(t_stop-t_start))

if __name__ == '__main__':
	po = Pool(3)            #定义一个进程池，最大进程数为3，立刻创建3个函数，用不用先不理,先执行进程池里的3个进程，多出来的等待进程池运行完有空位才运行
	for i in range(0,5):	#添加5个任务
		#po.apply_async(worker,(i,))     #异步方法,非阻塞方式执行work，（i，）为传递给worker的参数列表，以元组方式传递
		po.apply(worker,(i,))            #阻塞方法worker，一个子进程执行完后，再添加下一个子进程

	print('---------start-------------')
	po.close()   #关闭进程池
	po.join()    #等待po中所有子进程执行完毕后才执行后面，必须在close之后
	print('----------end--------------')
###################################################

##########   进程间的通信 Queue  ##################

q = Queue(3)
q.put('消息1')
q.put('消息2')
print(q.full())
q.put('消息3')
print(q.full())
q.put('消息4')

q.get()  #取出一个值
print(q)
###################################################

def write(q):
	for value in ['A','B','C','D']:
		print('put %s to queue...'%value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	while True:
		if not q.empty():
			value = q.get()
			print('get %s from queue...'%value)
			time.sleep(random.random())
		else:
			break

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))

	pw.start()   #用Queue写入信息
	pw.join()

	pr.start()   #用Queue读取信息
	pr.join()

	print('所有数据读写完毕')
############################################

##############   Queue-2   #################

def write(q):
	for value in ['A','B','C','D']:
		print('put %s to queue...'%value)
		q.put(value)   #q = Manager().Queue()   所以q.put = Queue.put
		time.sleep(random.random())

def read(q):
	print('read启动(%s),父进程为%s'%(os.getpid(),os.getppid()))
	for temp in range(q.qsize()):
		print('read从Queue获得消息:%s'%q.get())

if __name__ == '__main__':
	print('父进程%s启动'%os.getpid)
	q = Manager().Queue()                    #使用Manager中的Queue初始化
	pool = Pool()

	pool.apply(write,(q,))
	pool.apply(read,(q,))

	pool.close()
	pool.join()

	print('所有数据读写完毕')
##################################

'''
#######################  多进程拷贝文件 ##############
'''
def copyFile(filename,source_fold,destin_fold):
	#print(filename)
	f_read = open(source_fold + '\\' + filename,'rb')
	file_content = f_read.read()
	f_write = open(destin_fold + '\\' + filename,'wb')
	f_write.write(file_content)

	f_read.close()
	f_write.close()

def main():
	os.chdir('D:\\python')
	source_fold = input('输入源文件夹的名字')     #复制的文件夹
	destin_fold = source_fold + '复件'            #复制的文件夹

	os.removedirs(destin_fold)
	os.mkdir(destin_fold)
	
	file_name = os.listdir(source_fold)       #获取source所有文件名
	print(file_name)
	print('*'*50)
	pool = Pool(5)

	for name in file_name:
		pool.apply_async(copyFile,args=(name,source_fold,destin_fold))

	pool.close()
	pool.join()

	print(os.listdir(destin_fold))


if __name__ == '__main__':
	main()
'''
#####################################################
#
##################### 异步 async ##########################

def test1():
	print('----进程池中的进程------pid=%d,ppid=%d'%(os.getpid(),os.getppid()))
	for i in range(3):
		print('-----%d----'%i)
		time.sleep(1)
	return 'good'

def test2(args):
	print('-----callback func---pid=%d'%os.getpid())
	print('-----callback func---args=%s'%args)

if __name__ == '__main__':
	pool = Pool(3)
	#pool.apply_async(func=test1,callback=test2)  #异步调用，test1运行完后返回的值回调给test2当调用参数
	

	while True:
		pool.apply_async(func=test1,callback=test2)
		time.sleep(1)
		print('-----主进程pid=%d-----'%os.getpid())