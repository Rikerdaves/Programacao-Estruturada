def digito(num):
    if num >= 0 and num <= 9:
        return True
    else:
        return False


def main():
    num = float(input('Digite um número de 0 a 9: '))
    print (f'{digito(num)}')

if __name__ == "__main__":
    main() 