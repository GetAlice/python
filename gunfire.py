#创建一个自己对象
#2、创建一个抢对象
#3、创建一个弹夹对象
#4、创建一些子弹对象
#5、创建一个敌人对象
#6、老王吧子弹安装到弹夹中
#7、老王吧弹夹安装到枪中
#8、老王拿枪
#9、老王开枪打敌人


class Person(object):
	def __init__(self,name):
		#super(Person,self).__init__()
		self.name = name
		self.gun = None
		self.hp = 100
	def anzhuang_zidan(self,dan_jia,zi_dan):
		dan_jia.baocun_zidan(zi_dan)
	def anzhuang_danjia(self,gun,dan_jia):
		gun.baocun_danjia(dan_jia)

	def naqiang(self,gun):
		self.gun = gun

	def kou_ban_ji(self,diren):
		self.gun.fire(diren)

	def diao_xue(self,sha_shang_li):
		if self.hp <=0:
			print("已经死了")
		else:
			self.hp -= sha_shang_li

	def __str__(self):
		if self.gun:
			return "%s的血量为:%d,有枪%s"%(self.name,self.hp,self.gun)
		elif self.hp > 0:
			return '%s的血量为:%d,没枪'%(self.name,self.hp)
		else:
			return '已经死了'

class Gun(object):
	def __init__(self,name):
		#super(Gun,self).__init__()
		self.name = name
		self.danjia = None
	
	def baocun_danjia(self,dan_jia):
		self.danjia = dan_jia

	def fire(self,diren):
		zidan = self.danjia.tanchu_zidan()
		if zidan:
			zidan.dazhong(diren)
		else:
			print('没子弹了')

	def __str__(self):
		if self.danjia:
			return '枪的信息为:%s,%s'%(self.name,self.danjia)
		elif self.hp > 0:
			return '%s没弹夹'%(self.name)
		else:
			return None

class DanJia(object):
	def __init__(self,max_num):
		#super(DanJia,self).__init__()
		self.max_num = max_num
		self.zidan_list = []
	def baocun_zidan(self,zi_dan):
		self.zidan_list.append(zi_dan)
	def __str__(self):
		return "弹夹信息为:%d(当前)/%d(最大容量)"%(len(self.zidan_list),self.max_num)

	def tanchu_zidan(self):
		if self.zidan_list:
			return self.zidan_list.pop()
		else:
			return None

class ZiDan(object):
	def __init__(self,sha_shang_li):
		super(ZiDan,self).__init__()
		self.sha_shang_li = sha_shang_li

	def dazhong(self,diren):
		diren.diao_xue(self.sha_shang_li)


def main():
	laowang = Person('laowang')                    #1.创建一个自己为对象
	ak47 = Gun('ak47')							   #2.创建一个枪的对象
	dan_jia = DanJia(20)						   #  创建个装子弹的弹匣
	zi_dan = ZiDan(10)							   #3.创建一个子弹对象

	for i in range(18):
		laowang.anzhuang_zidan(dan_jia,zi_dan)
	print(dan_jia)


	laowang.anzhuang_danjia(ak47,dan_jia)
	print(ak47)

	laowang.naqiang(ak47)
	print(laowang)

	gebi_laosong = Person('隔壁老宋')
	print(gebi_laosong)

	for i in range(11):
		laowang.kou_ban_ji(gebi_laosong)
		print(laowang)
		print(gebi_laosong)

if __name__ == '__main__':
	main()

