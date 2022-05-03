# socket_proggraming2
id, password를 보내면 server에서는 기록하여 등록시킨다. 그리고 두번째 입력시부터는 회원의 id에 해당되는 pw를 확인한다.

## 결과
![image](https://user-images.githubusercontent.com/74875490/166429045-fd43dc64-7dd8-45d3-988a-fef30e2d614e.png)
client에서 로그인 진행여부 응답에 따라 계속 프로그램을 진행하거나, 소켓을 종료한다. 일단 프로그램이 시작되면, client로부터 id를 입력받는다. 만약 id가 table에 이미 존재한다면 등록된 회원이라는 뜻이고, table에 존재하지 않는다면 비회원이라는 의미이다. 회원이라면 pw를 입력받아 등록된 pw와의 일치여부에 따라 로그인을 진행하고, 비회원이라면 신규 회원등록을 진행한다. 신규회원등록 과정에서 입력한 pw의 일치여부를 확인하여 pw를 확인하는 절차도 추가하였다.