import os
import sys
import importlib.util
from urllib.parse import urlparse

# Asegurar que el script reconozca el directorio raíz para importar desde 'core'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Importación segura del motor de inteligencia artificial desde la carpeta core
try:
    from core.ia_brain import identificar_con_ia
except ImportError:
    def identificar_con_ia(datos): return "[-] Error: No se pudo cargar el análisis analítico de IA."

def escanear_ip(ip, categoria="General"):
    """
    Orquesta la ejecución dinámica de todos los submódulos de escaneo.
    Normaliza el objetivo para limpiar protocolos web (http/https) si se ingresa una URL.
    """
    # Limpieza automática del objetivo para evitar fallos de socket (getaddrinfo failed)
    objetivo_limpio = ip.strip()
    if objetivo_limpio.startswith(("http://", "https://")):
        parsed_url = urlparse(objetivo_limpio)
        objetivo_limpio = parsed_url.netloc

    hallazgos = []
    ruta_modulos = os.path.join(BASE_DIR, "modulos")
    
    # Carga y ejecución dinámica de los scripts dentro de la carpeta 'modulos'
    if os.path.exists(ruta_modulos):
        for archivo in os.listdir(ruta_modulos):
            if archivo.endswith(".py") and archivo != "__init__.py":
                nombre_mod = archivo[:-3]
                try:
                    spec = importlib.util.spec_from_file_location(nombre_mod, os.path.join(ruta_modulos, archivo))
                    m = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(m)
                    
                    if hasattr(m, 'run'):
                        res = m.run(objetivo_limpio)
                        hallazgos.append((nombre_mod, res))
                except Exception as e:
                    hallazgos.append((nombre_mod, f"Error al ejecutar módulo: {e}"))

    # Envía la recopilación completa de datos al cerebro de IA para su filtrado lógico
    res_ia = identificar_con_ia(str(hallazgos))
    hallazgos.append(("Analisis_IA", res_ia))
    
    return hallazgos