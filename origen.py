ORIGEN_FONDOS = [
        "Ingresos de actividades lícitas (salarios, rentas, ganancias de inversiones)",
        "Herencias o donaciones",
        "Venta de activos (propiedades, bienes muebles, acciones)",
        "Ahorros o fondos personales",
        "Inversiones extranjeras o bienes fuera del país",
        "Operaciones financieras informales o no registradas",
        "Fondeo o reestructuración de deuda (préstamos, refinanciación de deudas)",
        "Fondos provenientes de actividades no declaradas",
]

def seleccionar_origen_fondos():
        print("\nSeleccione el Origen de los Fondos: ")
        origen_fondos = 0
        while origen_fondos < 1 or origen_fondos > len(ORIGEN_FONDOS):
                i = 1
                for fondos in ORIGEN_FONDOS:
                        print(f"{i}- {fondos}")
                        i += 1
                seleccion = input("Seleccione el origen de fondo: ")
                
                seleccion_valida = True
                for char in seleccion:
                        if char < '0' or char > '9':
                                seleccion_valida = False
                                
                if seleccion_valida:
                        origen_fondos = int(seleccion)
                        if origen_fondos < 1 or origen_fondos > len(ORIGEN_FONDOS):
                                print("Por favor, ingrese un origen valido dentro del rango.")
                
        return ORIGEN_FONDOS[origen_fondos - 1]
                                
def ranking_origen_fondos(contribuyentes):
        
    origenes = [contribuyente[8] for contribuyente in contribuyentes]  
    origenes_unicos = []
    conteos = []

    for origen in origenes:
        encontrado = False
        for i in range(len(origenes_unicos)):
            if origenes_unicos[i] == origen:
                conteos[i] += 1
                encontrado = True
        if not encontrado:
            origenes_unicos.append(origen)
            conteos.append(1)

    for i in range(len(conteos)):
        for j in range(i + 1, len(conteos)):
            if conteos[j] > conteos[i]:
                conteos[i], conteos[j] = conteos[j], conteos[i]
                origenes_unicos[i], origenes_unicos[j] = origenes_unicos[j], origenes_unicos[i]

    return origenes_unicos, conteos

