def numero_ou_letra(letra):
    if letra in ('0' '1' '2' '3' '4' '5' '6' '7' '8' '9'):
        return True
    elif letra in ('a', 'e', 'i', 'o', 'u','b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        return False
    else:
        raise ValueError('Não é vogal nem consoante')

def main():
    letra = str(input("Digite uma Letra ou numero: "))
    print(f'{numero_ou_letra(letra)}')

if __name__ == "__main__":
    main()  