def mostrar_menu():
    """Muestra las opciones de operaciones matemáticas."""
    print("\n" + "="*30)
    print("   CALCULADORA EN PYTHON")
    print("="*30)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("="*30)

def obtener_numero(mensaje):
    """
    Solicita un número al usuario.
    Implementa manejo de excepciones para validar la entrada.
    """
    while True:
        try:
            # Intentamos convertir la entrada del usuario a un número flotante
            valor = float(input(mensaje))
            return valor
        except ValueError:
            # Si el usuario ingresa letras o símbolos, atrapamos el error
            print("[Error] Entrada inválida. Por favor, ingresa únicamente números.")

def calcular():
    """Función principal que controla la lógica y el flujo del programa."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una operación (1-5): ")

        if opcion == '5':
            print("\nCerrando la calculadora. ¡Hasta pronto!")
            break

        if opcion in ('1', '2', '3', '4'):
            # Solicitamos los números usando nuestra función validada
            print("\n--- Ingreso de Datos ---")
            num1 = obtener_numero("Ingresa el primer número: ")
            num2 = obtener_numero("Ingresa el segundo número: ")

            try:
                # Bloque try-except para manejar errores matemáticos
                if opcion == '1':
                    resultado = num1 + num2
                    operacion = "+"
                elif opcion == '2':
                    resultado = num1 - num2
                    operacion = "-"
                elif opcion == '3':
                    resultado = num1 * num2
                    operacion = "*"
                elif opcion == '4':
                    if num2 == 0:
                        # Levantamos un error intencionalmente si el divisor es cero
                        raise ZeroDivisionError("No es posible dividir entre cero.")
                    resultado = num1 / num2
                    operacion = "/"
                
                # Mostramos el resultado si todo salió bien
                print(f"\n[Resultado Exitoso] {num1} {operacion} {num2} = {resultado}")

            except ZeroDivisionError as error:
                # Atrapamos específicamente el error de división por cero
                print(f"\n[Error Matemático] {error}")
            except Exception as error:
                # Atrapamos cualquier otro error inesperado
                print(f"\n[Error Inesperado] Ocurrió un problema: {error}")
        else:
            print("\n[Advertencia] Opción no válida. Elige un número del 1 al 5.")

if  __name__ == "__main__":
    # Punto de entrada del script
    calcular()