# write your code here
import sys
import socket
import itertools

def iterGen():
    cases = list(itertools.chain(range(ord('a'), ord('z') + 1), range(ord('0'), ord('9') + 1)))
    ans = [cases]
    while 1:
        yield ans
        ans.append(cases)

if __name__ == "__main__":
    hostname, port = sys.argv[1:]

    with socket.socket() as client_socket:
        address = (hostname, int(port))
        client_socket.connect(address)
        response = "Wrong password!"
        it = iterGen()
        while response != "Connection success!":
            nit = next(it)
            for p in itertools.product(*nit):
                psw = bytes(p)
                client_socket.send(psw)
                response = client_socket.recv(1024).decode()
                if response == "Connection success!":
                    break
    print(psw.decode())
