import sys
import time

numero = 12345

linhas = [
    "  ███  ",
    " █   █ ",
    " █   █ ",
    " █   █ ",
    "  ███  "
]

for linha in linhas:
    for d in str(numero):
        digito = int(d)
        print(linha.replace("█", str(digito)), end=" ")
        sys.stdout.flush()  # Limpar o buffer do stdout
        time.sleep(0.5)
    print()