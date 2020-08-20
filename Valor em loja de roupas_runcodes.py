def valor(preco):
    valor_com_desconto = preco * 0.09

    valor_final = preco - valor_com_desconto

    parcela1 = preco / 5

    parcela2 = preco * (1 + 0.17) / 10

    return  (f'{valor_final:.2f}\n'
    f'{parcela1:.2f}\n'
    f'{parcela2:.2f}')

def main():
    preco = float(input())

    print(f'{valor(preco)}')  


if __name__ == "__main__":
    main()  