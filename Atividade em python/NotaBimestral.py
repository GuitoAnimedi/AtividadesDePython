def calcular_media(notas):
    
    if None in notas:
        return None
    
    
    media = sum(notas) / len(notas)
    return media

def main():
    print("Digite as 4 notas bimestrais:")
    notas = []
    
    
    for i in range(4):
        while True:
            try:
                nota = float(input(f"Nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Digite uma nota válida (entre 0 e 10).")
            except ValueError:
                print("Digite uma nota válida (número).")
    
    
    media = calcular_media(notas)
    if media is not None:
        print(f"A média das notas é: {media:.2f}")
    else:
        print("Erro: Alguma nota não foi informada corretamente.")

if __name__ == "__main__":
    main()
