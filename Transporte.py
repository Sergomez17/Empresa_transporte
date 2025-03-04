def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Ingrese un valor no negativo")
                continue
            return valor
        except:
            print("Entrada inválida")

def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Ingrese un valor no negativo")
                continue
            return valor
        except:
            print("Entrada inválida")

def main():
    total_pasajeros = 0
    total_recaudado = 0
    recaudado_hombres = 0
    recaudado_mujeres = 0
    total_descuentos = 0
    max_recaudacion = -1
    viaje_max = None
    suma_edades = 0
    while True:
        origen = input("Ingrese ciudad de origen: ")
        destino = input("Ingrese ciudad de destino: ")
        precio_viaje = pedir_float("Ingrese precio del viaje: ")
        cantidad_pasajeros = pedir_entero("Ingrese cantidad de pasajeros: ")
        viaje_recaudado = 0
        for i in range(cantidad_pasajeros):
            print("Pasajero", i + 1)
            nombre = input("Ingrese nombre del pasajero: ")
            genero = input("Ingrese género del pasajero (M/F): ").upper()
            edad = pedir_entero("Ingrese edad del pasajero: ")
            es_estudiante = input("¿Es estudiante? (s/n): ").lower()
            costo = precio_viaje
            descuento = 0
            if es_estudiante == "s":
                descuento = 0.3 * precio_viaje
                costo = precio_viaje - descuento
            viaje_recaudado += costo
            total_recaudado += costo
            total_pasajeros += 1
            suma_edades += edad
            if genero == "M":
                recaudado_hombres += costo
            elif genero == "F":
                recaudado_mujeres += costo
            total_descuentos += descuento
        print("El viaje de", origen, "a", destino, "recaudó:", viaje_recaudado)
        if viaje_recaudado > max_recaudacion:
            max_recaudacion = viaje_recaudado
            viaje_max = f"{origen} -> {destino}"
        continuar = input("¿Desea ingresar otro viaje? (s/n): ").lower()
        if continuar != "s":
            break
    print("Total de pasajeros:", total_pasajeros)
    print("Total de dinero recaudado:", total_recaudado)
    print("Total recaudado por hombres:", recaudado_hombres)
    print("Total recaudado por mujeres:", recaudado_mujeres)
    print("Total descuentos aplicados a estudiantes:", total_descuentos)
    if viaje_max is not None:
        print("El viaje que recaudó más dinero fue", viaje_max, "con", max_recaudacion)
    if total_pasajeros > 0:
        print("Promedio de edad de los pasajeros:", suma_edades / total_pasajeros)
    else:
        print("Promedio de edad de los pasajeros: 0")

if __name__ == "__main__":
    main()
