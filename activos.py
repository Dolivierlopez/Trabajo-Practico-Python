# Listas de bienes en Argentina y el Exterior
BIENES_ARGENTINA = [
    "Moneda nacional o extranjera en efectivo o depositada en cuentas bancarias o entidades residentes en Argentina",
    "Inmuebles ubicados en Argentina",
    "Acciones, participaciones en sociedades, derechos en fideicomisos o cuotapartes de fondos comunes de inversión emitidos por sujetos residentes en Argentina que no coticen en bolsas",
    "Títulos valores (acciones, bonos, obligaciones negociables, certificados de depósito, cuotas de fondos, etc.) que coticen en bolsas reguladas en Argentina",
    "Otros bienes muebles no incluidos en los incisos anteriores, ubicados en Argentina",
    "Créditos cuyo deudor sea residente fiscal en Argentina",
    "Derechos y bienes intangibles no incluidos en los incisos anteriores, pertenecientes a residentes fiscales en Argentina",
    "Criptomonedas, criptoactivos y bienes similares",
    "Otros bienes susceptibles de valor económico, incluyendo bienes y créditos originados en pólizas de seguro contratadas en el exterior de sujetos residentes fiscales en Argentina",
]

BIENES_EXTERIOR = [
    "Moneda extranjera en efectivo o depositada en cuentas bancarias o entidades financieras en el exterior",
    "Inmuebles ubicados fuera de Argentina",
    "Acciones, participaciones en sociedades, derechos en fideicomisos o similares emitidos por sujetos no residentes en Argentina que no coticen en bolsas",
    "Títulos valores (acciones, bonos, obligaciones negociables, certificados de depósito, cuotas de fondos, etc.) que coticen en bolsas o mercados del exterior",
    "Otros bienes muebles no incluidos en los incisos anteriores, ubicados fuera de Argentina",
    "Créditos cuyo deudor no sea residente fiscal en Argentina",
    "Derechos y bienes intangibles no incluidos en los incisos anteriores",
    "Otros bienes ubicados fuera del país no incluidos en los incisos anteriores",
]

def seleccionar_origen_bienes():
    origen_valido = False
    while not origen_valido:
        print("\n¿Dónde están ubicados sus bienes?")
        print("1- Argentina")
        print("2- Exterior")
        origen_input = input("Seleccione el origen de los bienes (1 o 2): ")
        if origen_input in ["1", "2"]:
            origen_valido = True
        else:
            print("Por favor, seleccione una opción válida (1 o 2).")
    
    if origen_input == "1":
        bienes = BIENES_ARGENTINA
        ubicacion = "Argentina"
    else:
        bienes = BIENES_EXTERIOR
        ubicacion = "Exterior"

    bien_valido = False
    while not bien_valido:
        print("\nSeleccione el bien correspondiente:")
        i = 1
        for bien in bienes:
            print(f"{i}- {bien}")
            i += 1
        
        bien_input = input("Seleccione el número del bien: ")
        bien_valido = True
        for char in bien_input:
            if char < '0' or char > '9':
                bien_valido = False
        
        if bien_valido:
            bien_seleccionado = int(bien_input)
            if bien_seleccionado < 1 or bien_seleccionado > len(bienes):
                bien_valido = False
                print("Por favor, seleccione un número válido dentro del rango.")
        else:
            print("Por favor, ingrese un número válido.")
    return ubicacion, bienes[bien_seleccionado - 1]

def contar_activos_repetidos(contribuyentes):
    activos = [contribuyente[9][1] for contribuyente in contribuyentes]
    activos_unicos = []
    conteos = []

    for activo in activos:
        encontrado = False
        for i in range(len(activos_unicos)):
            if activos_unicos[i] == activo:
                conteos[i] += 1
                encontrado = True
        if not encontrado:
            activos_unicos.append(activo)
            conteos.append(1)

    for i in range(len(conteos)):
        for j in range(i + 1, len(conteos)):
            if conteos[j] > conteos[i]:
                conteos[i], conteos[j] = conteos[j], conteos[i]
                activos_unicos[i], activos_unicos[j] = activos_unicos[j], activos_unicos[i]

    activo_mas_repetido = activos_unicos[0]
    activo_menos_repetido = activos_unicos[-1]
    
    return activo_mas_repetido, activo_menos_repetido


