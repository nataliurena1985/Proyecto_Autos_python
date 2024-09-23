
autos = ["Ferrari", "VolksWagen", "Fiat", "Lamborghini", "Tesla", "Honda"]

precios_autos = [10000000, 5000000, 500000, 9500000, 8000000, 1000000]

motos = ["Zanella", "Motomel", "Harley", "Honda"]

precios_motos = [100000, 250000, 2000000, 1000000]



def autoMasCaro():
    pre_max = precios_autos[0]  # Empezamos con el primer valor de la lista
    idx_max = 0  # Guardamos el índice del auto más caro
    for i in range(len(precios_autos)):  # Recorremos los índices
        if precios_autos[i] > pre_max:
            pre_max = precios_autos[i]
            idx_max = i  # Actualizamos el índice cuando encontramos un precio mayor
    return autos[idx_max], pre_max  # Devolvemos el auto y el precio más alto



def motoMasBarata():
    pre_min = precios_motos[0]  # Inicializamos con el primer precio
    idx_min = 0  # Índice de la moto más barata
    for i in range(len(precios_motos)):
        if precios_motos[i] < pre_min:
            pre_min = precios_motos[i]
            idx_min = i  # Actualizamos el índice cuando encontramos un precio menor
    return motos[idx_min], pre_min  # Devolvemos la moto más barata y su precio


def marcasDeAmbos(autos, motos):
    m_com = []  # Lista para almacenar las marcas de ambos
    for auto in autos:   # Recorremos con el elemento auto cada marca  en la lista de autos
        if auto in motos:  # Si la marca también está en la lista de motos
            m_com .append(auto)  # Añadimos el elemento auto, la marca a la lista de comunes 
    return m_com 






def menu():
    while True:
        print("\n   Opciones:")
        print("1. Auto más caro")
        print("2. Moto más barata")
        print("3. Marcas que fabrican tanto autos y motos")
        print("4. Todas las opciones a la vez")
        print("5. Salir")

        opcion = input("\n Elija una opción de 1 a 5: ")
        if opcion == '1':
            auto, pre_max = autoMasCaro()
            print(" \n El auto más caro es:", auto, "tiene un precio de: $", pre_max)
        elif opcion == '2':
           moto, pre_min = motoMasBarata()
           print(" \n La moto más barata es:", moto, "con un precio de: $", pre_min)
        elif opcion == '3':
           m_com  = marcasDeAmbos(autos, motos)
           print("\n Marcas que fabrican tanto autos como motos:", m_com )
        elif opcion == '4':
           auto, pre_max = autoMasCaro()
           moto, pre_min = motoMasBarata()
           m_com  = marcasDeAmbos(autos, motos)
           print(" \n El auto más caro es:", auto, "tiene un precio de: $", pre_max)
           print(" \n La moto más barata es:", moto, "con un precio de: $", pre_min)
           print("\n Marcas que fabrican tanto autos como motos:", m_com )
        elif opcion == "5":
            print("Saliendo del MENU.")
            break
        else:
            print("\n Opción inválida. Intente de nuevo.")





# Ejecutamos el menú
menu()