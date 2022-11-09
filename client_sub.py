import socket
import sys
import select
import errno
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

broker_address = ('localhost', 10000)
port = 10001
messageA = b'sub:id:%i'%port
messageB = b'sub:topic:game'

try:
    # Send data
    print('sending {!r}'.format(messageA))
    sent = sock.sendto(messageA, broker_address)
    print('sending {!r}'.format(messageB))
    sent = sock.sendto(messageB, broker_address)
finally:
    print('closing socket')
    sock.close()

# Bind the socket to the port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', port)
# A partir de aquí lo nuevo
while True:
    try:
        sock.bind(server_address) # Se intenta conectar
        # Si ha ido bien, imprime la dirección y puerto
        print('starting up on {} port {}'.format(*server_address))
        break # Sale del bucle
    except socket.error as e:
        # Si hay un error de dirección en uso
        if e.errno == errno.EADDRINUSE:
            print("Connection failed. Port %i is already in use."%port)
            port += 1 # Se incrementa el puerto en 1
            print("Connecting to port %i"%port)
            server_address = ('localhost', port) # Se actualiza la dirección
        
while True:
    print('\nwaiting to receive message')
    rlist, _, _ = select.select([sock], [], []) 
    data, address = sock.recvfrom(1024)
    # Do stuff with data, fill this up with your code
    print('received {} bytes from {}'.format(len(data), address))
    print(data)


