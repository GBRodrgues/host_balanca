import socket
import sqlite3
from datetime import datetime

# Configurações
HOST = '0.0.0.0'
PORT = 5000

# Cria o banco de dados
def criar_banco():
    conn = sqlite3.connect('balanca.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            peso REAL,
            data_hora TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Salva a leitura no banco
def salvar_leitura(peso):
    conn = sqlite3.connect('balanca.db')
    cursor = conn.cursor()
    
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO leituras (peso, data_hora) VALUES (?, ?)', (peso, data_hora))
    
    conn.commit()
    conn.close()
    print(f"Salvo no banco: {peso} kg - {data_hora}")

# Inicia o servidor
def iniciar_servidor():
    criar_banco()
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    
    print(f"Servidor rodando em {HOST}:{PORT}")
    print("Aguardando conexões...\n")
    
    while True:
        conexao, endereco = servidor.accept()
        print(f"Conectado: {endereco}")
        
        dados = conexao.recv(1024).decode('utf-8')
        
        if dados:
            try:
                peso = float(dados.strip())
                print(f"Peso recebido: {peso} kg")
                
                salvar_leitura(peso)
                
                conexao.send("OK".encode('utf-8'))
            except:
                print("Erro ao processar dados")
        
        conexao.close()

if __name__ == "__main__":
    iniciar_servidor()

