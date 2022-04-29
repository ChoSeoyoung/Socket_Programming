from socket import *

ID_table={'서영':'20', '민지':'19', '창수':'12', '철수':'5', '민석':'22'}

serverPort=12000
serverSocket=socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready to receive")
while True:
    member_id, clientAddress = serverSocket.recvfrom(2048)
    member_id = member_id.decode()
    print(member_id)
    member_pw, clientAddress = serverSocket.recvfrom(2048)
    member_pw = member_pw.decode()
    print(member_pw)
    #회원이면 PW를 확인함
    if(member_id in ID_table):
        if(ID_table[member_id]==member_pw):
            is_member = 'Success'
        else:
            is_member = 'Fail'
    #비회원이면 ID_Table에 등록함
    else:
        is_member = 'False'
        ID_table[member_id]=member_pw
    serverSocket.sendto(is_member.encode(),clientAddress)