a = int(input("Digite a Hora: "))
b = int(input("Digite os minutos: "))
c = int(input("Digite os segundos: "))

h = 24 - a
m = 60 - b
s = 60 - c

#transformando hora e minuto em segundos
h2 = h * 3600
m2 = m * 60

resultado = h2 + m2 + s

print(f"Se passaram {resultado} segundos desde a hora inserida {a}:{b}:{c}")