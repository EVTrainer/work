from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import hashlib
import sys

def createKeyArray(keyFile):
    keyArray = []
    with open(keyFile,"r",encoding="ascii") as f:
        for key in f:
            keyArray.append(key.strip())
        return keyArray
    
def stripMessage(message):
     message = message[:findMessageEnd(message)]
     i=0
     while(i<len(message)-1):
        if(message[i]==ord('\\')):
            message = message[0:i] + message[i+1:]
        i += 1
     return message

def findMessageEnd(message):
    for i in range(len(message)-2):
        if(message[i] == ord('\n') and message[i+1] == ord('.') and (message[i+2] == ord('\n') or message[i+2] == ord('\r'))):
            return i

def main():
    argv = sys.argv[1:]
    if(len(argv) != 2):
        sys.exit("Expected 2 arguments")
    port = int(argv[0])
    host = "localhost"
    keyFile = argv[1]
    with socket(AF_INET, SOCK_STREAM) as s:
        s.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            data = data.decode()
            data = data.strip()
            print(data)
            if(data != "HELLO"):
                conn.close()
                s.close()
                sys.exit("Didn't receive HELLO")
                # error and exit
            conn.sendall(b'260 OK')
            # add big while loop to get all inputs
            keyArray = createKeyArray(keyFile)
            data = conn.recv(1024)
            data = data.decode()
            data = data.strip()
            print(data)
            key = 0
            while(data != "QUIT"):
                if(data == "DATA"):
                    hash = hashlib.sha256()
                    data = conn.recv(1024)
                    data = stripMessage(data)
                    print(data.decode())
                    hash.update(data)
                    hash.update(keyArray[key].encode(encoding="ascii"))
                    conn.sendall(b'270 SIG')
                    conn.sendall(bytes(hash.hexdigest(),encoding="ascii"))
                    data = conn.recv(1024)
                    data = data.decode()
                    data = data.strip()
                    if(data != "PASS" and data != "FAIL"):
                        conn.close()
                        s.close()
                        sys.exit("Didn't receive PASS or FAIL")
                    print(data)
                    conn.sendall(b'260 OK')
                    data = conn.recv(1024)
                    data = data.decode()
                    data = data.strip()
                    print(data)
                    key += 1
                elif(data == "QUIT"):
                    conn.close()
        s.close()
    pass

if __name__ == "__main__":
    main()