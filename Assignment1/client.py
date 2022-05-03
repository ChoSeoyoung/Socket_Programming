from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    while True:
        message = input('Input lowercase/uppercase sentence: ')
        if(message.islower()):
            break
        elif(message.isupper()):
            break
        print("Message should be lowercase or uppercase.")
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    if(message=="break"):
        break
    
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
print("Close the client socket")
clientSocket.close()
