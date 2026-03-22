#Utilizando la siguiente lista y variable, determine si el valor 
#de la variable coincide o no con un valor de la lista. 
#Sugerencia, si es necesario, utilice un bucle for in y el operador in.
nombre = 'George' #Nombre a buscar 
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán'] #Lista de nombres

for x in lista_nombre: #Recorre cada elemento de la lista
    if nombre == x: #compara el nombre con el elemento actual
        print(f"{nombre} está en la lista") #Si coincide, imprime mensaje
        break #Termina el bucle inmediatamente
else: #el for al terminar sin un break,   
    print("No hay coincidencias") #imprime mensaje