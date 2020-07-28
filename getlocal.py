import socket

def main():
    # Get local IP address.
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)


if __name__ == "__main__":
    main()
