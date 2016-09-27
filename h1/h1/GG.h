
#define DLLEXPORT _stdcall
#define DLLEXPORT1 extern "C" _declspec(dllexport) 

DLLEXPORT1 int  client();
DLLEXPORT1 void  c_init(char *room_id);
DLLEXPORT1 void  keeplive();
DLLEXPORT1 char* getmsg();