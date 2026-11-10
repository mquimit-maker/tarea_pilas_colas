from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def buscar(self, numero):
        """Búsqueda lineal del FRENTE al FINAL. Retorna la posición o -1."""
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def encolar(self, pasajero):
        """Agrega al final evitando duplicados por número."""
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        # Validación: no permitir números de pasajero repetidos
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        """Muestra la cola del FRENTE al FINAL."""
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    def desencolar(self):
        """Remueve y retorna el FRENTE corriendo todos a la izquierda."""
        if self.esta_vacia():
            return None
        primer_pasajero = self.datos[0]
        # Correr elementos a la izquierda (eliminar_por_posicion(0))
        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.cantidad -= 1
        self.datos[self.cantidad] = None
        return primer_pasajero

    def ver_frente(self):
        """Retorna el elemento en el FRENTE sin sacarlo."""
        if self.esta_vacia():
            return None
        return self.datos[0]

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        """Modifica destino y asiento buscando desde el frente."""
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        """Desencola y vuelve a encolar 'cantidad' veces para rotar la cola."""
        if self.esta_vacia():
            return False

        encontrado = False
        elementos_a_procesar = self.cantidad

        for _ in range(elementos_a_procesar):
            p = self.desencolar()
            if p.numero == numero:
                encontrado = True
                # No lo volvemos a encolar, así se elimina
            else:
                self.encolar(p)

        return encontrado

    def copiar(self):
        """Copia la cola conservando el orden de entrada."""
        nueva_cola = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva_cola.encolar(self.datos[i])
        return nueva_cola

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0