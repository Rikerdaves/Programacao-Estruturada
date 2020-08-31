def nota(n1, n2, n3):
    if n3 > 8:
        media = ((n1 + n2 + n3)/3) + 1
    else:
        media = (n1 + n2 + n3)/3  
          
    if media > 10.0:
        media = 10                  
    return media    

def main():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    
    resultado = nota(n1, n2, n3)

    print (f'{resultado:.2f}')

if __name__ == "__main__":
    main()   

