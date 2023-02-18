lmeses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
ltbogota = [19,19,19,18,18,18,17,17,18,18,18,19]
ltmedellin = [25,25,25,25,26,26,26,26,25,25,25,25]
ltcali = [29,29,29,28,28,28,29,29,29,28,28,28]
ltbarranquilla = [30,30,31,31,32,32,32,32,32,31,31,30]

posmayo= lmeses.index("mayo")

def temp25a27 (listciudad, mes,ciudad):
    if listciudad[mes]>=25 and listciudad[mes]<=27:
        print(ciudad, "en el mes de mayo si tuvo una temperatura entre los 25 y 27 grados centigrados")

temp25a27(ltbogota,posmayo,"Bogota")
temp25a27(ltmedellin,posmayo,"Medellin")
temp25a27(ltcali,posmayo,"Cali")
temp25a27(ltbarranquilla,posmayo,"Barranquila")

print ("\n")

def superior31 (listciudad,ciudad):
    for i in range (0,11,1):
        if listciudad[i]>31:
           print(ciudad, "tuvo temperaturas mayores a 31 grados centigrados")
           break    

superior31 (ltbogota,"Bogota")
superior31 (ltmedellin,"Medellin")
superior31 (ltcali,"Cali")
superior31 (ltbarranquilla,"Barranquilla")

def messup31(listciudad,):
    for i in range (0,11,1):
        if listciudad[i]>31:
           print ("Mes mayor a 31 grados centigrados: ", lmeses[i])

messup31 (ltbogota)
messup31 (ltmedellin)
messup31 (ltcali)
messup31 (ltbarranquilla)
    

        
    
