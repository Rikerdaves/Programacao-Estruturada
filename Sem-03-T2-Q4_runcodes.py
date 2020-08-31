def numero_ou_letra(letra):
    if letra.lower() in 'a e i o u b c d f g h j k l m n p q r s t v w x y z':
        return True
    elif letra in '0 1 2 3 4 5 6 7 8 9': 
        return True
    else:
        return False 

def main():
    letra = str(input())
    print(f'{numero_ou_letra(letra)}')

if __name__ == "__main__":
    main()  