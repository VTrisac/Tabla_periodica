tabla = "Aluminio", "Al", "Azufre", "S", "Bismuto", "Bi", "Cloro", "Cl", "Mercurio", "Hg"

def locelemento(nombre):
    #Creamos una tupla con todos los elementos en mayúsculas
    tablaMayus = tuple(map(lambda e:e.upper(), tabla))
    if nombre.upper() in tablaMayus:
        # Si el indice del nombre a buscar es par, es un nombre de elemento y no un simbolo
        #Al dividir entre 2 no debe tener decimales, para ello el resto ha de ser igual a cero.
        indice = tablaMayus.index(nombre.upper())
        if indice % 2 != 0:
            print("¡Has indicado un símbolo en lugar de un elemento!")
        else:
            print((tabla[indice].ljust(15, ".") +
            tabla[indice+1].rjust(10, ".")))
    else:
        print("Elemento no encontrado en la tabla.")

def locsimbolo(nombre):
    #Creamos una tupla con todos los elementos en mayúsculas
    tablaMayus = tuple(map(lambda e:e.upper(), tabla))
    if nombre.upper() in tablaMayus:
        # Si el indice del nombre a buscar es impar, es un símbolo y no un nombre de elemento
        #Al dividir entre 2 debe tener decimales, para ello el resto ha de ser distinto a cero.
        indice = tablaMayus.index(nombre.upper())
        if indice % 2 == 0:
            print("¡Has indicado un elemento en lugar de un símbolo!")
        else:
            print((tabla[indice].ljust(15, ".") +
            tabla[indice-1].rjust(10, ".")))
    else:
        print("Símbolo no encontrado en la tabla.")

opcion = -1
while opcion != 0:
    print("\nTABLA PERIODICA - MENU DE OPCIONES:")
    print("1 - Buscar por elemento")
    print("2 - Buscar por simbolo")
    print("0 - Salir")
    opcion = eval(input("Escriba opcion: "))
    if opcion == 1:
        elemento = input("Escribe el nombre del elemento quimico: ")
        locelemento(elemento)
    if opcion == 2:
        simbolo = input("Escribe el simbolo del elemento quimico: ")
        locsimbolo(simbolo)
print("Gracias por usar el programa.")
