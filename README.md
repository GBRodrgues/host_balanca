# Balança Inteligente - TCC

Sistema simples para receber dados de peso via socket e salvar no banco de dados.

## Arquivos

- `servidor.py` - Servidor que recebe os dados
- `codigo_esp.ino` - Código para o ESP8266
- `ver_dados.py` - Visualiza os dados salvos
- `testar.py` - Testa o servidor

## Como usar

### 1. Iniciar o servidor

```bash
python3 servidor.py
```

### 2. Testar (opcional)

Em outro terminal:

```bash
python3 testar.py
```

### 3. Ver os dados

```bash
python3 ver_dados.py
```

### 4. Configurar o ESP

1. Abra `codigo_esp.ino` no Arduino IDE
2. Instale a biblioteca HX711
3. Altere o WiFi e o IP do servidor
4. Carregue no ESP

## Conexões do Hardware

**HX711 → ESP:**
- DOUT (D0/RX) → RX0
- SCK (CK/TX) → D4

**Célula de Carga → HX711:**
- Vermelho → A+
- Preto → B+ e GND (com resistor 1k)
- Branco → B- e GND (com resistor 1k)

## Banco de Dados

O arquivo `balanca.db` é criado automaticamente com a tabela:

```sql
leituras (
    id INTEGER,
    peso REAL,
    data_hora TEXT
)
```

