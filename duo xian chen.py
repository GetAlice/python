import time
import threading     #子线程模块


#主线程回等待所有子线程结束后才结束


'''
#####################################
def daySorry():
	print('sorry')
	time.sleep(1)

for i in range(5):
	daySorry()

if __name__ == '__main__':   #多线程
	for i in range(5):
		t = threading.Thread(target=daySorry)
		t.start()

####################################

####################################  #主线程回等待所有子线程结束后才结束
def sing():
	for i in range(3):
		print('唱歌.......%d'%i)
		#time.sleep(1)

def dance():
	for i in range(3):
		print('跳舞.........%d'%i)
		#time.sleep(1)

if __name__ == '__main__':
	print('--------开始-------%s'%time.ctime())
	t1 = threading.Thread(target=sing)
	t2 = threading.Thread(target=dance)

	t1.start()
	t2.start()
	while True:
		length = len(threading.enumerate())
		print('当前运行的线程数为:%d'%length)
		if length<=1:
			break
		time.sleep(0.5)

	#time.sleep(5)
	print('------------结束------------%s'%time.ctime())
####################################
'''
############################每个线程都有名字，如果没取名系统会自动取

'''
class MyThread(threading.Thread):
	def run(self):
		for i in range(3):
			time.sleep(2)
			msg = 'Im ' + self.name + ' @ ' +str(i)  #没给线程名字默认Thread开头
			print(msg)

def test():
	for i in range(5):
		t = MyThread()
		t.start()

if __name__ == '__main__':
	test()

#############################################
'''
##################线程更改全局变量######################
'''
g_num = 100
def work_1():
	global g_num
	for i in range(3):
		g_num +=1

def work_2():
	global g_num
	print('------work_2 , g_num is %d'%g_num)

print('创建线程前,g_num 是 %d'%g_num)

t1 = threading.Thread(target=work_1)
t1.start()

t2 = threading.Thread(target=work_2)
t2.start()
'''
####################################################

##################线程更改列表实参######################
'''
g_num = [11,22,33,44]
def work_1():
	global g_num
	g_num.append(55)
	print('work_1',g_num)

def work_2():
	global g_num
	print('------work_2 , g_num is ',g_num)

print('创建线程前,g_num 是 ',g_num)

t1 = threading.Thread(target=work_1)
t1.start()

t2 = threading.Thread(target=work_2)
t2.start()
'''
#######################################################
#
#######################################################
'''
g_num = 0
g_flag = 1
def work_1():
	global g_num
	global g_flag
	if g_flag==1:
		for i in range(1000000):
			g_num +=1
	g_flag += 1
	print('work_1,g_num = %d'%g_num)

def work_2():
	global g_num
	global g_flag
	while True:
		if g_flag != 1:
	#time.sleep(3)
			for i in range(1000000):
				g_num +=1
			break

	print('work_2,g_num = %d'%g_num)

t1 = threading.Thread(target=work_1)
t1.start()

t2 = threading.Thread(target=work_2)
t2.start()
'''
###################################################

############   同步  ############################
'''
#from threading import Thread,Lock


class Task1(Thread):
	def run(self):
		while True:
			if lock1.acquire():          #if 后的方法会直接运行  （先运行lock1.acquire上锁，如果返回True，上锁成功，就继续运行）
				print('------task1-----')
				time.sleep(0.5)
				lock2.release()			#释放lock2的锁定
				
class Task2(Thread):
	def run(self):
		while True:
			if lock2.acquire():
				print('------task2-----')
				time.sleep(0.5)
				lock3.release()			#释放锁定
class Task3(Thread):
	def run(self):
		while True:
			if lock3.acquire():
				print('------task3-----')
				time.sleep(0.5)
				lock1.release()         #释放锁定

lock1 = Lock()
lock2 = Lock()    
lock2.acquire()  #锁定lock2

lock3 = Lock()
lock3.acquire()  #锁定lock3

t1 = Task1()
t2 = Task2()
t3 = Task3()

t1.start()
t2.start()
t3.start()
'''
###############################################

####################   互斥锁   ########################
'''
g_num = 0
def work_1():
	global g_num
	for i in range(1000000):
		#lock_flag = mutex.acquire()      #阻塞，如果这个所在上锁前已经被锁上，要等待解锁后才能执行修改
		if mutex.acquire():
			g_num += 1
			mutex.release()
	print('work_1--------g_num = %d'%g_num)

def work_2():
	global g_num
	for i in range(1000000):
		#lock_flag = mutex.acquire()
		if mutex.acquire():
			g_num += 1
			mutex.release()
	print('work_2--------g_num = %d'%g_num)

mutex = threading.Lock()          #创建一个互斥锁，默认是未上锁状况

t1 = threading.Thread(target=work_1)   #work1不等于1000000的原因是两个都在运行，但是都运行够了1000000次所以work能2000000
t1.start()

t2 = threading.Thread(target=work_2)
t2.start()
'''
################################################
#
###################### 死锁例子 ####################
'''
class MyThread1(threading.Thread):
	def run(self):
		if mutexA.acquire():
			print(self.name+'do1-------up')
			time.sleep(1)
			if mutexB.acquire():
				print(self.name+'do1--------down')
				mutexB.acquire()
			mutexA.acquire()

class MyThread2(threading.Thread):
	def run(self):
		if mutexB.acquire():
			print(self.name+'do2-------up')
			time.sleep(1)
			if mutexA.acquire():
				print(self.name+'do2--------down')
				mutexA.acquire()
			mutexB.acquire()

if __name__ == '__main__':
	mutexA = threading.Lock()
	mutexB = threading.Lock()

	t1 = MyThread1()
	t2 = MyThread2()

	t1.start()
	t2.start()
'''
####################################################

##############  解决死锁  ##########################
'''
class MyThread1(threading.Thread):
	def run(self):
		if mutexA.acquire():
			print(self.name+'do1-------up')
			time.sleep(1)
			if mutexB.acquire(blocking=True,timeout=2):
				print(self.name+'B上锁--------down')
				mutexB.release()
				print(self.name+'B在1中解锁--------down')
			mutexA.release()
			print('A在1中解锁')

class MyThread2(threading.Thread):
	def run(self):
		if mutexB.acquire():
			print(self.name+'do2-------up')
			time.sleep(1)
			if mutexA.acquire(blocking=True,timeout=2):
				print(self.name+'A上锁--------down')
				mutexA.release()
				print(self.name+'A在2解锁成功------')
			mutexB.release()
			print('B在2解锁')

if __name__ == '__main__':
	mutexA = threading.Lock()
	mutexB = threading.Lock()

	t1 = MyThread1()
	t2 = MyThread2()

	t1.start()
	t2.start()
'''
######消费者和生产者模式  
'''
from queue import Queue

class Producer(threading.Thread):
	def run(self):
		global queue
		count = 0
		while True:
			if queue.qsize()<1000:
				for i in range(100):
					count += 1
					msg = '生产产品'+str(count)    #队列小于1000个就加500
					queue.put(msg)
					print(msg)
				time.sleep(0.5)

class Comsumer(threading.Thread):
	def run(self):
		global queue
		while True:
			if queue.qsize()>100:           #队列大于100就消费3个
				for i in range(3):
					msg = self.name + '消费了' + queue.get()
					print(msg)
				time.sleep(0.5)

if __name__ == '__main__':
	
	queue = Queue()
	for i in range(500):
		queue.put('初始产品'+str(i))


	for i in range(2):    #两个Producer线程
		p = Producer()
		p.start()

	for i in range(5):	  #五个Comsumer线程
		c = Comsumer()
		c.start()
'''
##############################################
#
########## threadlocal #######################

local_school = threading.local()  #创建全局ThreadLocal对象
def process_student():
	std = local_school.student #获取当前线程关联的student
	print('hello,%s(in %s)'%(std,threading.current_thread().name))

def process_thread(name):
	local_school.student = name  #绑定ThreadLocal的student
	process_student()

t1 = threading.Thread(target=process_thread,args=('laozhao',),name='Thread_a')
t2 = threading.Thread(target=process_thread,args=('laowang',),name='Thread_b')

t1.start()
t2.start()

t1.join()
t2.join()
