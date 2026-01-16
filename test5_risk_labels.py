import socket

target = input('Enter an IP or website: ')

ports = {
    21: "FTP (INSECURE)",
    22: "SSH",
    23: "Telnet (INSECURE)",
    80: "HTTP",
    443: "HTTPS"
}

print(f'\nScanning {target}...\n')

for port, service in ports.items():
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        if 'Insecure' in service:
            print(f'[WARNING] Port {port} OPEN - {service}')
        else:
            print(f'[OK] Port {port} OPEN - {service}')
    else:
        print(f'Port {port} CLOSED')

    s.close()

