def maximo(num1, num2, num3, num4, num5):
    return max(num1, num2, num3, num4, num5)

def minimo(num1, num2, num3, num4, num5):
    return min(num1, num2, num3, num4, num5)

def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    media = (num1 + num2 + num3 + num4 + num5) / 5

    print(f'{maximo(num1, num2, num3, num4, num5)}')
    print(f'{minimo(num1, num2, num3, num4, num5)}')
    print(f'{media}')

if __name__ == "__main__":
    main()    

