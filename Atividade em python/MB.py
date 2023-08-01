def calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps):
    # Converter o tamanho do arquivo para megabits (1 byte = 8 bits).
    tamanho_arquivo_mbps = tamanho_arquivo_mb * 8

    # Calcular o tempo em segundos (tamanho em megabits dividido pela velocidade em megabits por segundo).
    tempo_segundos = tamanho_arquivo_mbps / velocidade_internet_mbps

    # Converter o tempo para minutos.
    tempo_minutos = tempo_segundos / 60
    return tempo_minutos

def main():
    try:
        tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
        velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

        tempo_download_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps)

        print(f"Tempo aproximado de download: {tempo_download_minutos:.2f} minutos")
    except ValueError:
        print("Digite valores válidos (números).")

if __name__ == "__main__":
    main()
