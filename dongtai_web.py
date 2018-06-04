import sys
import socket
from multiprocessing import Process

#####################################################   动态页面

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
			print('[%s,%s]用户链接'%(c_socket,c_addr))
			c_process = Process(target=self.handle_client,args=(c_socket,))
			c_process.start()
			c_socket.close()


	def start_response(self,status,headers):
		response_headers = 'HTTP/1.1' + status + '\r\n'
		for header in headers:
			response_headers += '%s: %s\r\n'%header
		self.response_headers = response_headers


	def handle_client(self,c_socket):
		recvData = c_socket.recv(1024)
		print('recvData:')
		print(recvData)

		req_line = recvData.splitlines()     #???
		req_file_name = str(req_line[0],encoding='utf-8').split(' ')[1]
		method = str(req_line[0],encoding='utf-8').split(' ')[0]
		print(req_file_name)
		file_name = req_file_name.replace('/','')
		print(file_name)

		if file_name.endswith('.py'):
			try:
				m = __import__(file_name[0:-3])
				print('导入的模块是',m)
			except:
				self.response_headers = 'HTTP/1.1 404 NOT FOUND \r\n'
				response_body = 'NOT FOUND'
			else:
				env = {
					'PATH_INFO':req_file_name,
					'METHOD':method
				}
				response_body = m.application(env,self.start_response)

			response = self.response_headers + '\r\n' + response_body
		else:
			try:
				f = open('html' + '/' +file_name,'rb')
			except IOError:
				print('出错')
				res_start_line = 'HTTP/1.1 404 Not Found\r\n'
				res_header = 'server:My server\r\n'
				res_body = 'the file is not found!'
			
			else:
				f_data = f.read()
				f.close()

				res_start_line = 'HTTP/1.1 200 OK\r\n'
				res_header = 'server:my server\r\n'
				res_body = f_data.decode('utf-8')
			response = res_start_line + res_header + '\r\n' + res_body
		c_socket.send(bytes(response,'utf-8'))
		c_socket.close()



def main():
	http_server = HTTPServer()
	http_server.start()

if __name__ == '__main__':
	main()