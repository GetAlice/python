from multiprocessing import Process
import socket

#############################################################

def handle_client(c_socket):
	req_data = c_socket.recv(1024)
	print(req_data)

	res_start_line = 'HTTP/1.1 200 OK\r\n'
	res_headers = 'server:my server\r\n'
	res_body = 'hello world'
	res = res_start_line + res_headers +res_body
	
	print('response date:',res)

	c_socket.send(bytes(res,encoding='utf-8'))
	c_socket.close()

def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(('',7788))
	s.listen(10)

	while True:
		c_socket,c_address = s.accept()
		c_t = Process(target=handle_client,args=(c_socket,))
		c_t.start()
		c_socket.close()

if __name__ == '__main__':
	main()

#############################################################