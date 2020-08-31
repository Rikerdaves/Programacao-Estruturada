def vogal_ou_consoante(letra):
    if letra in 'a e i o u':
        return f'vogal'
    if letra in 'b c d f g h j k l m n p q r s t v w x y z':
        return f'consoante'
    elif float(letra):
        return  f'numero'
    else:
        return f'simbolo'      

def main():
    letra = str(input('Digite um caractere: '))
    print(f'{vogal_ou_consoante(letra)}')

if __name__ == "__main__":
    main()            