####################### 正则表达式
import re

###########################  match 从头查起，第一个不对就不继续查
'''
res = re.match('www','www.baidu.com')   #match是从头开始匹配的，所以www能匹配，baidu不能匹配
print(res)
print(res.group())
'''

'''
patten = 'www'
str1 = 'www.baidu.com'
res = re.match(patten,str1)
print(res)
'''

'''
print(re.match('...','a'))
print(re.match('...','ab'))
print(re.match('...','abc'))
print(re.match('...','12abc'))
'''

'''
ret = re.match('[A-Z][a-z]*','Mn')
print(ret)
'''

'''
ret = re.match('[a-zA-Z0-9_.]{6}','daskjdh21as')
print(ret)
ret = re.match('[a-zA-Z0-9_.]{8,20}','daskjdh21as')    #至少8个最多20次
print(ret)
'''

'''
ret = re.match('^1[3578]\d{9}$','17737656018')
print(ret)

ret = re.match('[\w]{4,20}@163\.com$','xiaowang@163.com')  #  $是结尾符号
print(ret)

ret = re.match(r'[0-9]\d?$|100','0')   #匹配0-100
print(ret)

ret = re.match(r'(<h1>)(.*)(</h1>)','<h1>title1</h1>')
print(ret.group(1))    #取第一个括号的内容
print(ret.groups())    #将所有括号里的内容放到元组里


ret = re.match('\w{4,20}@(163|126|qq)\.com$','test@163.com')
print(ret)
ret = re.match('\w{4,20}@(163|126|qq)\.com$','test@126.com')
print(ret)
ret = re.match('\w{4,20}@(163|126|qq)\.com$','test@gmail.com')
print(ret)
ret = re.match('\w{4,20}@(163|126|qq)\.com$','test@163.comwqe')
print(ret)

ret = re.match('([^-]*)-(\d+)','010-13513513')
print(ret)

ret = re.match('<[a-zA-Z]*>\w*<[/a-zA-Z]*>','<html>dsad</html>')
print(ret)

ret = re.match(r'<([a-zA-Z]*)>\w*</\1>','<html>dsad</htmlfdsfds>')
print(ret)
ret = re.match(r'<([a-zA-Z]*)>\w*</\1>','<html>dsad</html>')    #第一对<>是什么，后面的<>就是/什么
print(ret)


ret = re.match(r'<(\w*)><(\w*)>.*</\2></\1>','<html><h1>www.baidu.com</h1></html>')
print(ret)

ret = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>','<html><h1>www.baidu.com</h1></html>')
print(ret)
'''

##################################################
#
#
##################################################   search
'''
ret = re.search(r'\d+','阅读999')
print(ret)
'''
##########search  只找到第一个匹配的就结束
'''
s = 'ddlab<h1></html>daydaylab</h1>'     #\w只有a-z A-Z 1-9 和_
ret = re.search(r'\w+</h1>',s)
print(ret)
'''
#############################################  findall 找到所有匹配的
'''
s = 'ddlab</h1></html>daydaylab</h1>' 
ret = re.findall(r'\w+</h1>',s)
print(ret)

ret = re.findall(r'\d+','python=999,index=1000,adssad=213213')
print(ret)
'''
############################################sub 将匹配到的数据替换
'''
ret = re.sub(r'php','123','python php c c++ php')
print(ret)

def replace_1(num):
	print(num.group())
	return '100'
ret = re.sub(r'\d+',replace_1,'python=1000,php=10')
print(ret)


def replace_1(num):
	print(num.group())
	r = int(num.group())+50
	return str(r)
ret = re.sub(r'\d+',replace_1,'python=1000,php=10')
print(ret)

#############

ret = re.sub(r'\d+','998','python=997')
print(ret)


def add_1(num):
	r = int(num.group())+1
	return str(r)
ret = re.sub(r'\d+',add_1,'python=997')
print(ret)
'''

##################################### split 切割制服串
'''
ret = re.split(r':| ','info:xiaozhang 33 shandong')
print(ret)

s = 'dasdsa:dadsa,dasqw-dqwdqw'
ret = re.split(r':|,|-',s)
print(ret)
'''
#####################################


###############################贪婪和非贪婪
'''
str1 = 'this is 234-235-22-423'
r = re.match(r'.+(\d+-\d+-\d+-\d+)',str1)
print(r)
print(r.group(1))

r = re.match(r'(.+)(\d+-\d+-\d+-\d+)',str1) #默认贪婪，给第一个\d留一个就够了
print(r)
print(r.group(1))
print(r.group(2))


r = re.match(r'(.+?)(\d+-\d+-\d+-\d+)',str1)
print(r)
print(r.group(1))
print(r.group(2))
'''
#####################################
#
#
#########################练习

s = 'http://www.baidu.com/dasdsa/dasdsa'
ret = re.sub(r'(http://.+?/).*',lambda x:x.group(1),s)
print(ret)