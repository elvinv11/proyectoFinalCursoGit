
# este es el ejersicio 2 no le pondre la linea que da el ejecutable
# para probarlo usar el comando python3 ejersicio2.py


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



