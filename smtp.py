from socket import *
from base64 import *
import ssl
import getpass

YOUR_EMAIL =  input("Enter Your Email Address : ")
YOUR_PASSWORD = input("Enter Your Password : ")
YOUR_DESTINATION_EMAIL = input("Enter Email Destination : ")
YOUR_SUBJECT_EMAIL =  input("Enter Subject : ")
YOUR_BODY_EMAIL =  input("Enter Message : ")

msg = '{}. \r\nI love computer networks!'.format(YOUR_BODY_EMAIL)

mailServerURL = 'smtp.gmail.com'
mailPort = 587 


# Choose a mail server (e.g. Google mail server) and call it mailserver
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
# Account Authentication
# Fill in start
TLS = 1
if(TLS):
    strtlscmd = "STARTTLS\r\n".encode()
    clientSocket.send(strtlscmd)
    recv2 = clientSocket.recv(1024)
    sslClientSocket = ssl.wrap_socket(clientSocket)
    clientSocket = sslClientSocket

AUTH = 1
if(AUTH):
    EMAIL_ADDRESS = b64encode(YOUR_EMAIL.encode())
    EMAIL_PASSWORD = b64encode(YOUR_PASSWORD.encode())

    authorizationcmd = "AUTH LOGIN\r\n"

    sslClientSocket.send(authorizationcmd.encode())
    recv2 = sslClientSocket.recv(1024)
    print(recv2)

    sslClientSocket.send(EMAIL_ADDRESS + "\r\n".encode())
    recv3 = sslClientSocket.recv(1024)
    print(recv3)

    sslClientSocket.send(EMAIL_PASSWORD + "\r\n".encode())
    recv4 = sslClientSocket.recv(1024)
    print(recv4)
# Fill in end  

# Send MAIL FROM command and print server response.
# //Fill in start
mailfrom = "MAIL FROM: <{}>\r\n".format(YOUR_EMAIL)
clientSocket.send(mailfrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: "+recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# //Fill in end
# Send RCPT TO command and print server response.
# //Fill in start
rcptto = "RCPT TO: <{}>\r\n".format(YOUR_DESTINATION_EMAIL)
clientSocket.send(rcptto.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: "+recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# //Fill in end
# Send DATA command and print server response.
# //Fill in start
data = 'DATA\r\n'
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: "+recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# //Fill in end
# Send message data.
# //Fill in start

print("Trying to send subject & message")
sslClientSocket.send("Subject: {}\n\n{}".format(YOUR_SUBJECT_EMAIL, msg).encode())

# //Fill in end
# Message ends with a single period.
# //Fill in start
periodStr = '\r\n.\r\n' #send period, then blank line
clientSocket.send(periodStr.encode()) # sends period, then blank line
recv5 = clientSocket.recv(1024).decode() #amount of data to be sent
print (recv5) #print the message
if recv5[:3] != '250': #if the message does not print properly
    print ('250 reply not received from server.') #print out
# //Fill in end
# Send QUIT command and get server response.
# //Fill in start
quitcommand = 'QUIT\r\n'
sslClientSocket.send(quitcommand.encode())
message=clientSocket.recv(1024)
print (message)
clientSocket.close()
print('Was successful!')
# //Fill in end