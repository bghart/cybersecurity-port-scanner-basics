import socket

target = input('Enter an IP or website: ')

ports = [21,22,23,80,443]

print(f'\nScanning {target}...\n')

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f'Port {port} is OPEN')
    else:
        print(f'Port {port} is ClOSED')


    s.close()