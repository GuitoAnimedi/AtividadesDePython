def calcular_salario_bruto(valor_hora, horas_trabalhadas):
    return valor_hora * horas_trabalhadas

def main():
    try:
        valor_hora = float(input("Digite o valor que você ganha por hora: "))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

        salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas)
        print(f"Seu salário bruto no mês é: R$ {salario_bruto:.2f}")
    except ValueError:
        print("Digite valores válidos (números).")

if __name__ == "__main__":
    main()
