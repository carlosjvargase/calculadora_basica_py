'''
MEJORA!
Realizar un sistema de calculadora con las operaciones básicas: +, -, *, /.
El sistema debe ser cíclico hasta el usuario decida salir.
'''
def sumar(num_1, num_2):
  return num_1 + num_2

def restar(num_1, num_2):
  return num_1 - num_2

def multi(num_1, num_2):
  return num_1 * num_2

def divid(num_1, num_2):
  return num_1/num_2 if num_2 != 0 else 'No se puede dividir por Cero.'  
  
def menu():
  print('''
### Menú ###
1. Suma
2. Resta
3. Multiplicar
4. Dividir
5. Salir
  ''')
  return input('Ingrese una opción válida: ')
def pedir():
  num1 = float(input('Ingrese el primer número: '))
  num2 = float(input('Ingrese el segundo número: '))
  return num1, num2

while True:
  opc = menu()
  if opc == '1':
    numeros = pedir()
    print(f'El resultado de la suma es: {sumar(numeros[0], numeros[1])}')
  elif opc == '2':
    numeros = pedir()
    print(f'El resultado de la resta es: {restar(numeros[0], numeros[1])}')
  elif opc == '3':
    numeros = pedir()
    print(f'El resultado de la multiplicación es: {multi(numeros[0], numeros[1])}')
  elif opc == '4':
    numeros = pedir()
    print(f'El resultado de la división es: {divid(numeros[0], numeros[1])}')
  elif opc == '5':
    print('Gracias por usar nuestra Calculadora.')
    break
  else:
    print('Opción no válida. Vuela a intentarlo!')