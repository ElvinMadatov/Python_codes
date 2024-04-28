import socket

def check_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        s.close()
    except Exception as e:
        print("Error:", e)

ip_address = input("IP address: ")
port_to_check = int(input("Port: "))

check_port(ip_address, port_to_check)
