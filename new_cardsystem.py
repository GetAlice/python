a = '''1.添加名片
2.删除名片
3.修改名片
4.查询名片
5.退出系统'''

card = {}
card_list = {'深职魅影':{'name':'深职魅影','qq':'21312'}}
show_card = []


def choose():
	print(a,'\n'+'*'*50)

class CardList(object):
	for i in card_list.keys():
		show_card.append(i)
	def show_cardlist(self):
		print(show_card)
		return card_list

	def find_card(self):
		fin = input('请输入要查找的名片')



choose()

class Add_card(object):
	def add(self,name,qq):
		self.name = name
		self.qq = qq
		card['name'] = self.name
		card['qq'] = self.qq
		card_list[self.name] = card


class Del_card(object):
	def delete(self,name):
		self.name = name
		if self.name in card_list:
			del card_list[self.name]
			print('删除完毕')
			print(card_list)


class Alter_card(object):
	def AltName(self,name,altname):
		name_bak = name
		card_bak = card_list[name]
		self.name = altname
		card_bak['name'] = self.name
		del card_list[name_bak]
		card_list[self.name] = card_bak
		#print(card_bak)          			 #查看名片内容
		print(card_list)         			 #查看名片夹内容

	def AltQQ(self,name,QQ):
		card_bak = card_list[name]
		self.qq = QQ
		card_bak['qq'] = self.qq
		print(card_list) 

def num_2():
	delname = input('输入要删除的名片')
	dc = Del_card()
	dc.delete(delname)
	print('删除成功')


def alta(altname):
	global alt_name
	if alt_name not in card_list:
		while True:
			alt_name = input('没有这个名片，请重新输入')
			if alt_name in card_list:
				break
	if alt_name in card_list:
		alt = Alter_card()
		o = input('请输入要修改的选项')
		if o == 'name':
			a_name = input('请输入要修改的内容')
			alt.AltName(alt_name,a_name)
		if o == 'qq':
			a_qq = input('请输入要修改的内容')
			alt.AltQQ(alt_name,a_qq)
#class 
#
fi = CardList()
while True:
	try:
		num = int(input('请输入数字'))
		if num == 1:
			name = input('输入名字')
			qq = input('输入QQ')

			a = Add_card()
			a.add(name,qq)
			print('添加成功')
			print(card_list)

		elif num == 2:
			fi.show_cardlist()
			num_2()

		elif num == 3:
			fi.show_cardlist()
			alt_name = input('请输入要修改的名片')
			alta(alt_name)
		
		elif num == 4:
			#fi = CardList()
			fi.show_cardlist()


		elif num == 5:
			break


	except:
		print('输入错误,请重新输入')





