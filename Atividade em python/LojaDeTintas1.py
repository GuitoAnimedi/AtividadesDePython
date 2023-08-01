import math

def calcular_quantidade_latas(area):
    # Cada lata tem 18 litros e cobre 3 metros quadrados por litro.
    litros_necessarios = math.ceil(area / 3)
    latas_necessarias = math.ceil(litros_necessarios / 18)
    return latas_necessarias

def calcular_preco_total(latas_necessarias):
    preco_por_lata = 80.00
    return latas_necessarias * preco_por_lata

def main():
    try:
        area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

        latas_necessarias = calcular_quantidade_latas(area_a_ser_pintada)
        preco_total = calcular_preco_total(latas_necessarias)

        print(f"Quantidade de latas de tinta a serem compradas: {latas_necessarias}")
        print(f"Preço total da compra: R$ {preco_total:.2f}")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
