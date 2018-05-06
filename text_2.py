'''
#num = int(input("请选择:"))
for num in range(1,4):
    if num == 1:
        name = input("1:请输入名字：")

    elif num == 2:
        job = input("2:请输入职位：")

    elif num == 3:
        qqnum = input("3:请输入qq号：")

    else:
        print("1-3")
print("#"*20)
print("名字：" + name)
print("职位:"+job)
print("qq号:" + qqnum)
'''

cookie = 'anonymid=jfgfivcbazwm36; ' \
         '_r01_=1; ' \
         'ln_uact=18689393892; ' \
         'ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; ' \
         '_de=E0EDF5D325EC1DBA1D9123C741F918C1; ' \
         'depovince=GUZ; ' \
         'ick_login=6be5197b-c163-4429-b58e-75d2abc70648; jebecookies=48921195-5c61-4615-8cbb-51e19985e85c|||||; ' \
         'jebe_key=11bfc5d3-b7fe-42c5-906c-82a149aa932d%7Cd2d0ee61a963d41f217dde8146469b12%7C1522566662335%7C1%7C1524539451045'

CookieList_1 = cookie.split(';')
#print(b)
dic1 = {}
#print('\n',"#"*100,'\n')
for CookieNum in CookieList_1:
	CookieList_2 = CookieNum.split('=')
	CookieKey_1 = CookieList_2[0]
	CookieValue_1 = CookieList_2[1]
	dic1[CookieKey_1] = CookieValue_1
	#cc[c[0]] = c[1]
print(str.ljust('keys:',15,' '),' \t','value:')
print("#"*180)
for keys,value in dic1.items():
	print(str.ljust(keys,15,' '),'=\t',value)


	