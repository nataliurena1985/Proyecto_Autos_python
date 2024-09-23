'''
Proyecto Autos
Te presentamos 4 listas:

autos = ["Ferrari", "VolksWagen", "Fiat", "Lamborghini", "Tesla", "Honda"]

precios_autos = [10000000, 5000000, 500000, 9500000, 8000000, 1000000]

motos = ["Zanella", "Motomel", "Harley", "Honda"]

precios_motos = [100000, 250000, 2000000, 1000000]

Deberás escribir:
Una función que nos de el precio del auto más caro.  v
Una función que nos de el precio de la moto más barata. v
Una función que devuelva las marcas de autos que también fabrican motos. v
Una función MENU que nos permita:
Elegir cual de las opciones anteriores queremos ejecutar  v
Ejecutar más de una vez si el usuario lo desea
Consultar los 3 valores al mismo tiempo.
Las listas ya están dadas y NO pueden modificarse

Utilizar obligatoriamente funciones para la resolución de este ejercicio.

👉 Entregá tu proyecto en el siguiente link: Formulario Proyecto Autos

Fecha límite: 28 de septiembre


'''


'''

def autoMasCaro(precios_autos):
    pre_max = precios_autos[0]  # Empezamos con el primer valor de la lista
    for precio in precios_autos:
        if precio > pre_max:
            pre_max = precio
    return pre_max

precios_autos = [10000000, 5000000, 500000, 9500000, 8000000, 1000000]
pre_max = autoMasCaro(precios_autos)
print("El precio del auto más caro es:", pre_max)

'''




'''
def motoMasBarata(precios_motos):
    pre_min = precios_motos[0]  
    for precio in precios_motos:
       
        if precio < pre_min:

            pre_min = precio
    return pre_min

precios_motos = [100000, 250000, 2000000, 1000000]
pre_min = motoMasBarata(precios_motos)
print("El precio de la moto más barata es:", pre_min)
'''




'''
def marcasDeAmbos(autos, motos):
    m_com = []  # Lista para almacenar las marcas de ambos
    for auto in autos:   # Recorremos con el elemento auto cada marca  en la lista de autos
        if auto in motos:  # Si la marca también está en la lista de motos
            m_com .append(auto)  # Añadimos el elemento auto, la marca a la lista de comunes 
    return m_com 

# Listas de autos y motos
autos = ["Ferrari", "VolksWagen", "Fiat", "Lamborghini", "Tesla", "Honda"]
motos = ["Zanella", "Motomel", "Harley", "Honda"]

# Llamamos a la función
m_com  = marcasDeAmbos(autos, motos)
print("Marcas que fabrican tanto autos como motos:", m_com )

'''




'''

# Listas de autos y motos con sus precios
autos = ["Ferrari", "VolksWagen", "Fiat", "Lamborghini", "Tesla", "Honda"]
precios_autos = [10000000, 5000000, 500000, 9500000, 8000000, 1000000]
motos = ["Zanella", "Motomel", "Harley", "Honda"]
precios_motos = [100000, 250000, 2000000, 1000000]

# Función para obtener el auto más caro
def auto_mas_caro():
    indice_caro = precios_autos.index(max(precios_autos))  # Encontramos el índice del auto más caro
    return autos[indice_caro], max(precios_autos)

# Función para obtener la moto más barata
def moto_mas_barata():
    indice_barato = precios_motos.index(min(precios_motos))  # Encontramos el índice de la moto más barata
    return motos[indice_barato], min(precios_motos)

# Función para encontrar marcas que fabrican tanto autos como motos
def marcas_que_fabrican_ambos():
    marcas_comunes = []
    for auto in autos:
        if auto in motos:
            marcas_comunes.append(auto)
    return marcas_comunes

# Función MENU para ejecutar las opciones
def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Ver el auto más caro")
        print("2. Ver la moto más barata")
        print("3. Ver las marcas que fabrican tanto autos como motos")
        print("4. Consultar todas las opciones a la vez")
        print("5. Salir")
        
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == '1':
            auto, precio = auto_mas_caro()
            print(f"\nEl auto más caro es {auto} con un precio de ${precio}.")
        elif opcion == '2':
            moto, precio = moto_mas_barata()
            print(f"\nLa moto más barata es {moto} con un precio de ${precio}.")
        elif opcion == '3':
            marcas = marcas_que_fabrican_ambos()
            if marcas:
                print(f"\nLas marcas que fabrican tanto autos como motos son: {', '.join(marcas)}.")
            else:
                print("\nNo hay marcas que fabriquen tanto autos como motos.")
        elif opcion == '4':
            # Consultamos todas las opciones al mismo tiempo
            auto, precio_auto = auto_mas_caro()
            print(f"\nEl auto más caro es {auto} con un precio de ${precio_auto}.")
            
            moto, precio_moto = moto_mas_barata()
            print(f"La moto más barata es {moto} con un precio de ${precio_moto}.")
            
            marcas = marcas_que_fabrican_ambos()
            if marcas:
                print(f"Las marcas que fabrican tanto autos como motos son: {', '.join(marcas)}.")
            else:
                print("No hay marcas que fabriquen tanto autos como motos.")
        elif opcion == '5':
            print("\n¡Gracias por usar el menú! Adiós.")
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")

# Ejecutamos el menú
menu()

'''



'''
def autoMasCaro():
    pre_max = precios_autos[0]  # Empezamos con el primer valor de la lista
    idx_max = 0  # Guardamos el índice del auto más caro
    for i in range(len(precios_autos)):  # Recorremos los índices
        if precios_autos[i] > pre_max:
            pre_max = precios_autos[i]
            idx_max = i  # Actualizamos el índice cuando encontramos un precio mayor
    return autos[idx_max], pre_max  # Devolvemos el auto y el precio más alto


autos = ["Ferrari", "VolksWagen", "Fiat", "Lamborghini", "Tesla", "Honda"]
precios_autos = [10000000, 5000000, 500000, 9500000, 8000000, 1000000]

auto, pre_max = autoMasCaro()
print("El auto más caro es:", auto, "con un precio de: $", pre_max)

'''



def motoMasBarata():
    pre_min = precios_motos[0]  # Inicializamos con el primer precio
    idx_min = 0  # Índice de la moto más barata
    for i in range(len(precios_motos)):
        if precios_motos[i] < pre_min:
            pre_min = precios_motos[i]
            idx_min = i  # Actualizamos el índice cuando encontramos un precio menor
    return motos[idx_min], pre_min  # Devolvemos la moto más barata y su precio


motos = ["Zanella", "Motomel", "Harley", "Honda"]
precios_motos = [100000, 250000, 2000000, 1000000]

moto, pre_min = motoMasBarata()
print("La moto más barata es:", moto, "con un precio de: $", pre_min)













