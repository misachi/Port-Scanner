import socket, time

HOST = ''
NUM = 0

if __name__ == '__main__':
    t1 = time.time()
    HOST = input('Host name: ')
    NUM = int(input('Port range: '))

    """Creates new socket each time with a a new
        port number from a user given range
    """
    for PORT in range(NUM):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT)) # This checks if port is open
            print(PORT) # prints the open sockets
        except Exception:
            print('This port is closed: %s' % PORT)
    t2 = time.time()
    print('It takes this long to complete: ', str(t2-t1) + ' seconds')
