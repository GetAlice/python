'''
class Student(object):
	classroom = 101
	
	def  __init__(self,name,age):    #默认调用初始化的方法,类的实例化方法		
		self.__name = name
		self.__age = age
	def print_age(self):
		print('%s: %s: %s'%(self.name,self.age,self.classroom))

	def get_name(self):
		return self.__name
	def set_name(self):
		self.__name = name

	@property                         #类装饰器
	def age(self):
		return self.__age

	@age.setter
	def age(self,age):
		self.__age = age
	@age.deleter
	def age(self):
		self.__age = 0
		print('删除数据')

	@staticmethod    #静态方法
	def f1():
		pass

	@classmethod     #类方法    
	def f2(cls):
		pass

obj = Student('jack',18)
print(obj.age)
obj.age = 19
print(obj.age)
del obj.age
print(obj.age)


class Student_2(Student):
	def __init__(self,name,age,grade):
		#Student.__init__(self,name,age)
		        ######等于#####
		#print(dir(Student_2))
		super(Student_2,self).__init__(name=name,age=age)
		self.__grade = grade       #私有成员，不能被类外面访问
	def print_age(self):
		print('%s: %s: %s: %s'%(self.name,self.age,self.classroom,self.__grade))

stu = Student('jack',18)
stu.classroom = 102
stu.print_age()

stu2 = Student('bo',20)
stu2.print_age()

stu3 = Student_2('po',20,1)
stu3.print_age()
######################################################
print('*'*50)

def speak(ani):
	if ani =='dog':
		print('wangwang')
	elif ani =='cat':
		print('miaomiao')
	elif ani =='colt':
		print('moumou')
	else:
		print('speak peple')

a,b,c,d = 'dog','cat','colt','peple'
speak(a)
speak(b)
speak(c)
speak(d)

print('*'*50)
##################
class Animal(object):
	def __init__(self,kind,voice):
		self.kind = kind
		self.voice = voice
	def speak(self):
		print(self.kind,self.voice)
a = Animal('dog','wangwang')
a.speak()


#多态类
class Animal:
	def kind(self):
		print('i am animal')

class dog(Animal):
	def kind(self):
		print('i am a dog')

class cat(Animal):
	def kind(self):
		print('i am a cat')

def show_kind(animal):
	animal.kind()

d = dog()
c = cat()
show_kind(d)
show_kind(c)

'''
class people(object):
	def __init__(self,name,age):
		self.__name = name
		self.__age =age
	def get_age(self):
		return self.__age
	def set_age(self,age):
		self.__age = age
	def del_age(self):
		print('obj年龄数据删除')

	age = property(get_age,set_age,del_age,'name')


print('*'*50)
print('###########    等于   ###########')
print('*'*50)

class People(object):
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
		print('这是init的age%d'%self.__age)

	@property
	def age(self):
		return self.__age
	@age.setter
	def age(self,age):
		self.__age = age
		print('这是setter的age%d'%self.__age)
	@age.deleter
	def age(self):
		self.__age = 0
		print('oobj删除数据')

obj = people('pjack',18)
oobj = People('Ppjack',19)
print(obj.age)
print(oobj.age)
obj.age = 20
oobj.age = 21
print(obj.age)
print(oobj.age)
del obj.age
del oobj.age
