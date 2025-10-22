import socket

HOST = 'localhost'
PORT = 5000

# Simula envio de peso
peso = 1.5

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

print(f"Enviando peso: {peso} kg")
cliente.send(str(peso).encode('utf-8'))

resposta = cliente.recv(1024).decode('utf-8')
print(f"Resposta: {resposta}")

cliente.close()

