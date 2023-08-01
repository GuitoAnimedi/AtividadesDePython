def calcular_produto_dobro_metade(num1, num2):
    return (2 * num1) * (num2 / 2)

def calcular_soma_triplo_terceiro(num1, num3):
    return (3 * num1) + num3

def calcular_terceiro_elevado_cubo(num3):
    return num3 ** 3

def main():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        num3 = float(input("Digite o número real: "))

        produto_dobro_metade = calcular_produto_dobro_metade(num1, num2)
        soma_triplo_terceiro = calcular_soma_triplo_terceiro(num1, num3)
        terceiro_elevado_cubo = calcular_terceiro_elevado_cubo(num3)

        print(f"Produto do dobro do primeiro com metade do segundo: {produto_dobro_metade}")
        print(f"Soma do triplo do primeiro com o terceiro: {soma_triplo_terceiro}")
        print(f"Terceiro elevado ao cubo: {terceiro_elevado_cubo}")
    except ValueError:
        print("Digite valores válidos.")

if __name__ == "__main__":
    main()
