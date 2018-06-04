import socket       #socket模块   网络编程模块
import threading
import sys
import select
import os
import time
##################### UDP编程 ####################
##############  UDP
'''
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

binAddr = ('',8899)
s.bind(binAddr)    #绑定自己的地址到套接字

ser_ip_port = ('192.168.1.114',8080)
s.sendto(b'hello world',ser_ip_port)   			   #socket传递的都是bytes字节，所以要用b转换
s.sendto('hello world1'.encode('utf-8'),ser_ip_port) 
s.sendto('大伟哥飞妈'.encode('gbk'),ser_ip_port)   #用gbk或者bg2312编码发送中文


resvData = s.recvfrom(1024)                        #接收UDP数据，和recv类似
content,addr_info = resvData
print(content.decode('gbk'))
print(addr_info)

s.close()
'''
##############################################
#
##################  聊天室  ##################
'''
def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	bin_addre = ('192.168.1.113',8899)
	s.bind(bin_addre)


	while True:                    #循环接收数据
		recvData = s.recvfrom(1024)
		s.sendto(recvData[0],recvData[1])   #0数据  1地址信息
		print('from[%s] :%s'%(recvData[1],recvData[0].decode('gbk')))

if __name__ == '__main__':
	main()

'''
###############################################

################### 模拟QQ ####################

'''
def recvData(s):
	while True:
		recvData = s.recvfrom(1024)
		content,dest_info = recvData
		print('')
		print('Recv from:%s :%s'%(dest_info,content.decode('gbk')))
        print('')

def sendData(s,ser_ip_port):
	while True:
		content = input('send:')
		s.sendto(content.encode('gbk'),ser_ip_port)

ser_ip_port = ('192.168.1.114',8080)
sour_ip_port = ('192.168.1.113',8890)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #DGRAM是UDP
s.bind(sour_ip_port)

t_recv = threading.Thread(target=recvData,args=(s,))
t_send = threading.Thread(target=sendData,args=(s,ser_ip_port))

t_recv.start()
t_send.start()

t_recv.join()
t_send.join()

s.close()
'''
#######################################
#
######### UDP广播 #####################
'''
dest = ('192.168.1.255',8080)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) #广播
s.sendto(b'hi',dest)
'''
########################################
#
#
#
#
############################## TCP编程 #############################

######## 服务器
'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # TCP
s.bind(('192.168.1.113',8890))

s.listen(5)    #监听链接，并发数5

#socket是新的客户端,info表示客户端的ip和端口
while  True:
	client_socket,client_info = s.accept()    #被动接收客户端链接，阻塞式等待链接到来并返回

	recvData = client_socket.recv(1024)
	print('client_socket is %s'%str(client_socket))
	print('*'*50)
	print('从客户端(%s)接收的数据是:%s'%(client_socket,recvData.decode('gbk')))
	print('*'*50)

	client_socket.close()
s.close()
'''
#######################

#####################TCP客户端
'''
tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
svrAddr = ('192.168.1.112',8899)
tcpClient.connect(svrAddr)       #发送到的服务器地址

#sendData = input('发送的数据')
tcpClient.send('吃饭吃饭'.encode('gbk'))
#客户端tcpClient发送出去后返回的值是NONE
recvData = tcpClient.recv(1024)   #接收数据
print(recvData.decode('gbk'))

tcpClient.close()
'''
#######################################
#
########## TCP聊天程序
'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

bind_addr = ('192.168.1.113',8890)
s.bind(bind_addr)
s.listen(5)

while True:
	client_socket,client_info = s.accept()
	while True:
		recvData = client_socket.recv(1024)
		if len(recvData) >0:
			print('从客户端收到数据%s'%recvData.decode('gbk'))
		else:
			break

		sendData = input('send:')
		client_socket.send(sendData.encode(gbk))

	client_socket.close()

s.close()

'''
'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bind_addr2 = ('192.168.1.112',8890)
s.connect(bind_addr2)

while True:
	send_data = input('请输入发送的数据:')
	if len(send_data)>0:
		s.send(send_data.encode('gbk'))
	else:
		break

	recv_data = s.recv(1024)
	print(recv_data.decode('gbk'))

s.close()
'''

########################################
#
######### 多线程服务器 ########################
'''
def echo_client(new_s):
	send_date = input('请输入回复内容')
	news_s.send(send_data.encode('gbk'))


def dealClinet(new_s,addr_info): #处理客户端
	while True:
		recvData = new_s.recv(1024)
		if len(recvData) > 0:
			print('recv[%s] :%s'%(addr_info,recvData.decode('gbk')))
			echo_client(new_s)
		else:
			print('客户端%s已经关闭',%addr_info)
			break
	new_s.close()   #关闭new_s这个线程



def main():
	serSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	bind_addr = ('',8890)   #本机（服务器的地址）
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.bind(bind_addr)		#设置本机（服务器的）地址
	s.listen(5)

	try:
		while True:
			print('-----正在等待客户端的链接---')
			new_s,addr_info = s.accept()
			print('-----收到一个客户端的链接,创建一个新的线程处理这个链接%s---'%str(addr_info))
			client_shread = threading.Thread(target=dealClinet,args=(new_s,addr_info))
			client_shread.start()
	finally:
		s.close()

if __name__ == '__main__':
	main()
'''
#################################################

#############  多进程模式  ######################

#################################################
#
############ 单进程服务器（非阻塞模式）##########
'''
g_socketlist = []

def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	local_addr = ('192.168.1.113',8891)  #服务器（本机）IP
	s.bind(local_addr)

	s.listen(10)
	s.setblocking(False)

	while True:
		try:
			new_client_info = s.accept()
		except Exception as result:
			pass
		else:
			print('-----一个新的客户端[%s]来了----'%str(new_client_info))
			new_client_info[0].setblocking(False)
			g_socketlist.append(new_client_info)

			print('*'*50)
			print(g_socketlist)
			print('*'*30)

		needDelClientInfiList = []
		for clientsocket,clientaddr in g_socketlist:
			try:
				recvData = clientsocket.recv(1024)
				if len(recvData) > 0:
					print('recv[%s] :%s'%(clientaddr,recvData.decode('gbk')))
				else:
					print('[%s]客户端已经关闭'%clientaddr)
					clientsocket.close()
					needDelClientInfiList.append(clientsocket,clientaddr)
			except Exception as result:
				pass

		for needDelClientInfiList in needDelClientInfiList:
			g_socketlist.remove(needDelClientInfiList)

if __name__ == '__main__':
	main()
'''
##########################################################
#
#
################ select版TCP服务器 #########################
######回显服务器
'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.1.113',8890))
s.listen(5)

inputs = [s]#sys.stdin]
running = True

while True:
	readable,writeable,exceptional = select.select(inputs,[],[])
	print(readable)
	for sock in readable:
		if sock == s:
			conn,addr = s.accept()  #接收新的套接字
			inputs.append(conn)
			print(inputs)

		else:
			data = sock.recv(1024)  #获取客户端发送的数据
			print('*',*)
			print(data.decode('gbk'))
			if data:
				sock.send(data)
			else:
				inputs.remove(sock)
				sock.close()
s.close()
'''
##########################################################
#
###############  epoll版tcp服务器 和 select版TCP服务器一样，但是套接上限大于1024    好像自由linux能用，做不了实验

#############################################################################


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',8089))
server.listen(5)

def duoxc(Data,ippr):
	sayData = Data
	sayPort = ippr
	while True:
		client_spe = threading.Thread(target=duoliaotian,args=(sayData,sayPort))
		client_spe.start()
		time.sleep(2)

def duoliaotian(Data,ippr):
	#print('进入子线程%s'%os.getpid())
	spe = Data.recv(1024).decode('gbk')
	ip = ippr[0]
	print(ip,':',spe)
	Data.close()


while True:
	print('进入')	
	sayData,sayPort = server.accept()
	s = threading.Thread(target=duoxc,args=(sayData,sayPort))
	s.start()
	#while True:
		#print(sayData.recv(1024).decode('gbk'))
		#duoliaotian(sayData,sayPort)
	#	client_spe = threading.Thread(target=duoliaotian,args=(sayData,sayPort))
	#	client_spe.start()
	#	time.sleep(2)
		#client_spe.close()
		#break