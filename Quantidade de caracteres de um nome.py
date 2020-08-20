def palavra(a):
    return len(a)

def main():
    a = str(input('Digite uma palavra: '))
    print(f'{palavra(a)}')

if __name__ == "__main__":
    main()