from socket import *
k=('',6002)
s=socket(AF_INET,SOCK_STREAM)
s.bind(k)
s.listen(0)
while True:
	client,addr=s.accept()
	print "accept %s connect"%(addr,)
	while 1:
		date=client.recv(1024)
		while date!="":
			f=open('D:/monitor1.txt','a')
			f.write(date+'\r\n')
			print date
			date=client.recv(1024)
		break
	client.send('ok!')
	client.close()