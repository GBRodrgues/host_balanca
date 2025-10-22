import sqlite3

conn = sqlite3.connect('balanca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM leituras ORDER BY id DESC LIMIT 20')
resultados = cursor.fetchall()

print("\n=== LEITURAS DA BALANÇA ===\n")
print(f"{'ID':<5} {'Peso (kg)':<12} {'Data/Hora':<20}")
print("-" * 40)

for row in resultados:
    id_leitura, peso, data_hora = row
    print(f"{id_leitura:<5} {peso:<12.2f} {data_hora:<20}")

print("\n")

# Estatísticas
cursor.execute('SELECT COUNT(*), AVG(peso), MIN(peso), MAX(peso) FROM leituras')
total, media, minimo, maximo = cursor.fetchone()

print("=== ESTATÍSTICAS ===")
print(f"Total de leituras: {total}")
if media:
    print(f"Peso médio: {media:.2f} kg")
    print(f"Peso mínimo: {minimo:.2f} kg")
    print(f"Peso máximo: {maximo:.2f} kg")

conn.close()

