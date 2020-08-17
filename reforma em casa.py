def quest2_d():
  return

def main():
    altura = int(input("Digite a Altura: "))
    comprimento = int(input("Digite o comprimento: "))
    largura = int(input("Digite a largura: "))

    area_piso_sala = altura * largura

    volume_sala = largura * comprimento * altura

    area_paredes = 2 * altura * largura + 2 * altura * comprimento 


    print(f'Área do piso da sala: {area_piso_sala} metros quadrados\n'
          f'Volume da sala: {volume_sala} metros cubicos\n'
          f'Área das paredes da sala: {area_paredes} metros quadrados')

if __name__ == '__main__':
  main()    

