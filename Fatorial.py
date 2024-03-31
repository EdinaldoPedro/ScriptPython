def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        fatorial = 1
        contador = 1
        while contador <= n:
            fatorial *= contador
            contador += 1
        return fatorial

# Exemplo de uso da função para calcular o fatorial de um número
numero = int(input("Digite um número que deseja o fatorial: "))

resultado = calcular_fatorial(numero)

print(f'O fatorial de {numero} é {resultado}')
