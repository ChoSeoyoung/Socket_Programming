from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    flag = input('로그인 하시겠습니까?(T/F): ')
    clientSocket.sendto(flag.encode(),(serverName, serverPort))
    if(flag == 'F'):
        break
    
    #id를 입력받음
    member_id = input('Please enter your id: ')
    clientSocket.sendto(member_id.encode(),(serverName, serverPort))
    
    #id입력 결과 출력/ 비밀번호 확인 or 회원등록 절차
    is_member, serverAddress = clientSocket.recvfrom(2048)
    is_member = is_member.decode()
    if(is_member=="True"):
        member_pw = input('Please enter your pw: ')
    else:
        #회원등록
        print(member_id+"님 안녕하세요. 비밀번호를 설정해주세요.")
        while True:
            member_pw = input('Please enter your pw: ')
            tmp = input('Please enter your pw again: ')
            if(member_pw == tmp):
                break
            else:
                print("비밀번호가 서로 다릅니다. 다시 입력해주세요")
    clientSocket.sendto(member_pw.encode(),(serverName, serverPort))
    
    #회원이면 로그인 성공 여부 출력
    #비회원이면 회원가입 절차
    success, serverAddress = clientSocket.recvfrom(2048)
    success = success.decode()
    if(success == 'True'):
        print(member_id+"님 로그인되었습니다")
    elif(success == 'True'):
        print("잘못된 id/pw입니다.")
    elif(success == "New"):
        print("회원등록이 완료되었습니다")
print("Close the client socket")
clientSocket.close()
