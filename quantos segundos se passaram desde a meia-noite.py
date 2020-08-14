a = int(input("Digite a Hora: "))
b = int(input("Digite os minutos: "))
c = int(input("Digite os segundos: "))

h = a * 3600 
m = b * 60
s = c


resultado = h + m + s

print(f"Se passaram {resultado} segundos desde a meia-noite")
