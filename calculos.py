def calcular_edad_promedio(contribuyentes):
    edades = []
    
    for contribuyente in contribuyentes:
        edades.append(int(contribuyente[3]))  
        
    menor_edad = edades[0]
    mayor_edad = edades[0]
    total_edades = 0
    
    for edad in edades:
        if edad < menor_edad:
            menor_edad = edad
        if edad > mayor_edad:
            mayor_edad = edad
        total_edades += edad
    
    edad_promedio = total_edades / len(edades)
    
    return mayor_edad, menor_edad, edad_promedio

def calcular_fechas(contribuyentes):
    fechas_declaracion = []
    
    for contribuyente in contribuyentes:
        fecha_str = contribuyente[6]  
        fechas_declaracion.append(fecha_str)
    
    fecha_lejana = fechas_declaracion[0]  
    fecha_cercana = fechas_declaracion[0]  
    
  
    for fecha in fechas_declaracion:
        if fecha > fecha_lejana:
            fecha_lejana = fecha
        if fecha < fecha_cercana:
            fecha_cercana = fecha
    
    return fecha_lejana, fecha_cercana

def calcular_monto_promedio(contribuyentes):
    montos = []
    
    for contribuyente in contribuyentes:
        montos.append(int(contribuyente[7]))
        
    monto_menor = montos[0]
    monto_mayor = montos[0]
    total_montos = 0
    
    for monto in montos:
        if monto < monto_menor:
            monto_menor = monto
        if monto > monto_mayor:
            monto_mayor = monto
        total_montos += monto
    
    monto_promedio = total_montos / len(montos)
    
    return monto_mayor, monto_menor, monto_promedio