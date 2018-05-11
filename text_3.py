a = '''1.添加名片
2.删除名片
3.修改名片
4.查询名片
5.退出系统'''
print(a,'\n'+'*'*50)

def card_name():
	if name in CardDic:
		del CardDic[name]
def show_CardDic():
	clist = []
	for n in CardDic.keys():
		clist.append(n)
	return(print(clist))



CardDic = {'深职魅影':{'姓名':'深职魅影','QQ':'1042970096','电话':11111111111},'婆':{'姓名':'婆','QQ':'1321','电话':'123123'}}
while True:
	temp = input('请输入您的操作序号')
	if (not temp.isdigit()):
		print('请输入数字1-5')
		continue
	num = int(temp)
	if 1 > num or num > 5:
		print('请输入正确的数字')
	if num == 1:
		name = input('请输入名字')
		qq = input('请输入QQ')
		tel = input('请输入电话')
		card_1 = {}
		card_1['姓名'] = name
		card_1['QQ'] = qq
		card_1['电话'] = tel
		CardDic[card_1['姓名']] = card_1
		print(CardDic)
		continue
	if num == 2:
		show_CardDic()
		#for n in CardDic.keys():
		#	print('名片名:'+n,end=';\n')
		name = input('输入要删除的名片')
		if name not in CardDic:
			while True:
				name = input('输入错误，请输入已有的名片')
				if name in CardDic:
					break
		if name in CardDic:
			del CardDic[name]
			print('删除成功')
			print(CardDic)

	if num == 3:
		show_CardDic()
		#for n in CardDic.keys():
		#	print('名片名:'+n,end=';\n')
		name = input('\n请输入要修改名片的名字')
		if name not in CardDic:
			while True:
				name = input('没有这张名片，请从新输入名片名')
				if name in CardDic:
					break
		if name in CardDic:					
			for i in CardDic:
				if name == i:
					card = CardDic[name]
					print(card)
					o = input('请输入要修改的选项:')
					if o not in card:
						while True:
							o = input('请输入名字，QQ 或者 电话')
							if o in card:
								break					
					if o in card:
						neirong = input('请输入修改的内容')
						card[o] = neirong
						if o == '姓名':
							name_bak = neirong
							card_bak = card
							del CardDic[i]
							CardDic[name_bak] = card_bak	
						print(card)
						print(CardDic)
						print('修改完毕')
						break	
	if num == 4:
		i = 0;
		name = input('请输入查询的名字')
		while True:
			if name in CardDic:
				for n in CardDic:
					i = 1
					print(CardDic[name])
					break
				break		
			if i == 0:
				print('查无此人')
				name = input('请重新输入查询的名字')
				continue


	if num == 5:
		print('感谢使用本系统')
		break
	#else:
	#	print('请输入1-5的操作序号')
		