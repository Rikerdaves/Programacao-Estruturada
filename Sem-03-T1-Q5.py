def nota(n1, n2, n3):
    media = (n1 + n2 + n3)//3
    if n2 > 8:
        media + 1
    elif media > 10:
        media = 10
    return print (f'{media}')    

def main():
    n1 = int(input("Digite a nota 1: "))
    n2 = int(input('Digite a nota 2: '))
    n3 = int(input('Digite a nota 2: '))
    return nota(n1, n2, n3)

if __name__ == "__main__":
    main()   

