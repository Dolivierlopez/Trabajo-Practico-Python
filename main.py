from activos import contar_activos_repetidos
from calculos import calcular_edad_promedio, calcular_fechas, calcular_monto_promedio
from profesiones import ranking_profesiones
from origen import ranking_origen_fondos
from inputs import registro, resultados,buscar_declaracion
def main():
    contribuyentes = registro()  
    porcentaje_arg, porcentaje_ext = resultados(contribuyentes)  
    mayor_edad, menor_edad, edad_promedio = calcular_edad_promedio(contribuyentes)
    fecha_lejana, fecha_cercana = calcular_fechas(contribuyentes)
    monto_mayor, monto_menor, monto_promedio = calcular_monto_promedio(contribuyentes)
    origenes_unicos, conteos = ranking_origen_fondos(contribuyentes)
    profesiones_vacias, conteo_profesiones = ranking_profesiones(contribuyentes)
    activo_mas_repetido, activo_menos_repetido = contar_activos_repetidos(contribuyentes)
    
    print(f"\nTotal de personas registradas: {len(contribuyentes)}")
     
    print(f"Edad Menor: {menor_edad}")
    print(f"Edad Mayor: {mayor_edad}")
    print(f"Edad Promedio: {edad_promedio}")
    print(f"Fecha de Declaración más lejana: {fecha_lejana}")
    print(f"Fecha de Declaración más cercana: {fecha_cercana}")
    print(f"Monto Menor: {monto_menor}")
    print(f"Monto Mayor: {monto_mayor}")
    print(f"Monto Promedio: {monto_promedio}")
    print(f"Porcentaje de bienes declarados en Argentina: {porcentaje_arg}%")
    print(f"Porcentaje de bienes declarados en el Exterior: {porcentaje_ext}%")
    print(f"El activo regularizado que más se repite es: {activo_mas_repetido}")
    print(f"El activo regularizado que menos se repite es: {activo_menos_repetido}")

    
    print("\n!----Ranking de Profesiones----!")
    for i in range(len(profesiones_vacias)):
        print(f"{i + 1}.{profesiones_vacias[i]} - {conteo_profesiones[i]}")
    print("\n!----Ranking de Origen de fondos----!")
    for i in range(len(origenes_unicos)):
        print(f"{i + 1}.{origenes_unicos[i]} - {conteos[i]}")
 
    # \n
    buscar_declaracion(contribuyentes)

# EJECUTAR EL PROGRAMA
main()