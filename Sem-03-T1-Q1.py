def sexo(sex, name):
    if sex == 1:
        return print(f'Ilmo Sr. {name}')
    elif sex == 2:
        return print(f'Ilma Sr. {name}')

def main():
        print('Sexo:\n'
        '1 - Masculino\n'
        '2 - Feminino')
        name = str(input("Digite seu nome: "))
        sex = int(input("Qual seu sexo: "))
        return sexo(sex, name)   

if __name__ == "__main__":
    main()        

    
