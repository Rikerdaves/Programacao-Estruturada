def par(num):
    if num % 2 == 0:
        return False
    else:
        return True

def main():
    num = int(input())
    print(f'{par(num)}')

if __name__ == "__main__":
    main()    

       