import math

def calcular_area_circulo(raio):
    area = math.pi * raio ** 2
    return area

def main():
    raio = float(input("Digite o valor do raio da circunferência: "))
    area = calcular_area_circulo(raio)
    print(f"A área da circunferência é: {area:.2f}")

if __name__ == "__main__":
    main()
