def sexo(sex, name):
    if sex == 1:
        print(f'Ilmo Sr. {name}')
    else: 
        print(f'Ilma Sra. {name}')

def main():
        name = str(input())
        sex = int(input())
        return sexo(sex, name)   

if __name__ == "__main__":
    main()        

    
