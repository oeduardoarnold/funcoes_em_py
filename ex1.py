def eprimo(numero):
  for i in range(2, numero-1):
      # se o resto da divisão for zero, ele não é primo
      if numero % i == 0:
        # se ele for divisivel por qualquer um numero, retorna falso
        return False
  return True

print("Digite o intervalo para encontrar numeros primo")

while True:
  min = int(input("Min:"))
  if min >1:
    break
  print("Min precisa ser maior do que 1:")

max = int(input("Max:"))
primos = []

# itera entre o range de numeros
for numero in range(min, max+1):
  # testa se o numero é primo
  if eprimo(numero):
    # se é primo, adiciona na lista
    primos.append(numero)

# imprime todos os primos adionados
for primo in primos:
  print(primo)