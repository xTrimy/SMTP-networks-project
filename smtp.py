from socket import *
import ssl
import base64
import getpass

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
mailServerURL = 'smtp.gmail.com'
mailPort = 587 

# Choose a mail server (e.g. Google mail server) and call it mailserver
#mailserver = ("smtp.google.com",587) #//Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#//Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((mailServerURL,mailPort))
#//Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
 
#Send STARTTLS command and print server response.



enableTLS = 0
if(enableTLS):
    heloCommand = 'STARTTLS\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '220':
        print('220 reply not received from server.')

#Send User Auth
AUTH = 0
if(AUTH):
    Username="Your username to SMTP connection"
    Password= "Your Password to SMTP connection"
    UP=("\000"+Username+"\000"+Password)
    print (UP)
    UP=UP.strip("\n")
    login = 'AUTH PLAIN '+ UP + '\r\n'
    clientSocket.send(login.encode())
    recvLogin = clientSocket.recv(1024).decode()
    print (recvLogin)


# Send MAIL FROM command and print server response.
# //Fill in start
mailFrom = "MAIL FROM: <mohamed881999@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: "+recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# //Fill in end
# Send RCPT TO command and print server response.
# //Fill in start
rcptTo = "RCPT TO: <xxTrimy@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: "+recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# //Fill in end
# Send DATA command and print server response.
# //Fill in start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: "+recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# //Fill in end
# Send message data.
# //Fill in start
subject = "Subject: SMTP mail client testing \r\n\r\n" 
clientSocket.send(subject.encode())
message = input("Enter your message: \r\n")
clientSocket.send(message.encode())
recv_msg = clientSocket.recv(1024).decode()
print("Response after sending message body:"+recv_msg)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# //Fill in end
# Message ends with a single period.
# //Fill in start
periodStr = '.' #send period, then blank line
clientSocket.send(periodStr.encode()) # sends period, then blank line
recv5 = clientSocket.recv(1024).decode() #amount of data to be sent
print (recv5) #print the message
if recv5[:3] != '250': #if the message does not print properly
    print ('250 reply not received from server.') #print out
# //Fill in end
# Send QUIT command and get server response.
# //Fill in start
clientSocket.send("\r\nQUIT\r\n".encode())
message=clientSocket.recv(1024)
print (message)
clientSocket.close()
# //Fill in end