import socket 
from multiprocessing import Process
import re


###################################       静态页面
'''
def Deal_client(c_socket):
	print('线程开始处理')
	recvData = c_socket.recv(1024)
	print('recvData:%s'%recvData)

	req_line = recvData.splitlines()     #???
	req_file_name = str(req_line[0],encoding='utf-8').split(' ')[1]
	print(req_file_name)
	#for line in req_line:
	#	print(line)

	try:
		f = open('html' + req_file_name,'rb')
	except IOError:
		print('出错')
		res_start_line = 'HTTP/1.1 404 Not Found\r\n'
		res_header = 'server:My server\r\n'
		res_body = 'the file is not found!'
	else:
		print('打开成功')
		f_data = f.read().decode('utf-8')
		print('内容',f_data)
		f.close()

		res_start_line = 'HTTP/1.1 200 OK\r\n'
		res_header = 'server:my server\r\n'
		res_body = f_data
	res = res_start_line + res_header + '\r\n' +res_body
	print(res)

	c_socket.send(bytes(res,'utf-8'))
	c_socket.close()




def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.bind(('',8000))
	s.listen(10)

	while True:
		c_socket,c_addr = s.accept()
		print(c_addr)

		c_process = Process(target=Deal_client,args=(c_socket,))
		c_process.start()
		c_socket.close()



if __name__ == '__main__':
	main()

'''
####################################################


####################################################      静态页面 Class写法
'''
server_address = ('',7788)
class HTTPServer(object):
	def __init__(self):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.s.bind(server_address)

	def start(self):
		self.s.listen(10)
		while True:
			c_socket,c_addr = self.s.accept()
			c_process = Process(target=self.ClientHandle,args=(c_socket,))
			c_process.start()
			c_socket.close()

	def ClientHandle(self,c_socket):
		print('----收到客户端链接----')
		recvData = c_socket.recv(1024)
		print('RecvData:%s'%recvData)

		req_line = recvData.splitlines()     #???
		req_file_name = str(req_line[0],encoding='utf-8').split(' ')[1]
		print(req_file_name)
		#for line in req_line:
		#	print(line)

		try:
			f = open('html' + req_file_name,'rb')
		except IOError:
			print('出错')
			res_start_line = 'HTTP/1.1 404 Not Found\r\n'
			res_header = 'server:My server\r\n'
			res_body = 'the file is not found!'
		else:
			print('打开成功')
			f_data = f.read().decode('utf-8')
			print('内容',f_data)
			f.close()

			res_start_line = 'HTTP/1.1 200 OK\r\n'
			res_header = 'server:my server\r\n'
			res_body = f_data
		res = res_start_line + res_header + '\r\n' +res_body
		print(res)
		c_socket.send(bytes(res,'utf-8'))
		c_socket.close()



def main():
	http_server = HTTPServer()
	http_server.start()



if __name__ == '__main__':
	main()

'''
#######################################################
#
#


