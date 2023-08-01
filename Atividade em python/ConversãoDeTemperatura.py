def converter_fahrenheit_para_celsius(temp_fahrenheit):
    return 5 * ((temp_fahrenheit - 32) / 9)

def main():
    try:
        temp_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        temp_celsius = converter_fahrenheit_para_celsius(temp_fahrenheit)
        print(f"A temperatura em graus Celsius é: {temp_celsius:.2f} °C")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
