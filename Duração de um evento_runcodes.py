def horas(num):
    horas = num // 3600

    resto = num % 3600

    minutos = resto // 60

    segundos = resto % 60

    return (f'{horas}:{minutos}:{segundos}')

def main():
    num = int(input())

    print(f'{horas(num)}')

if __name__ == "__main__":
    main()    


