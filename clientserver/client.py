from socket import socket, AF_INET, SOCK_STREAM
import time
import sys


def formatString(string):
    i=0
    while(i<len(string)):
        if(string[i]=='.' or string[i]=='\\'):
            string = string[0:i] + '\\' + string[i:]
            i += 1
        i += 1
    string = string + "\n.\r\n"
    return bytes(string,encoding="ascii")

def createMessageArray(messageFile):
    messageArray = []
    with open(messageFile,"r",encoding="ascii") as f:
        bytesNumber = f.readline()
        while bytesNumber != "":
            bytesNumber = int(bytesNumber[:-1])
            message = f.readline()
            if(message[-1]=='\n'):
                bytesNumber -= 1
            messageArray.append(formatString(message[:bytesNumber]))
            bytesNumber = f.readline()
    return messageArray

def createSignatureArray(signatureFile):
    signatureArray = []
    with open(signatureFile, "r", encoding="ascii") as f:
        for signature in f:
            signatureArray.append(bytes(signature.strip(),"ascii"))
    return signatureArray

def stripReturn(message):
    i=0
    while (i<len(message)):
        if(message[i]=='\n' or message[i]=='\r'):
            message = message[:i]+message[i+1:]
        i+=1
    return message

def main():
    argv = sys.argv[1:]
    if(len(argv) != 4):
        sys.exit("Need four arguments")
    host = argv[0]
    port = int(argv[1])
    messageArray = createMessageArray(argv[2])
    signatureArray = createSignatureArray(argv[3])
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"HELLO\r")
        data = s.recv(1024)
        data = data.decode()
        data = data.strip()
        if(data != "260 OK" and data != "260OK"):
            sys.exit("Didn't receive 260 OK")
        print(data)
        messageCounter = 0
        while(messageCounter < len(messageArray)):
            s.sendall(b'DATA')
            time.sleep(0.05)
            s.sendall(messageArray[messageCounter])
            data = s.recv(1024)
            data = data.decode()
            data = data.strip()
            if(data != "270 SIG" and data != "270SIG"):
                s.close()
                sys.exit("Didn't receive 270 SIG")
            print(data)
            data = s.recv(1024)
            #data = stripReturn(data)
            print(data.decode())
            if(data == signatureArray[messageCounter]):
                s.sendall(b'PASS\r')
                print("PASS")
            else:
                s.sendall(b'FAIL\r')
                print("FAIL")
            data = s.recv(1024)
            data = data.decode()
            data = data.strip()
            if(data != "260 OK" and data != "260OK"):
                s.close()
                sys.exit("Didn't receive 260 OK")
            print(data)
            messageCounter += 1
        s.sendall(b'QUIT\r')
        s.close()
    pass

if __name__ == "__main__":
    main()