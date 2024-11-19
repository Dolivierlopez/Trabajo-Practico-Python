PROFESIONES = [
    "Médico",
    "Ingeniero civil",
    "Abogado",
    "Profesor",
    "Contador público",
    "Desarrollador de software",
    "Diseñador gráfico",
    "Psicólogo",
    "Arquitecto",
    "Farmacéutico",
    "Periodista",
    "Enfermero",
    "Electricista",
    "Carpintero",
    "Mecánico automotriz",
    "Chef",
    "Veterinario",
    "Piloto de aviación",
    "Fotógrafo",
    "Fisioterapeuta",
    "Administrador de empresas",
    "Científico de datos",
    "Traductor",
    "Economista",
    "Técnico en sistemas",
    "Analista financiero",
    "Soldador",
    "Barbero",
    "Actor",
    "Biólogo",
    "Químico industrial",
    "Policía",
    "Bombero",
    "Astrónomo",
    "Historiador",
    "Sociólogo",
    "Antropólogo",
    "Cocinero profesional",
    "Trabajador social",
    "Maestro de construcción",
    "Dibujante técnico",
    "Odontólogo",
    "Estilista",
    "Geólogo",
    "Productor musical",
    "DJ",
    "Guía turístico",
    "Agente inmobiliario",
    "Especialista en marketing digital",
    "Piloto de drones",
    "Especialista en ciberseguridad",
    "Camarógrafo",
    "Técnico de sonido",
    "Guardabosques",
    "Florista",
    "Pescador profesional",
    "Ingeniero ambiental",
    "Matemático",
    "Diseñador de videojuegos",
    "Otro"
]

def seleccionar_profesion():
    print("\nSeleccione su Profesión:")
    profesion = 0  
    while profesion < 1 or profesion > len(PROFESIONES):
        i = 1 
        for prof in PROFESIONES:
            print(f"{i}- {prof}")
            i += 1

        seleccion = input("\nSeleccione el número de la profesión que desea elegir: ")

        profesion_valida = True
        for char in seleccion:
            if char < '0' or char > '9':
                profesion_valida = False
                
        if profesion_valida:
            profesion = int(seleccion)
            if profesion < 1 or profesion > len(PROFESIONES):
                print("\nPor favor, ingrese un número válido dentro del rango.")
        else:
            print("Por favor, ingrese un número válido.")
            
    return PROFESIONES[profesion - 1]

def ranking_profesiones(contribuyentes):
        
    profesiones = [contribuyente[5] for contribuyente in contribuyentes]  
    profesiones_vacias = []
    conteo_profesiones = []

    for origen in profesiones:
        encontrado = False
        for i in range(len(profesiones_vacias)):
            if profesiones_vacias[i] == origen:
                conteo_profesiones[i] += 1
                encontrado = True
        if not encontrado:
            profesiones_vacias.append(origen)
            conteo_profesiones.append(1)

    for i in range(len(conteo_profesiones)):
        for j in range(i + 1, len(conteo_profesiones)):
            if conteo_profesiones[j] > conteo_profesiones[i]:
                conteo_profesiones[i], conteo_profesiones[j] = conteo_profesiones[j], conteo_profesiones[i]
                profesiones_vacias[i], profesiones_vacias[j] = profesiones_vacias[j], profesiones_vacias[i]

    return profesiones_vacias, conteo_profesiones

