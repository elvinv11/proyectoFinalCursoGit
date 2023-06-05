# aquí tambien para probarlo se debe usar python3 ejersicio3.py

a = 0
while a >= 0:
 a = float(input("ingrese el total del monto que vendio: preciones -1 para salir"))
 if a >= 0:
  b = a * 9 / 100
  c = 200
  print("el salario de su semana es de:", c, "+", "el 9% de:", a, "el total a cobrar es de:", c + b)
 else:
  print("adios")



