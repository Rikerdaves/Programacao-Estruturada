def sinal(cor):
    if cor.upper() == "V":
        return f'Siga'
    elif cor.upper() == "A":
        return f'Atenção'
    elif cor.upper() == "E": 
        return f'Pare'
   
def main():
    cor = str(input())
    fazer = sinal(cor)
    print(fazer)

if __name__ == "__main__":
    main()    

    

    
