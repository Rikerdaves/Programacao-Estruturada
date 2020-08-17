def quest2_d():
  return

def main():
  hora = int(input())
  minutos = int(input())
  segundos = int(input())

  h = hora * 3600 
  m = minutos * 60
  s = segundos

  resultado = h + m + s

  print(f"{resultado}")

if __name__ == '__main__':
  main()
