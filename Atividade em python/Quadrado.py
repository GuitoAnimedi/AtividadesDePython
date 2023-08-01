def calcular_area_quadrado(lado):
    return lado ** 2

def main():
    try:
        lado = float(input("Digite o valor do lado do quadrado: "))
        area = calcular_area_quadrado(lado)
        dobro_area = area * 2
        print(f"A área do quadrado é: {area:.2f}")
        print(f"O dobro da área do quadrado é: {dobro_area:.2f}")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
