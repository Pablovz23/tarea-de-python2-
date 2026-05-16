from abc import ABC, abstractmethod

# Interfaz para los que van a recibir alertas
class IObservador(ABC):
    @abstractmethod
    def actualizar(self):
        pass

# Sujeto que sera vigilado
class Servidor:
    def init(self):
        self.__observadores = [] # Lista privada de servicios
        self.__estado = True     # True = Online, False = Caido

    def enlazar(self, observador):
        self.__observadores.append(observador)

    def cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado
        # Si el estado es False (se cae), avisa a todos
        if not self.__estado:
            print("\n--- SERVIDOR CAIDO ---")
            for obs in self.__observadores:
                obs.actualizar()

# Observador 1
class AlertaEmail(IObservador):
    def actualizar(self):
        print("[Email]: Alerta enviada al administrador.")

# Observador 2
class SistemaReinicio(IObservador):
    def actualizar(self):
        print("[Reinicio]: Intentando levantar el sistema...")

# Prueba corta
server = Servidor()
server.enlazar(AlertaEmail())
server.enlazar(SistemaReinicio())

# Simulamos la caida del servidor
server.cambiar_estado(False)