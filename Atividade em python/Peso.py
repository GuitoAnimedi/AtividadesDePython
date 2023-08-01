def calcular_peso_ideal(altura):
    return (72.7 * altura) - 58

def main():
    try:
        altura = float(input("Digite a altura da pessoa (em metros): "))
        peso_ideal = calcular_peso_ideal(altura)
        print(f"O peso ideal para uma pessoa com altura {altura} metros é: {peso_ideal:.2f} kg")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
