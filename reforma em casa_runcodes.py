altura = int(input())
comprimento = int(input())
largura = int(input())

area_do_piso_da_sala = largura * comprimento

volume_da_sala = largura * comprimento * altura

area_das_paredes_da_sala = 2 * altura * largura + 2 * altura * comprimento 

print(f'{area_do_piso_da_sala}')
print(f'{volume_da_sala}')    
print(f'{area_das_paredes_da_sala}')   