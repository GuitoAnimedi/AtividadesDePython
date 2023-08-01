def calcular_peso_ideal_homem(altura):
    return (72.7 * altura) - 58

def calcular_peso_ideal_mulher(altura):
    return (62.1 * altura) - 44.7

def main():
    try:
        altura = float(input("Digite a altura da pessoa (em metros): "))
        genero = input("Digite 'h' para homem ou 'm' para mulher: ")

        if genero.lower() == 'h':
            peso_ideal = calcular_peso_ideal_homem(altura)
        elif genero.lower() == 'm':
            peso_ideal = calcular_peso_ideal_mulher(altura)
        else:
            print("Opção inválida. Digite 'h' para homem ou 'm' para mulher.")
            return

        print(f"O peso ideal para uma pessoa com altura {altura} metros é: {peso_ideal:.2f} kg")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
