def metros_para_centimetros(metros):
    return metros * 100

def main():
    try:
        metros = float(input("Digite o valor em metros: "))
        centimetros = metros_para_centimetros(metros)
        print(f"{metros} metros equivalem a {centimetros} centímetros.")
    except ValueError:
        print("Digite um valor válido (número).")

if __name__ == "__main__":
    main()
