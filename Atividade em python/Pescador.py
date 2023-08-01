def calcular_excesso_multa(peso_peixes):
    limite_peso = 50
    excesso = max(0, peso_peixes - limite_peso)
    multa_por_quilo = 4
    multa = excesso * multa_por_quilo
    return excesso, multa

def main():
    try:
        peso_peixes = float(input("Digite o peso de peixes (em quilos): "))

        excesso, multa = calcular_excesso_multa(peso_peixes)

        if excesso > 0:
            print(f"Você excedeu o limite de peso em {excesso:.2f} quilos.")
            print(f"O valor da multa a pagar é: R$ {multa:.2f}")
        else:
            print("Peso dentro do limite, nenhuma multa a pagar.")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
