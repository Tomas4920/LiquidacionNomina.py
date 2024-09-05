def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("El valor debe ser positivo.")
            return value
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtalo de nuevo.")

def get_int_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                raise ValueError(f"El valor debe estar entre {min_value} y {max_value}.")
            return value
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtalo de nuevo.")

def main():
    print("Bienvenido al sistema de cálculo de nómina.")

    salary = get_float_input("Introduce el sueldo mensual: ")
    days_worked = get_int_input("Introduce los días trabajados en el mes (1-31): ", 1, 31)
    hours_worked = get_float_input("Introduce las horas trabajadas en el día (0-24): ")
    commissions = get_float_input("Introduce el total de comisiones: ")
    overtime_hours = get_float_input("Introduce las horas extras trabajadas: ")

    try:
        payroll = calculate_payroll(salary, days_worked, hours_worked, commissions, overtime_hours)
        print("\nResumen de la nómina:")
        print(f"Total ganado: ${payroll['total_earned']:.2f}")
        print(f"Deducciones por salud: ${payroll['health_deductions']:.2f}")
        print(f"Deducciones por pensión: ${payroll['pension_deductions']:.2f}")
        print(f"Total deducciones: ${payroll['total_deductions']:.2f}")
        print(f"Pago final: ${payroll['final_payroll']:.2f}")
    except PayrollException as e:
        print(f"Error en el cálculo de la nómina: {e}")

if __name__ == "__main__":
    main()
