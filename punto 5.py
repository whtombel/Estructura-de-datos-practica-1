A=[5,8,4,14,2,1,10,3,5]


def ordenar(vector):
    tamaño = len(vector)
    for actual in range(0,tamaño):    
        mas_pequeno = actual
        for i in range(actual+1,tamaño) :
            if vector[i] < vector[mas_pequeno] :
                mas_pequeno = i
                

                
        if min is not actual :
            tempo = vector[actual]
            vector[actual] = vector[mas_pequeno]
            vector[mas_pequeno] = tempo
            
    return vector


print ("El vector sin ningún orden es: ", A)    
print ("El vector organizado quedaría: " , ordenar(A))



         
