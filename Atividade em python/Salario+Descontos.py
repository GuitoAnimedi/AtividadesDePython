def calcular_salario_bruto(valor_hora, horas_trabalhadas):
    return valor_hora * horas_trabalhadas

def calcular_desconto_imposto_renda(salario_bruto):
    return salario_bruto * 0.11

def calcular_desconto_inss(salario_bruto):
    return salario_bruto * 0.08

def calcular_desconto_sindicato(salario_bruto):
    return salario_bruto * 0.05

def calcular_salario_liquido(salario_bruto, desconto_ir, desconto_inss, desconto_sindicato):
    return salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

def main():
    try:
        valor_hora = float(input("Digite o valor que você ganha por hora: "))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

        salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas)
        desconto_ir = calcular_desconto_imposto_renda(salario_bruto)
        desconto_inss = calcular_desconto_inss(salario_bruto)
        desconto_sindicato = calcular_desconto_sindicato(salario_bruto)
        salario_liquido = calcular_salario_liquido(salario_bruto, desconto_ir, desconto_inss, desconto_sindicato)

        print(f"Salário Bruto: R$ {salario_bruto:.2f}")
        print(f"Desconto IR (11%): R$ {desconto_ir:.2f}")
        print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
        print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    except ValueError:
        print("Digite valores válidos (números).")

if __name__ == "__main__":
    main()
