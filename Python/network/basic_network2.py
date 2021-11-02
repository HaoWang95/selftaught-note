from os import error
import socket
import argparse
import sys

def test_socket_timeout():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'Default socket timeout: {my_socket.gettimeout()}')
    my_socket.settimeout(100)
    print(f'Current socket timeout: {my_socket.gettimeout()}')


def use_socket():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket examples')
    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', action='store', dest='port', type=int, required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)

    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Err at creating socket -> {e}')
        sys.exit(1)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(f'Address related error connecting to server -> {e}')
        sys.exit(1)
    except socket.error as e:
        print(f'Connection err -> {e}')
        sys.exit(1)
    
    try:
        msg = f'GET {filename} HTTP/1.0\r\n\r\n'
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print(f'Error sending data -> {e}')

    while 1:
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print(f'Error at receiving data -> {e}')
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf.decode('utf-8'))    

if __name__ == '__main__':
    #test_socket_timeout()
    use_socket()