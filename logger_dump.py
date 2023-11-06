import socket

server = "192.168.0.23"
port = 30003

print("Connecting...")
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((server, port))
    print("Connected!")
    while True:
        data = s.recv(4096)
        decData = data.decode("utf-8")
        msgPacket = decData.split("\r\n")
        for msg in msgPacket:
            if len(msg) > 1 and msg[:6] != "Server":
                f = open("c:\Dev\ADSB Logger Py\logger_dump.txt", "a")
                f.write(msg + "\n")
                print(msg)
                f.close