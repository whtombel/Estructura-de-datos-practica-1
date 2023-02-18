ledades = [13,14,16,13,11,18,17,15,15,15,14,16,13,12,14,16,15,16,17,12]


def Insertion_sort(Vector):
    for i in range(1,len(Vector)):
        actual = Vector[i]
        j = i
        #Desplazamiento de los elementos de la matriz
        while j>0 and Vector[j-1]<actual:
            Vector[j]=Vector[j-1]
            j = j-1
        #insertar el elemento en su lugar
        Vector[j]=actual
    return(Vector)

def promedio (vector):
    suma= sum(ledades)
    cantidad= len(vector)
    promedio = round(suma/cantidad)
    return promedio


    
print("las edades ordenadas en forma decendente: ", Insertion_sort(ledades))
print ("El numero que se aproxima al promedio de las edades es: ", promedio(ledades))
