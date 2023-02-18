#lista de morosos por cedula
lmorosos = [ 1111,2222,3333,4444,5555,6666,7777,8888,9999,1010,2020,3030,4040,5050,6060,7070,8080,9090,2121,3131]

cedula = int(input("ingrese el numero de cedula: "))
if cedula in lmorosos:
    print("El usuario no es apto para el prestamo ya que se encuentra reportado como moroso.")
else:
    print("El usuario si es apto para el prestamo, no esta reportado.")


             
