import socket

target_ip = "192.168.1.95"
ports_to_scan = [21, 22, 80, 443, 8080]

print(f"[*] Starting port scan on {target_ip}...")

for port in ports_to_scan:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection attempt

    #Try to connect to the target IP and port
    result = sock.connect_ex((target_ip, port))

    if result == 0:
        print(f"[+] Port {port}: OPEN(Service detected!)")
    else:
        print(f"[-] Port {port}: CLOSED")

    sock.close()

print("[*] Port scan completed.")