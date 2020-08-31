def vogal_ou_consoante(letra):
    if letra.lower() in 'a e i o u b c d f g h j k l m n p q r s t v x z w y':
        return True
    else:
        return False

def main():
    letra = str(input())
    print(f'{vogal_ou_consoante(letra)}')

if __name__ == "__main__":
    main()       