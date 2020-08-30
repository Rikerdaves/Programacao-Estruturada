def vogal_ou_consoante(letra):
    if letra in ('a', 'e', 'i', 'o', 'u'):
        return True
    elif letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        return False
    else:
        raise ValueError('Não é vogal nem consoante')

def main():
    letra = str(input('Digite uma lera: '))
    print(f'{vogal_ou_consoante(letra)}')

if __name__ == "__main__":
    main()        