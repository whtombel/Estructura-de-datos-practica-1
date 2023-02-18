codigo =["001","002","003","004","005","006"]

nombres=["luiz dominguez", "daniela florez", "jesus bastidas", "camilo chaves", "diana chaves", "jackeline riascos"]

nota= [4.5 , 3.8 , 2.5 , 4.8, 4.6 , 4.2 ]

codigoest = input("ingrese el codigo del estudiante que desea consultar la nota: ")


if codigoest in codigo:
    #encuentra la posicion
    posicion = codigo.index(codigoest)
    nomest= nombres[posicion]
    notaest= nota[posicion]           
                              
    print("codigo: ", codigoest, ", nombre: ", nomest, ", nota: ", notaest)
else:
    print("El estudinte no se encuentra en la base de datos")
