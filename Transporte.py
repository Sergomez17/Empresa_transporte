def solicitar_0_o_1(nombre_de_la_variable):
    while True:
        try:
            valor_de_la_variable = int(input(f'{nombre_de_la_variable}'))
            if valor_de_la_variable == 1 or valor_de_la_variable == 0:
                break
            else:
                print(f'{nombre_de_la_variable} debe ser 1 o 0 rey.')
            
        except ValueError:
            print(f'{nombre_de_la_variable} debe ser un número entero rey.2')
    return valor_de_la_variable

def solicitar_valor_positivo(nombre_de_la_variable):
    while True:
        try:
            valor_variable = float(input(f'Ingrese {nombre_de_la_variable}: '))
            if valor_variable <0:
                print(f'{nombre_de_la_variable} no puede ser negativo.')
            else:
                break
        except ValueError:
            print(f'{nombre_de_la_variable} debe ser un número.')
    return valor_variable

def solicitar_entero_positivo(nombre_de_la_variable):
    while True:
        try:
            valor = int(input(f'Ingrese {nombre_de_la_variable}: '))
            if valor < 0:
                print(f'{nombre_de_la_variable} no puede ser negativo.')
            else:
                return valor
        except ValueError:
            print(f'{nombre_de_la_variable} debe ser un número entero.')

def solicitar_texto(nombre_de_la_variable):
    while True:
        texto = input(f'Ingrese {nombre_de_la_variable}: ')
        if texto == '':
            print(f'{nombre_de_la_variable} no puede estar vacio.')
        else:
            return texto

def solicitar_genero(nombre_de_la_variable):
    while True:
        genero = input(f'Ingrese {nombre_de_la_variable}: ').lower()
        if genero == 'm':
            genero += total_hombres
        elif genero == 'f':
            genero += total_mujeres
            return genero
        else:
            print(f'{nombre_de_la_variable} debe ser f o m.')

total_pasajeros = 0
total_dinero = 0
total_dinero_masculino = 0
total_dinero_femenino = 0
total_hombres = 0
total_mujeres = 0 
total_descuentos = 0
suma_edades = 0
viaje_max_dinero = None
max_dinero = 0

agregar_viaje = solicitar_0_o_1('Ingrese si desea agregar un viaje (0 o 1): ')
while agregar_viaje == 1:
    ciudad_origen = solicitar_texto('ciudad de origen')
    ciudad_destino = solicitar_texto('ciudad de destino')
    precio_viaje = solicitar_valor_positivo('precio del viaje')
    cantidad_pasajeros = solicitar_entero_positivo('la cantidad de pasajeros')
    dinero_viaje = 0
    
    for i in range(cantidad_pasajeros):
        nombre_pasajero = solicitar_texto('nombre del pasajero')
        genero = solicitar_genero('genero del pasajero')
        edad = solicitar_entero_positivo('edad del pasajero')
        es_estudiante = solicitar_0_o_1('el pasajero es estudiante (1 si, 0 si no): ')
        
        if es_estudiante == 1:
            descuento = precio_viaje * 0.30
            pago = precio_viaje - descuento
            total_descuentos += descuento
        else:
            pago = precio_viaje
        dinero_viaje += pago
        total_pasajeros += 1
        suma_edades += edad
        
        if genero == 'm':
            total_dinero_masculino += pago
        else:
            total_dinero_femenino += pago
        
    total_dinero += dinero_viaje
    if dinero_viaje > max_dinero:
            max_dinero = dinero_viaje
            viaje_max_dinero = f'{ciudad_origen} a {ciudad_destino}.'
            
    agregar_viaje = solicitar_0_o_1('desea agregar otro viaje (1 si, 0 no): ')
    
promedio_edad_mujeres = suma_edades / total_mujeres if total_mujeres > 0 else 0

promedio_edad = suma_edades / total_pasajeros if total_pasajeros > 0 else 0

print(f'\nEl promedio de las edades de las mujeres es de: {promedio_edad_mujeres}')
print(f'\nTotal de pasajeros: {total_pasajeros}')
print(f'Total de dinero de los viajes: ${total_dinero}')
print(f'\nTotal dinero de los pasajeros masculinos: ${total_dinero_masculino}')
print(f'Total de dinero de los pasajeros femeninos: ${total_dinero_femenino}')
print(f'\nTotal de los descuentos que se aplicaron: ${total_descuentos}')
print(f'El viaje que recaudo mas dinero fue: {viaje_max_dinero} con ${max_dinero}')
print(f'\nPromedio de la edad de los pasajeros: {promedio_edad}')
print(f'\nTotal de dinero de todos los viajes: ${total_dinero}')