#!/usr/bin/python

"""

a = 0 
while a >= 0:
 a = int(input("Ingrese los Kilometros recorridos: "))
 if a >= 0:
  b = int(input("cuantos litros de gazolina usò: "))
  print("Estimado conductor usted a usado, 1 litros de combustible cada", a / b, "kilometro recorrido")

print("Gracias por usar este programa. Adios")

"""

"""

a = 0
while a >= 0:
 a = int(input("numero de cuenta del cliente: -1 para salir   "))
 if a >= 0:
  saldo_inicial = float(input("ingrese el saldo del cliente: "))
  articulos = int(input("escriba el total de los  articulos  del cliente: "))
  tcredito = int(input("total del credito del cliente: "))
  lim = float(input("escriba el limite del credito: ")) 
  saldo = saldo_inicial + articulos - tcredito
  if saldo > lim:
   print("el cliente", a, "tiene un limite de credito de:", lim, "y su nuevo saldo es:", saldo, "exedio el limite del credito")
  else:
   print("el nuevo slado es:", saldo)

"""

"""

a = 0
while a >= 0:
 a = float(input("ingrese el total del monto que vendio: preciones -1 para salir"))
 if a >= 0:
  b = a * 9 / 100
  c = 200
  print("el salario de su semana es de:", c, "+", "el 9% de:", a, "el total a cobrar es de:", c + b)
 else:
  print("adios")

"""

"""

a = 0
while a >= 0:
 a = float(input("Ingrese la cantidad de horas trabajadas: (-1 para salir)"))
 if a >= 0:
  b = float(input("Ingrese el precio en dolares de la hora: "))
  if a <= 40:
   print("su salario bruto es:", a * b)
  else:
   print(" su salario bruto es:", a * b + b * 0.5)
 else:
  print("adios")

"""

"""

contador = 1
busca = []
while contador <= 10:
 num = int(input("Ingrese un número::  "))
 busca.append(num)
 print(contador)
 contador += 1
busca.sort()
mayor = busca[9]
print("el número mayor que introducistes es:", mayor)

"""
