# Socket_Programming
데이터를 네트워크를 통해 전송하기 위해서는 소켓을 이용해야 한다.
소켓을 이용한 server와 client의 통신과정은 다음과 같다.

![image](https://user-images.githubusercontent.com/74875490/165886044-1dd6be35-ea48-46fd-acdd-b90331a3a5c2.png)

1. client socket
- socket(): 사용할 소켓을 생성한다.
- connect(): IP주소와 포트번호로 특정되는 대상에 연결 요청을 보낸다.
- send()/recv(): 서버와 클라이언트 사이에 데이터를 전송한다.
- close(): 소켓을 닫는다.

2. server socket
- socket(): 사용할 소켓을 생성한다.
- bind: IP주소와 포트번호를 결합한다.
- listen(): client의 연결을 기다린다.
- send()/recv(): 서버와 클라이언트 사이에 데이터를 전송한다.
- close(): 소켓을 닫는다.
