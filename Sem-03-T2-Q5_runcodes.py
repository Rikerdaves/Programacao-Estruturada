def vogal_ou_consoante(letra):
    if letra.lower() in 'a e i o u':
        return f'vogal'
    elif letra.lower() in 'b c d f g h j k l m n p q r s t v w x y z':
        return f'consoante'
    if letra in ('0 1 2 3 4 5 6 7 8 9'):
        return  f'numero'
    else:
        return f'simbolo'     

def main():
    letra = input()
    print(f'{vogal_ou_consoante(letra)}')

if __name__ == "__main__":
    main()            