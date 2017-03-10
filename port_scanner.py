import socket, time, fire

class PortScanner:
    HOST = ''  # accepts all hosts
    NUM = 0

    def __init__(self, host, num):
        self.HOST = host
        self.NUM = num

    def scan_open_ports(self):
        """Creates new socket each time with a a new
            port number from a user given range
        """
        for PORT in range(NUM):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((HOST, PORT)) # This checks if port is open
                print(str(PORT) + " open") # prints the open sockets
            except Exception:
                print('This port is closed: %s' % PORT)

if __name__ == '__main__':
    HOST = input('Host name: ')
    NUM = int(input('Port range: '))
    t1 = time.time()  # initial time
    
    port_scan = PortScanner(HOST, NUM)
    fire.Fire(port_scan.scan_open_ports())
    t2 = time.time()  # finish time

    # computes and displays the total time taken to scan all the port within the given range
    print('It takes this long to complete: ', str(t2-t1) + ' seconds')
