def calcular_nomina(salario_basico, subsidio_transporte, tiempo_laborado, tiempo_festivo_laborado, horas_extras, porcentaje_salud, porcentaje_pension, tiempo_incapacidades, tiempo_licencias):

    
    SALARIO_HORA = salario_basico / 160  # VALOR ALEATORIO DE HORAS QUE PUSE 
    VALOR_HORA_EXTRA = SALARIO_HORA * 1.5  # QUE LA HORA EXTRA SE PAGUE EN 1.5
    VALOR_HORA_FESTIVO = SALARIO_HORA * 2  # SE PAGUEN EL DOBLE (SUPOSICION)

    
    valor_horas_extras = horas_extras * VALOR_HORA_EXTRA
    valor_festivo_laborado = tiempo_festivo_laborado * VALOR_HORA_FESTIVO
    total_devengado = (salario_basico + subsidio_transporte +
                        valor_horas_extras + valor_festivo_laborado)

    
    base_deduccion = salario_basico + subsidio_transporte
    deduccion_salud = base_deduccion * (porcentaje_salud / 100)
    deduccion_pension = base_deduccion * (porcentaje_pension / 100)

    
    deduccion_incapacidades = tiempo_incapacidades * SALARIO_HORA
    deduccion_licencias = tiempo_licencias * SALARIO_HORA

    total_deducciones = (deduccion_salud + deduccion_pension +
                         deduccion_incapacidades + deduccion_licencias)

   
    total_a_pagar = total_devengado - total_deducciones

    return total_a_pagar

# un ejemplo que hice 
 
salario_basico = 2000000  
subsidio_transporte = 100000  
tiempo_laborado = 160  
tiempo_festivo_laborado = 8  
horas_extras = 10 
porcentaje_salud = 4  
porcentaje_pension = 4  
tiempo_incapacidades = 0  
tiempo_licencias = 0  

total = calcular_nomina(salario_basico, subsidio_transporte, tiempo_laborado, tiempo_festivo_laborado, horas_extras, porcentaje_salud, porcentaje_pension, tiempo_incapacidades, tiempo_licencias)
print(f"Total a pagar al empleado: {total:.2f}")
