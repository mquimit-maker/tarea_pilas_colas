from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el único que se ve y el único que sale)
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def buscar(self, numero):
        """Búsqueda lineal del TOPE al FONDO. Retorna la posición o -1."""
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def apilar(self, pasajero):
        """Agrega al tope evitando duplicados por número."""
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        # Validación: no permitir números de pasajero repetidos
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        """Muestra la pila del TOPE al FONDO."""
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    def desapilar(self):
        """Remueve y retorna el TOPE."""
        if self.esta_vacia():
            return None
        self.cantidad -= 1
        pasajero = self.datos[self.cantidad]
        self.datos[self.cantidad] = None
        return pasajero

    def ver_tope(self):
        """Retorna el elemento en el TOPE sin sacarlo."""
        if self.esta_vacia():
            return None
        return self.datos[self.cantidad - 1]

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        """Modifica destino y asiento de un pasajero buscando desde el tope."""
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        """Desapila a una Pila Auxiliar hasta hallarlo, lo descarta y regresa el resto."""
        if self.esta_vacia():
            return False

        pila_aux = MiPila(self.capacidad)
        encontrado = False

        # Desapilar hacia la auxiliar
        while not self.esta_vacia():
            p = self.desapilar()
            if p.numero == numero:
                encontrado = True
                break
            pila_aux.apilar(p)

        # Regresar los elementos a la pila original manteniendo el orden
        while not pila_aux.esta_vacia():
            self.apilar(pila_aux.desapilar())

        return encontrado

    def copiar(self):
        """Copia la pila apilando de abajo hacia arriba (0 a cantidad-1)."""
        nueva_pila = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva_pila.apilar(self.datos[i])
        return nueva_pila

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0