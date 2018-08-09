import socket


def main(host='0.0.0.0', port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size
        print("connection from: %s", addr)

        sock.sendto(b"Hello", addr)


if __name__ == '__main__':
    main()
