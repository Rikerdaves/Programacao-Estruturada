def sinal(cor):
    if cor == 'V':
        return print('Siga')
    elif cor == 'A':
        return print('Atenção')
    else:
        return print('Pare')
   
def main():
    print('"V" - verde\n' 
    '"A"  - amarelo\n' 
    '"E" - vermelho')
    cor = str(input('Digite uma letra: '))
    return sinal(cor)

if __name__ == "__main__":
    main()    

    
