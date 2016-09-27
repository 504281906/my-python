
#include "GG.h"
#include <windows.h>
#include <iostream>
#include <time.h>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;

SOCKET Client_Sock;
struct MsgInfo{
	int len; //数据包长度
	int code;
	int sign;
	char c[1024];
}msg,msg2;

struct postData{
    int data_len;        //4字节
    int data_len_2;        //4字节
    int message;        //2字节
    int secreat;            //1字节
    int presv;            //1字节
    char body[10];   // = "type@=loginreq/roomid@=846805/";
};

DLLEXPORT1 int client()
{
	WSADATA wsa;
	if (WSAStartup(MAKEWORD(1,1),&wsa)!=0)
	{
		return -1;
	}
	Client_Sock=socket(AF_INET,SOCK_STREAM,0);
	struct sockaddr_in servaddr;
	memset(&servaddr,0,sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(8601);
	servaddr.sin_addr.s_addr = inet_addr("123.150.206.162"); //openbarrage.douyutv.com的ip地址
	memset(servaddr.sin_zero,0,8);
	if (connect(Client_Sock, (struct sockaddr*)&servaddr,sizeof(servaddr)) < 0)
	{
		printf("连接失败\n");
		return -1;
	}
	return Client_Sock;
}

DLLEXPORT1 void c_init(char *room_id)
{
	strcpy_s(msg.c,"type@=loginreq/username@=modiz/password@=6771152/roomid@=");
	strcat(msg.c, room_id);
	strcat(msg.c, "/");
	msg.sign = 689;

	msg.len = sizeof(msg.c) + sizeof(msg.code) + sizeof(msg.sign);
	msg.code = msg.len;

	send(Client_Sock,(char *)&msg,sizeof(MsgInfo),0);
	//recv(Client_Sock,(char *)&msg2,sizeof(msg2),0);
	//cout<<"1:"<<msg2.c<<endl;

	strcpy_s(msg.c,"type@=joingroup/rid@=");
	strcat(msg.c,room_id);
	strcat(msg.c,"/gid@=-9999/");
	msg.sign = 689;
	
	msg.len = sizeof(msg.c) + sizeof(msg.code) + sizeof(msg.sign);
	msg.code = msg.len;
	send(Client_Sock,(char *)&msg,sizeof(MsgInfo),0);
	recv(Client_Sock,(char *)&msg2,sizeof(msg),0);
	//cout<<"2:"<<msg2.c<<endl;
}

DLLEXPORT1 void keeplive()
{
	time_t t;
	int j;
	j = time(&t);
	stringstream ss;
	string str;
	ss<<j;
	ss>>str;

	strcpy_s(msg.c,"type@=keeplive/tick@=");
	strcat(msg.c,str.c_str());
	strcat(msg.c,"/");
	msg.sign = 689;

	msg.len = sizeof(msg.c) + sizeof(msg.code) + sizeof(msg.sign);
	msg.code = msg.len;
	send(Client_Sock,(char *)&msg,sizeof(MsgInfo),0);
	recv(Client_Sock,(char *)&msg2,sizeof(msg),0);
	//cout<<"3:"<<msg2.c<<endl;

}
//https://www.douyu.com/291514
DLLEXPORT1 char* getmsg()
{
	recv(Client_Sock,(char *)&msg2,sizeof(msg2),0);
	//puts(msg2.c);
	//string s;
	//s=msg.c;
	return msg2.c;
}

DLLEXPORT1 void writefile()
{
	freopen("t1.txt","a+",stdout);
}

int main()
{
	/*client();
	c_init("810263");
	int i=0;
	while(1)
	{
		if (i % 2==0)
		{
			keeplive();
		}
		cout<<getmsg()<<endl;  
		i++;
	}
	system("pause");
	return 0;*/
}