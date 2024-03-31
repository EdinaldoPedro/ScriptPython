def calcular_fatorial(x):
    if x == 0:
        return 1
    else:
        fatorial = 1
        contador = 1
        while contador <= x:
            fatorial *= contador
            contador += 1
        return fatorial
    
def binomial (n, p):
    return calcular_fatorial(n) / (calcular_fatorial(p) * (calcular_fatorial(n - p)))


# Exemplo de uso da função para calcular o binomial aplicando a relação de Stifel
n = int(input("Digite um número N que deseja o binomial: "))
p = int(input("Digite um número P que deseja o binomial: "))

if p > n :
    print("Invalido, o 'N' não pode ser  maior que o 'P'")
else:
    resultado = binomial(n, p)

    print(f'O binomial é {resultado}')
