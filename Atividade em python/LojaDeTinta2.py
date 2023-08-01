import math

def calcular_quantidade_latas(area):
    # Cada lata tem 18 litros e cobre 6 metros quadrados por litro.
    litros_necessarios = area / 6
    latas_necessarias = math.ceil(litros_necessarios / 18)
    return latas_necessarias

def calcular_quantidade_galoes(area):
    # Cada galão tem 3,6 litros e cobre 6 metros quadrados por litro.
    litros_necessarios = area / 6
    galoes_necessarios = math.ceil(litros_necessarios / 3.6)
    return galoes_necessarios

def calcular_mistura_latas_galoes(area):
    # Cada lata tem 18 litros e cada galão tem 3,6 litros.
    # Considerando que o desperdício seja reduzido, vamos calcular a melhor combinação possível.
    litros_necessarios = area / 6
    latas_necessarias = int(litros_necessarios / 18)
    litros_restantes = litros_necessarios - latas_necessarias * 18
    galoes_necessarios = math.ceil(litros_restantes / 3.6)
    return latas_necessarias, galoes_necessarios

def calcular_preco_latas(latas_necessarias):
    preco_por_lata = 80.00
    return latas_necessarias * preco_por_lata

def calcular_preco_galoes(galoes_necessarios):
    preco_por_galao = 25.00
    return galoes_necessarios * preco_por_galao

def calcular_preco_mistura(latas_necessarias, galoes_necessarios):
    preco_por_lata = 80.00
    preco_por_galao = 25.00
    return (latas_necessarias * preco_por_lata) + (galoes_necessarios * preco_por_galao)

def main():
    try:
        area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

        latas_necessarias = calcular_quantidade_latas(area_a_ser_pintada)
        preco_latas = calcular_preco_latas(latas_necessarias)

        galoes_necessarios = calcular_quantidade_galoes(area_a_ser_pintada)
        preco_galoes = calcular_preco_galoes(galoes_necessarios)

        latas_mistura, galoes_mistura = calcular_mistura_latas_galoes(area_a_ser_pintada)
        preco_mistura = calcular_preco_mistura(latas_mistura, galoes_mistura)

        print(f"Quantidade de latas de tinta a serem compradas: {latas_necessarias}")
        print(f"Preço total das latas: R$ {preco_latas:.2f}")

        print(f"Quantidade de galões de tinta a serem comprados: {galoes_necessarios}")
        print(f"Preço total dos galões: R$ {preco_galoes:.2f}")

        print(f"Quantidade de latas de tinta na mistura: {latas_mistura}")
        print(f"Quantidade de galões de tinta na mistura: {galoes_mistura}")
        print(f"Preço total da mistura: R$ {preco_mistura:.2f}")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
