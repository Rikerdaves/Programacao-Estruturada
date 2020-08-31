def consoante(letra):
    if letra.lower() in 'b c d f g h j k l m n p q r s t v w x y z':
        return True
    else:
        return False

def main():
    letra = str(input())
    print(f'{consoante(letra)}')

if __name__ == "__main__":
    main()    
