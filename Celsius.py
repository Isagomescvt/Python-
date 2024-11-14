def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def main():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f} ºF")

if __name__ == "__main__":
    main()
def calcular_total_segundos(dias, horas, minutos, segundos):
    total_segundos = segundos + minutos * 60 + horas * 3600 + dias * 86400
    return total_segundos

def main():
    dias = int(input("Digite a quantidade de dias: "))
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    segundos = int(input("Digite a quantidade de segundos: "))
    
    total_segundos = calcular_total_segundos(dias, horas, minutos, segundos)
    print(f"O total de tempo em segundos é: {total_segundos} segundos")

if __name__ == "__main__":
    main()
