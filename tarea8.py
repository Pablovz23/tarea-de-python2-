
from abc import ABC, abstractmethod
NIVELES = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
def requiere_autorizacion(func):
    def wrapper(self, nivel, mensaje, usuario_autorizado=False):
        if not usuario_autorizado:
            print(f" [BLOQUEADO]: Sin autorización para: '{mensaje}'")
            return
        return func(self, nivel, mensaje, usuario_autorizado)
    return wrapper
class LoggerBase(ABC):
    @abstractmethod
    def registrar(self, nivel, mensaje, usuario_autorizado=False):
        pass
class LogConsola(LoggerBase):
    def __init__(self, nivel_activo):
        self.__nivel_activo = nivel_activo.upper()

    @requiere_autorizacion
    def registrar(self, nivel, mensaje, usuario_autorizado=False):
        nivel = nivel.upper()
        posicion_mensaje = NIVELES.index(nivel)
        posicion_activa = NIVELES.index(self.__nivel_activo)
        if posicion_mensaje < posicion_activa:
            print(f" [{nivel} Omitido]: Por debajo del nivel activo ({self.__nivel_activo}).")
        else:
            print(f" [{nivel}]: {mensaje}")
if __name__ == "__main__":
    logger = LogConsola(nivel_activo="WARNING")
    logs = [
        ("DEBUG", "Cargando configuración...", True),  
        ("INFO", "Usuario conectado.", True),       
        ("WARNING", "Poco espacio en disco.", True),  
        ("ERROR", "Conexión perdida.", False),     
        ("CRITICAL", "Sistema caído.", True)    
    ]
    for nivel, mensaje, autorizado in logs:
        logger.registrar(nivel, mensaje, usuario_autorizado=autorizado)