from profesiones import seleccionar_profesion
from origen import seleccionar_origen_fondos
from activos import seleccionar_origen_bienes


def inicio_programa():
    proceder = input("Para registrarse presione S, para salir presione N: ")#cambio lower
    if proceder == 's':
        return registro()  
    elif proceder == 'n':
        return None 
    else:
        print("Opción no válida. Por favor, elija S o N.")
        return inicio_programa()

#INGRESO DE DATOS
def ingreso_datos():
#DNI
    dni_valido = False
    while not dni_valido:
        dni = input("Ingrese su DNI: ")
        if len(dni) >= 8:
            dni_valido = True  
            for i in dni:
                if i < '0' or i > '9':  
                    dni_valido = False  
        if not dni_valido:
            print("Por favor, ingrese un DNI válido (solo números y al menos 8 dígitos).")
    
#APELLIDO
    apellido_valido = False
    while not apellido_valido:
        apellido = input("Ingrese su Apellido: ")

    # Verificamos si todos los caracteres del apellido son letras
        apellido_valido = True  # Asumimos que es válido inicialmente
        for char in apellido:
            if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
                apellido_valido = False  
                print("Por favor ingrese solo letras para el apellido.") 
    
            
#NOMBRE           
    nombre_valido = False
    while not nombre_valido:
        nombre = input("Ingrese su Nombre: ")

        nombre_valido = True  
        for char in nombre:
            if not ('a' <= char <= 'z'  or 'A' <= char <= 'Z'):  
                nombre_valido = False 
                print("Por favor ingrese solo letras para el nombre.")    
                
#EDAD
    edad_valida = False
    while not edad_valida:
        edad = input("Ingrese su Edad: ") 
        if len(edad) <= 3:
            edad_valida = True   
            for i in edad:
                if i < '0' or i > '9':  
                    edad_valida = False  
            if edad_valida:
                if int(edad) < 1 or int(edad) > 150:
                    edad_valida = False  
        if not edad_valida:
            print("Por favor, ingrese una edad válida (entre 1 y 150).")

#FECHA DE NACIMIENTO
    fecha_nacimiento = False  
    while not fecha_nacimiento:
        fecha_nacimiento_input = input("Ingrese su fecha de Nacimiento (dd/mm/yyyy): ")
        if len(fecha_nacimiento_input) == 10 and fecha_nacimiento_input[2] == '/' and fecha_nacimiento_input[5] == '/':
            fecha_nacimiento = True  
        else:
            print("Formato incorrecto. Ingrese la fecha en formato dd/mm/yyyy.")
            
#PROFESION           
    profesion = seleccionar_profesion()

#FECHA DE DECLARACION
    fecha_declaracion = False
    while not fecha_declaracion:
        fecha_declaracion_input = input("Ingrese la fecha de Declaracion (dd/mm/yyyy): ")
        if len(fecha_declaracion_input) == 10 and fecha_declaracion_input[2] == '/' and fecha_declaracion_input[5] == '/':
            fecha_declaracion = True
        else:
            print("Formato incorrecto. Ingrese la fecha en formato dd/mm/yyyy.")
            
#MONTO A DECLARAR
    monto_valido = False
    while not monto_valido:
        monto_input = input("Ingrese el Monto a Declarar: ")
        monto_valido = True  
        for char in monto_input:
            if char < '0' or char > '9':  
                monto_valido = False
        if not monto_valido:
            print("Por favor, ingrese un monto válido.")
        else:
            monto = int(monto_input)
            
            
#ORIGEN DE LOS FONDOS
    origen_fondos = seleccionar_origen_fondos()
    
    
#ACTIVOS REGULARIZADOS
    bien_final = seleccionar_origen_bienes()
    

    return dni, apellido, nombre, edad, fecha_nacimiento_input, profesion, fecha_declaracion_input, monto, origen_fondos, bien_final

# FUNCION PARA REGISTRAR
def registro():
    contribuyentes = []
    continuar = 's'
    while continuar == 's':  
        contribuyentes.append(ingreso_datos())  
        continuar = input("\n¿Desea ingresar otro contribuyente? (S/N): ")
    return contribuyentes    

# RESULTADOS
def resultados(contribuyentes):
    activo_argentina = 0
    activo_exterior = 0

    for contribuyente in contribuyentes:
        bien_final = contribuyente[-1]  
        if "Argentina" in bien_final:
            activo_argentina += 1
        elif "Exterior" in bien_final:
            activo_exterior += 1

    totalactivos = activo_argentina + activo_exterior

    porcentaje_arg = (activo_argentina / totalactivos) * 100
    porcentaje_ext = (activo_exterior / totalactivos) * 100

    for contribuyente in contribuyentes:
        dni, apellido, nombre, edad, fecha_nacimiento_input, profesion, fecha_declaracion_input, monto, origen_fondos, bien_final = contribuyente
        print(f"\nDNI: {dni}")
        print(f"Apellido: {apellido}")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Fecha de nacimiento: {fecha_nacimiento_input}")
        print(f"Profesion: {profesion}")
        print(f"Fecha de declaracion: {fecha_declaracion_input}")
        print(f"Monto a declarar: {monto}")
        print(f"Origen de fondos: {origen_fondos}")
        print(f"Origen de activos: {bien_final}")
    return porcentaje_arg, porcentaje_ext

#Buscar por DNI

def buscar_declaracion(contribuyentes):
    dni_buscar = input("\nIngrese el número de DNI del contribuyente que desea buscar: ")

    encontrado = False
    for contribuyente in contribuyentes:
        if contribuyente[0] == dni_buscar:
            encontrado = True
            print("\n--- Declaración Jurada Encontrada ---")
            print(f"DNI: {contribuyente[0]}")
            print(f"Apellido: {contribuyente[1]}")
            print(f"Nombre: {contribuyente[2]}")
            print(f"Edad: {contribuyente[3]}")
            print(f"Fecha de nacimiento: {contribuyente[4]}")
            print(f"Profesión: {contribuyente[5]}")
            print(f"Fecha de declaración: {contribuyente[6]}")
            print(f"Monto a declarar: {contribuyente[7]}")
            print(f"Origen de fondos: {contribuyente[8]}")
            print(f"Origen de activos: {contribuyente[9]}")
    if not encontrado:
        print("No se encontró una declaración jurada con ese DNI.")
    
    continuar = input("\n¿Desea buscar otra declaración jurada? (S/N): ")
    if continuar == 's':
        buscar_declaracion(contribuyentes)


