from socket import *

ID_table={'서영':'20', '민지':'19', '창수':'12', '철수':'5', '민석':'22'}

serverPort=12000
serverSocket=socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready to receive")
while True:
    #로그인 지속 여부 확인
    flag, clientAddress = serverSocket.recvfrom(2048)
    flag = flag.decode()
    if(flag=='F'):
        break

    member_id, clientAddress = serverSocket.recvfrom(2048)
    member_id = member_id.decode()
    #회원/비회원 여부 확인
    if(member_id in ID_table):
        print(member_id+"님은 회원입니다. 비밀번호가 필요합니다.")
        is_member = "True"
    else:
        print(member_id+"님은 비회원입니다. 회원등록이 필요합니다.")
        is_member = "False"
    serverSocket.sendto(is_member.encode(),clientAddress)

    #비밀번호를 입력받음
    member_pw, clientAddress = serverSocket.recvfrom(2048)
    member_pw = member_pw.decode()

    if(is_member=="True"):
        #회원이면 비밀번호를 확인함
        if(ID_table[member_id]==member_pw):
            print("로그인 성공")
            success = "True"
        else:
            print("잘못된 id/pw입니다.")
            success = "False"
    else:
        #비회원이면 ID_Table에 등록함
        print("신규 회원입니다.")
        ID_table[member_id]=member_pw
        success = "New"

    serverSocket.sendto(success.encode(),clientAddress)
print("Close the server socket")
serverSocket.close()
