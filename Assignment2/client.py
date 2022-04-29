from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    flag = input('계속하시겠습니까?(T/F): ')
    if(flag == 'F'):
        break
    #id를 입력받음
    member_id = input('Please enter your id: ')
    clientSocket.sendto(member_id.encode(),(serverName, serverPort))
    #pw를 입력받음
    member_pw = input('Please enter your pw: ')
    clientSocket.sendto(member_pw.encode(),(serverName, serverPort))

    #로그인 결과/회원 등록 결과 출력
    is_member, serverAddress = clientSocket.recvfrom(2048)
    is_member = is_member.decode()
    if(is_member == 'Success'):
        print(member_id+"님 로그인되었습니다")
    elif(is_member == 'Fail'):
        print("잘못된 id/pw입니다.")
    elif(is_member == 'False'):
        print("회원등록이 완료되었습니다")
clientSocket.close()