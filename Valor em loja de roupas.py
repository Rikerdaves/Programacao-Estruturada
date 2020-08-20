def valor(preco):
    valor_com_desconto = preco * 0.09

    valor_final = preco - valor_com_desconto

    parcela1 = preco / 5

    parcela2 = preco * (1 + 0.17) / 10

    return  (f'Valor com Desconto de 9% R${valor_final:.2f}\n'
    f'Valor parcelado 5x sem juros R${parcela1:.2f}\n'
    f'Valor parcelado 10x e 17% de juros R${parcela2:.2f}')

def main():
    preco = float(input("Digite o Valor da Roupa: R$ "))

    print(f'{valor(preco)}')  


if __name__ == "__main__":
    main()    