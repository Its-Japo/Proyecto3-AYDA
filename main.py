def mtf():
    elementos = [0, 1, 2, 3, 4]
    solicitudes = [int(x) for x in input("Ingrese el listado de solicitudes: ").strip().split(" ")]

    costoTotal = 0

    if any(solicitud not in elementos for solicitud in solicitudes):
        print('Elementos de solicitud no existen en la lista de configuración')
        return

    print('==== ALGORITMO MTF ====')
    print(27*'--')
    for req in solicitudes:

        for index in range(len(elementos)):
            if elementos[index] == req:
                costoTotal += index + 1
                elementos.remove(req)
                elementos.insert(0, req)
                print(f'Lista de configuración: {elementos} | Solicitud {req} | Costo: {index + 1} | Costo Acumulado: {costoTotal}')
                break

    print(f'El costo total de las solicitudes es {costoTotal}')


def imtf():
    elementos = [0, 1, 2, 3, 4]
    solicitudes = [int(x) for x in input("Ingrese el listado de solicitudes: ").strip().split(" ")]

    costoTotal = 0

    if any(solicitud not in elementos for solicitud in solicitudes):
        print('Elementos de solicitud no existen en la lista de configuración')
        return

    print('==== ALGORITMO IMTF ====')
    for reqIndex in range(len(solicitudes)):
        for index in range(len(elementos)):
            if elementos[index] == solicitudes[reqIndex]:
                costoTotal += index + 1
                print(f'Lista de configuración: {elementos} | Solicitud {solicitudes[reqIndex]} | Costo: {index + 1} | Costo Acumulado: {costoTotal}')

                if solicitudes[reqIndex] in solicitudes[(reqIndex+1):(reqIndex+index+1)]:
                    elementos.remove(solicitudes[reqIndex])
                    elementos.insert(0, solicitudes[reqIndex])
                    break

    print(f'El costo total de las solicitudes es {costoTotal}')


if __name__ == "__main__":
    while True:
        print("""
        1. MTF
        2. IMFT
        3. Salir
        """)

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mtf()
        elif opcion == "2":
            imtf()
        elif opcion == "3":
            exit(0)
        else:
            print("Ingrese una opción válida")
