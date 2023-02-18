lcodigos=["111","222","333","444","555","666","777","888","999"]
lautores=["gabriel garcia marquez", "rafael pombo", "alvaro mutis", "jorge isaacs","andres caicedo","laura restrepo","mario mendoza", "pilar quintana","hector abad"]
llibros=["la hojarasca","el renacuajo paseador","la nieve del almirante", "la maria", "el atravesado", "delirio", "la melancolia de los feos","caperucita  se come al lobo","el olvido que seremos"]
leditorial=["mondadori","la manchita","punto de lectura","samuel", "norma", "santillana", "grupo planeta", "penguin random house","planeta"]
laregistro=[2002,2007,2012,2010,2008,2020,2015,2022,1999]




codigoaut = input("ingrese el codigo del libro: ")
if codigoaut in lcodigos:
    #encuentra la posicion
    posicion = lcodigos.index(codigoaut)
    nomautor = lautores[posicion]
    nomlibro= llibros[posicion]
    nomeditorial = leditorial[posicion]
    añoregistro = laregistro[posicion]
                              
    print("nombre del libro:", nomlibro,", autor:",nomautor, ", editorial:", nomeditorial, " año de registro:", añoregistro)
else:
    print("El libro no se encuentra en esta biblioteca")

