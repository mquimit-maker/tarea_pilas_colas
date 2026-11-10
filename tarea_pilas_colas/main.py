from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("  ✓ Apilado: ahora es el tope")
        elif op == "2":
            pila.listar()
        elif op == "3":
            pasajero = pila.desapilar()
            if pasajero:
                print(f"  ✓ Salió del tope: {pasajero}")
            else:
                print("  ⚠ La pila está vacía")
        elif op == "4":
            tope = pila.ver_tope()
            if tope:
                print(f"  Tope actual: {tope}")
            else:
                print("  (pila vacía)")
        elif op == "5":
            num = leer_entero("  Ingrese n.º de pasajero a buscar: ")
            pos = pila.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en posición [{pos}]: {pila.datos[pos]}")
            else:
                print("  ❌ No existe")
        elif op == "6":
            num = leer_entero("  N.º de pasajero a modificar: ")
            if pila.buscar(num) != -1:
                dest = input("  Nuevo destino: ").strip()
                asiento = input("  Nuevo asiento: ").strip().upper()
                pila.modificar(num, dest, asiento)
                print("  ✓ Pasajero modificado")
            else:
                print("  ❌ Pasajero no encontrado")
        elif op == "7":
            num = leer_entero("  N.º de pasajero a eliminar: ")
            if pila.eliminar_por_numero(num):
                print(f"  ✓ Pasajero {num} eliminado de la pila")
            else:
                print("  ❌ No se encontró el pasajero")
        elif op == "8":
            copia_pila = pila.copiar()
            print("  ✓ Copia realizada con éxito. Mostrando copia:")
            copia_pila.listar()
        elif op == "9":
            print(f"  Longitud: {pila.longitud()} | ¿Está vacía?: {'Sí' if pila.esta_vacia() else 'No'}")
        elif op == "C":
            cargados = 0
            for p in datos_prueba():
                if pila.apilar(p):
                    cargados += 1
            print(f"  ✓ Processados {cargados} datos de prueba")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("  ✓ Encolado: está al final")
        elif op == "2":
            cola.listar()
        elif op == "3":
            pasajero = cola.desencolar()
            if pasajero:
                print(f"  ✓ Salió del frente: {pasajero}")
            else:
                print("  ⚠ La cola está vacía")
        elif op == "4":
            frente = cola.ver_frente()
            if frente:
                print(f"  Frente actual: {frente}")
            else:
                print("  (cola vacía)")
        elif op == "5":
            num = leer_entero("  Ingrese n.º de pasajero a buscar: ")
            pos = cola.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en posición [{pos}]: {cola.datos[pos]}")
            else:
                print("  ❌ No existe")
        elif op == "6":
            num = leer_entero("  N.º de pasajero a modificar: ")
            if cola.buscar(num) != -1:
                dest = input("  Nuevo destino: ").strip()
                asiento = input("  Nuevo asiento: ").strip().upper()
                cola.modificar(num, dest, asiento)
                print("  ✓ Pasajero modificado")
            else:
                print("  ❌ Pasajero no encontrado")
        elif op == "7":
            num = leer_entero("  N.º de pasajero a eliminar: ")
            if cola.eliminar_por_numero(num):
                print(f"  ✓ Pasajero {num} eliminado de la cola")
            else:
                print("  ❌ No se encontró el pasajero")
        elif op == "8":
            copia_cola = cola.copiar()
            print("  ✓ Copia realizada con éxito. Mostrando copia:")
            copia_cola.listar()
        elif op == "9":
            print(f"  Longitud: {cola.longitud()} | ¿Está vacía?: {'Sí' if cola.esta_vacia() else 'No'}")
        elif op == "C":
            cargados = 0
            for p in datos_prueba():
                if cola.encolar(p):
                    cargados += 1
            print(f"  ✓ Procesados {cargados} datos de prueba")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()