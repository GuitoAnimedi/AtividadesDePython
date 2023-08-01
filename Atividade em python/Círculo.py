import math

def calcular_area_circulo(raio):
    return math.pi * raio**2

def main():
    try:
        raio = float(input("Digite o raio do círculo: "))
        area = calcular_area_circulo(raio)
        print(f"A área do círculo com raio {raio} é: {area:.2f}")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
