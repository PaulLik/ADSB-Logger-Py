import socket
import time
from datetime import datetime

#msg1 = "MSG,5,0,2,155C1E,2,2023/11/04,17:10:42.195,2023/11/04,17:13:43.195,,35000,,,,,,,0,0,0,0"
#msg2 = "MSG,8,0,2,155C1E,2,2023/11/04,17:13:43.289,2023/11/04,17:13:43.289,,,,,,,,,0,0,0,0"

HOST = "127.0.0.1"
PORT = 30003

def setMessageTimeout(msg1, msg2, accelerator = 1):
    x1 = msg1.split(",")
    x2 = msg2.split(",")

    dt1 = x1[6] + " " + x1[7] + "000"
    dt2 = x2[6] + " " + x2[7] + "000"
    if dt1 != dt2:
        t1 = datetime.strptime(dt1, "%Y/%m/%d %H:%M:%S.%f")
        t2 = datetime.strptime(dt2, "%Y/%m/%d %H:%M:%S.%f")
        tdiff = datetime.strptime(str(t2 - t1), "%H:%M:%S.%f")
        m = int(tdiff.strftime("%M")) * 60
        s = int(tdiff.strftime("%S"))
        f = int(tdiff.strftime("%f")) / 1000000
        smt = (m + s+ f) / accelerator
    else:
        smt = 0
    return smt

def JobStart():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
        sck.bind((HOST, PORT))
        sck.listen()
        conn, addr = sck.accept()
        with conn:
            while True:
                f = open("logger_dump.txt", "r")
                prevLine = f.readline()
                for line in f:
                    time.sleep(setMessageTimeout(prevLine, line, 10))
                    print(line)
                    prevLine = line

    f.close()
    print("Complete")

if __name__ == "__main__":
    JobStart()