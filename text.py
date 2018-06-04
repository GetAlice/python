'''
for i in range(10):
     for k in range(10):
          if k!= i:
               print(k)
          else:
               print("i+k=",i+k)
     print ("i=",i)



i = 0

def add_num(x,y):
     num = x+y
     if num > 500:
          return "to big"
     return num

count = add_num(100,600)
print(count)



a = '''
#asddsa
#asa
#aaa
'''
print(a)
print("##############")
b = "asdas" \
    "dasda" \
    "asds"
print(b)




for i in range(100,10000):            #水仙花数
    if i < 1000:
        a = (i //100)**3
        b = ((i%100)//10)**3
        c = (i % 10)**3
        if(a+b+c == i):
          print(i)
    if i > 1000:
        a = (i //1000)**4
        b = ((i%1000)//100)**4
        c = ((i%100)//10)**4
        d = (i % 10)**4
        if(i == a+b+c+d):
          print(i)




num = 0
while True:
  num += 1
  if num > 200:
    break
  print (num,end=" ")



name = input("请输入名字")
name = name.strip()                                  #去除字符串空格  lstrip去除左边空格  rstrip去除右边空格
if name.isalpha() and name.lower() == 'jack':        # x.lower(强制转换小写) x.upper(强制大写)
  print(name.lower())
elif name.lower != 'jack':
  print ("you no jack")
else:
  print("名字不能为空，请重新输入")

aaa ="cuo"
age = input("输入年龄:")
age = age.strip()
if len(age)>2:
if age.isdigit():
  print("年龄：",age)
else:
  print("输入错误")



s = "good afternoon"
print(s.capitalize())          #字符串首字母大写

c = "cjr"
print(c.center(10,'-'))        #字符串在总长度 10 中居中，剩余用 '-' 填充
print(str.ljust(c,40,'#'))       #字符串 c 靠左，右边填充#到40位

name = 'cjrf;cjrf'
print(name.count('f'))         #统计 f 在字符串中出现几次
print(name.endswith('l'))      #字符串结尾是否为 l
print(name.isalnum())          #判断字符串是否全是字母或者数字
print(name.title())            #将字符串中每组单词的首字母变为大写
print('*'.join(name))          #用 * 把字符串每个字符串连接起来

l = name.split(';')            #在字符串中指定的分隔符分开字符串，最终返回到数组
print(l)

####################
a = [1,2,3]
b = a
print(a,b)
a.append(4)
print(a,b)

print('*'*50)

a = [1,2,3]
b = a[:]
print(a,b)
a.append(4)
print(a,b)
####################

print(name.replace('f','sbb')) #将字符串中的 f 替换为sbb
print(name.isidentifier())     #判断字符串是否为合法变量名
print(name.isupper())          #判断字符串是否全是大写
print(name.istitle())          #判断字符串是否每个单词首字母大写

dic1 = {'1':'aaa','2':'bbb'}
dic2 = dict(a='aaa',b='bbb')
dic1["3"] = 'ccc'              #添加名字为 3 的指定键，键值为ccc
print(dic1)
print(dic2)
print("3 = "+ dic1.get('3'))   #返回键 3 的值，和dic1['3']效果一样
print(dic1.items())            #以列表返回字典可遍历的键和值的元组对
print(dic1.keys())             #以列表返回字典所有的键
print(dic1.values())           #以列表返回字典所有的值
del dic1['3']                  #删除字典里的键 '3'
print(dic1)

print("\nkey value")
#for key,value in dic1.items():  #遍历字典
#  print(key,"  ",value)
#for key in dic1:
#  print(key,dic1[key])
for key in dic1.keys():
  print(key,dic1[key])

dic3 = dict(zip('abc',[1,2,3]))
print('dic3 = ',dic3)

dic4 = {i:2*i for i in range(3)}
print(3)

class aaaa:
  for i in range(3):
    print(i)

dic5 = dict.fromkeys(range(3),aaaa)   #只能创建一样的值
print(dic5)

dic6 = {1:'1',2:'2'}
dic7 = {3:'3',4:'4'}
dic8 = dic6.update(dic7)
print (dic6)

b = str1.encode('编码类型')              #默认将utf-8的字符串 转为bytes字节
b = bytes1.decode('编码类型')            #将bytes转成字符串，默认为utf-8解码
b = bytes('asdasd',encoding='编码类型')  #用bytes内置方法将字符串转为指定编码的bytes

###############################################
lis = [12,23,34]
def func(*args):                         #将值转换为元组
  for arg in args:
    print(arg)

func(lis)
func(*lis)                               #将列表，元组每个值取出来，字典只取key

###############################################

def fund(**kwargs):                      #只接收键值对，例如 k1='k1'，然后将值传入字典
  print(kwargs)
  for arg in kwargs:
    print(arg)

fund(k1='v1')
dic1 = {'k1':'v1','b1':'c1'}
fund(**dic1)

################################################

################################################
def sum_100(n):
  if n <= 0:
    return 0
  return n+sum_100(n-1)
ret = sum_100(100)
print(ret)
################################################

sum = lambda s:s*s                      #匿名函数表达式
def f(s):
    return s*s
print(sum(2))
print(f(2))

def make_r(n):
    return lambda s:s*n
f1 = make_r(2)
m = f1(2)
print(m)


g = lambda x:x+2
info =  [g(x) for x in range(10)]
print(info)


info = [lambda a:a**3,lambda b:b**2]
print(info[0](3))
print(info[1](2))
for f in info:
    print(f(5))

lis = [x*x for x in range(1,10)]
print(lis)

list1 = [a+b for a in '123' for b in 'abc']     ###推倒式
print(list1)
    #等于
list2 = []
for a in '123':
    for b in 'abc':
        list2.append(a+b)
print(list2)


dic = {x:x**2 for x in (2,4,6)}      #字典推倒式
print(dic)

a = {x for x in 'dasdasdfjoeiwajdsaf' if x not in 'abc'}   #集合推倒式
print(a)

result = [lambda x:x+i for i in range(10)]
print(result[0](10))
result = [lambda x,i=i:x+i for i in range(10)]
print(result[0](10))

from collections import Iterable   #载入collections的Iterable类型判断对象是否可迭代
print(isinstance([1,2,3],Iterable))#isinstance是Iterable的一个函数,整数不能迭代


lis = [1,2,3,4]
it = iter(lis)                   #创建迭代器对象
print(next(it))                  #迭代下一个到报错结束   next是迭代器

for x in it:                     #for循环遍历迭代对象
    print(x)


g = (x*x for x in range(5))    #生成器
for i in g:
    print(i)

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        print(b,end=' ')
        a,b = b,a+b
        n = n+1
fab(5)
######################################

def fab_1(max):
    n,a,b = 0,0,1
    lis = []
    while n<max:
        lis.append(b)
        a,b = b,a+b
        n +=1
        print(lis)
    return lis
for i in fab_1(5):
    print(i)

######################################
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b             #带有yield的函数会被python视为一个生成器，不生成值
        a,b = b,a+b         #当用到for或者next()后，yield才会返回B值
        n = n+1             #每次next()时，代码到yield停止，并记住单签位置
f = fab(5)                  #到下一次next时从yield下面的代码开始，for同理
print(f.__next__())
for n in fab(5):
    print(n,end=' ')

######################################

def outer(func):              #   func == f1
    def iner(*args,**kwargs):
        print('ok1')
        ret = func(*args,**kwargs)
        print('ok2')
        return ret
    return iner

@outer                       #只要加了装饰器，函数回车后直接运行
def f1():                    #被outer装饰的函数 被当成outer使用的参数,只调用函数内容
    print('f1')              #不调用返回值
f1()                         #所以实际上面的outer(func)==outer(f1)

def outer2(func):
    def iner(*args,**kwargs):
        print('ko')
        res = func(*args,**kwargs)
        print('ko')
    return(iner)


@outer
@outer2
def f2(name):
    print(name)
f2('渣渣飞')
#######################################


import os
os.chdir('D:\\python\\text')
print(os.getcwd())
f = open('file1','w')                #以写入的方式打开file1，如果没有file1这个文件
s = 'hello world'                    #会先创建一个
f.write(s)
#f.read()
f.close()

#try:
#    data = f.read()
#finally:
#    f.close()

    #等于

with open('file1','w') as f:
    f.write('Hello world!!')

###################################

import os
os.chdir('D:\\python\\text')
print(os.getcwd())

fold_name = input("请输入目录名")
file_name = os.listdir(fold_name)
print(file_name)
for name in file_name:
    os.rename(name,'text'+name)
print(os.listdir())
#####################################

#print(dir(__builtins__))

def f1():
    return 10/0
def f2():
    f1()
def f3():
    f2()

try:
    f3()
except: 
    print('error')

s1 = 'hello'
try:
    try:
        print(int(s1))
    except IndexError as e:
        print(e)
except ValueError as e:
    print(e)

#####等于
try:
    print(int(s1))
except IndexError as e:
    print(e)
except ValueError as a:
    print(a)
#####等于
try:
    print(int(s1))
except(IndexError,ValueError) as a:
    print(a)
#####
import sys

try:
    print(int(s1))
except(IndexError,OSError) as err:
    print(err)
except Exception as a:
    print(a)

############
try:
    r = 10/5
except:
    print('error')
    raise                           #主动抛出异常
else:
    print(r)                        #有else 和 finally 的时候，try没出错运行else和finally
finally:
    print('finally')                #无论出错与否，都会输出finally

#####################################


class Foo:
    def __init__(self,lis):          #在类里使用迭代器
        self.lis = lis
    def __iter__(self):
        return iter(self.lis)
obj = Foo([1,2,3,4,5,6])
for i in obj:
    print(i,end=' ')


class Foo1(object):
    def __init__(self):
        pass
    def __iter__(self):
        yield 1
        yield 2
        yield 3
    __slots__ = ('name','age','a')   #限定实例在新建对象的时候只能使用name,age,a

obj = Foo1()
obj.name = 'jack'
obj.age = 11
obj.a = 1
for i in obj:
    print(i)


class A:
    def show(self):
        print('A')

        

class B(A):
    def show(self):
        print('B')

        
obj = B()
obj.show()
obj.__class__ = A     #指向类赋值
obj.show()
obj.__class__ = B
obj.show()


class A:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def myprint(self):
        print('%s  %s'%(self.__a,self.__b))
    def __call__(self,num):
        print('call',num+self.__a)

    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
obj = A(5,10)
print(obj.get_a())
print(obj.get_b())
print(obj.myprint())
obj(80)


class A(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('init')
    def mydefault(self,*args):
        print('default')

    def __getattr__(self,name):   #拦截点号运算   如果实例没有找到实例方法，就会调用自己定义的方法
        return self.mydefault

a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()



a = 1
def s():
    a = 2
    print('s()a:',a)
    print('s()a的id:',id(a))
s()
print('a:',a)
print('a的id:',id(a))

def d():
    global a                     #global可以将函数内的私有函数改成全局函数，可覆盖函数外的全局函数
    a = 2
    print('d()a',a)
    print('d()a的id',id(a))
d()
print('a:',a)
print('a的id',id(a))


from collections import Iterable  #判断是否可迭代对象(Iterable)
print(isinstance('abc',Iterable)) #判断数据类型是否和后面写的对象类型一样，一样返回Ture




###################闭包########################
def test(num):
    print('-------text1--------')

    def test_in(num_in):
        print('-------------test 2-------------')
        return num + num_in
    print('-------test3--------')
    return test_in     #返回调用test_in

test(20)
res = test(20)     # res == test() == test_in
print(res(22))


def line_conf(a,b):
    def line(x):
        return a*x + b
    return line

lin1 = line_conf(2,3)
print(lin1(5))



class A(object):
    def __init__(self,a,b):
        print('A__init__')
        self.__a = a
        self.__b = b
    def print_info(self):
        print('%d %d'%self.__a,self.__b)
    def __call__(self,num):
        print('----call me ====',num)
    def __str__(self):
        return 'hello world'
    def __new__(cls,a,b):
        print('new',a,b)
        if a>10:
            return super(A,cls).__new__(cls)
        return B()

class B(object):
    def __init__(self):
        print('B__init__')
def run(self):
    print('run')

import types
a = A(11,30)
a.run = types.MethodType(run,a)       #将函数run和对象a绑定,添加实例方法,将run绑定到a，将对象a传递给self`
a.run()
B.run = run            #添加类方法
b = B()
b.run()



class Game(object):
    num = 0
    def __init__(self):
        self.name = 'lw'
    @classmethod             #类方法
    def add_num(cls):
        cls.num = 100
        print(cls.num)
   

    @staticmethod            #静态方法
    def print_menu():
        print('-----cf-----')
        print('---playgame---')
        print('---closegame---')
@staticmethod
def test():
    print('test static')

game = Game()
Game.add_num()
print(Game.num)
game.add_num()


Game.print_menu()
game.print_menu()

Game.test = test
Game.test()



###############斐波那契数列#######
def fib(times):
    n = 0
    a,b = 0,1
    while n<times:
        yield(b)
        a,b = b,a+b
        n+=1
    return 'over'

for i in fib(100):
    print(i,end = ' ')
##################################



def test():
    i = 0
    while i<10:
        temp = yield i
        print(temp)
        i +=1

p = test()
print(next(p))
print(p.send('a'))          #将a保留到temp里
        

####################################

def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

myclass = choose_class('foo')
print(myclass)
yourclass = choose_class('bar')
print(yourclass)

class Test():
    pass
print(Test())
a = type('test2',(),{})     #type是创建类对象的类
print(a)
a.name = 'tom'
a.age = 18
######################################

class Person(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'
    def __getattribute__(self,obj):    #属性访问拦截器
        if obj == 'subject1':
            print('log subject1')
            return 'reditect python'
        else:
            return object.__getattribute__(self,obj)
    def show(self):
        print('this show')

s = Person('python')
print(s.subject1)
print(s.subject2)
#####################################

############### map函数 #############
ret = map(lambda x:x*x,[1,2,3,4,5])
for tmp in ret:
    print(tmp,end=' ')

print(' ')
print('*'*50)

ret = map(lambda x,y:x+y,[1,2,3,4,5],[5,6,7,8,9])
for tmp in ret:
    print(tmp,end=' ')


print('')
print('*'*50)


a = [0,1,2,3,4,5,6]
b = ['sun','mon','T','W','TH','F','S']
def f1(a,b):
    return a,b

f = f1(a,b)
print(f)

d = map(f1,a,b)
print(list(d))

z = zip(a,b)
print(list(z))
#######################################

###############filter函数##############
a = filter(lambda x:x%2,[1,2,3,4])
print(list(a))

b = filter(None,"hello")
print(list(b))

#######################################

################reduce函数#############

from functools import reduce
print(reduce(lambda x,y:x+y,[1,2,3,4]))
#从1 --> x  ,2 ---> y,计算出x+y==3 然后将结果3--->x,在用列表中的3 ---->y, x+y一次类推，最后为10

print(reduce(lambda x,y:x+y,[1,2,3,4],5))   #起始值为5 
#######################################

############sorted函数#################
a = [12,564,156,165,3,123,56]  #将a从小到大排序
a.sort()
print(a)
a.sort(reverse=True)            #将a从大到小排序
print(a)

######################################

################partial偏函数#########
import functools
def showarg(*args,**kwargs):
    print(args)
    print(kwargs)

p1 = functools.partial(showarg,1,2,3)
print(p1(),end='\n\n')
print(p1(4,5,6))
print(p1(a='python',b='dayday'))

p2 = functools.partial(showarg,a=3,b='linux')
print(p2())
'''

############### 协程 ########################
'''
def simple_coroutine():
	print('--->启动协程')
	y = 10
	for i in range(5):
		x = yield y+i
	print('--->协程接收到了x的值:',x)

my_coro = simple_coroutine()
ret = next(my_coro)
print(ret)
my_coro.send(20)
my_coro.send(20)
my_coro.send(20)
'''
#############################################
#
###########  协程装饰器 #####################

import asyncio
import datetime

@asyncio.coroutine
def display_date(num,loop):
	end_time = loop.time() + 10.0
	while True:
		print('loop:{} time:{}'.format(num,datetime.datetime.now()))
		if(loop.time()+1.0)>=end_time:
			break
		yield from asyncio.sleep(2)

loop = asyncio.get_event_loop()
tasks = [display_date(1,loop),display_date(2,loop)]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()