numero = 12345

linhas = [
    ["███", "█ █", "█ █", "█ █", "███"],  # Representação visual do dígito 0
    ["  █", "  █", "  █", "  █", "  █"],  # Representação visual do dígito 1
    # Adicione as representações visuais dos dígitos 2 a 9 aqui
]

for linha in range(5):
    for d in str(numero):
        digito = int(d)
        print(linhas[digito][linha], end=" ")
    print()