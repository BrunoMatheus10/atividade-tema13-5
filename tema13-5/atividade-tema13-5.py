# Solicita ao usuário que insira um RG para validação
rg = input("Digite o RG para validação (somente números): ")

# Inicializa variáveis de controle
valido = True  # Indica se o RG é válido
contador = 0  # Contador para o número de caracteres

# Percorre cada caractere do RG
for i in range(len(rg)):
    # Verifica se o caractere é um dígito
    if '0' <= rg[i] <= '9':
        contador += 1  # Incrementa o contador se o caractere for um dígito
    else:
        valido = False  # Se encontrar um caractere que não é dígito, marca como inválido

# Verifica se o RG tem entre 7 e 9 dígitos
if contador < 7 or contador > 9:
    valido = False  # Se o RG não tiver entre 7 e 9 dígitos, marca como inválido

# Verifica se todas as condições foram atendidas
if valido:
    print(rg," é um RG válido.")  # RG é válido
else:
    print(rg," é um RG inválido.")  # RG é inválido
