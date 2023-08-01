def converter_celsius_para_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

def main():
    try:
        temp_celsius = float(input("Digite a temperatura em graus Celsius: "))
        temp_fahrenheit = converter_celsius_para_fahrenheit(temp_celsius)
        print(f"A temperatura em graus Fahrenheit é: {temp_fahrenheit:.2f} °F")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
