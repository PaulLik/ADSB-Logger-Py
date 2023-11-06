import socket
from win32com.client import Dispatch
import logger_db

#logger_db.loadAirports()
#for a in logger_db.airports:
    #print(a)

server = "127.0.0.1"
port = 30003

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((server, port))
    while True:
        data = s.recv(4096)
        decData = data.decode("utf-8")
        msgPacket = decData.split("\r\n")
        for msg in msgPacket:
            if len(msg) > 1 and msg[:6] != "Server":
                print(msg)
                msgValues = msg.split(",")
                if len(msgValues) > 4:
                    afHex = msgValues[4]
                    airframe = logger_db.findAircraft(afHex)
                    if msg[:2] == "ID":
                        speak = Dispatch("SAPI.SpVoice").Speak
                        speak("ID " + airframe)
                    if msg[:3] == "AIR":
                        speak = Dispatch("SAPI.SpVoice").Speak
                        speak("Air " + airframe)