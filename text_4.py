'''
import sys
import os
os.chdir(r'D:\python\text')

for arg in sys.argv:
    print(arg,end="")
for arg in sys.argv[1:]:
    print(arg)
try:
    f = open(arg,'r')
except:
    print('cannot open',arg)
else:
    print(arg,'has',len(f.readlines()),'lines')
    f.close()

'''

class MyExcept(Exception):           		   #自定义异常
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return  self.message

sex = int(input('please input num'))
try:
	if sex == 1:
		print('male')
	elif sex == 0:
		print('female')
	else:
		print('not male not female')
		raise MyExcept('非法输入')             #抛出上面自定义的异常类
except MyExcept as e:
	print(e)