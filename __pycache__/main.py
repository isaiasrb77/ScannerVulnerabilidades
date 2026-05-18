import os
import sys
import importlib.util
from urllib.parse import urlparse  # Permite limpiar URLs completas automáticamente

# Asegurar que main también reconozca la raíz para llegar a 'core'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Importaciones de tus archivos en la carpeta core
try:
    from core.ia_brain import identificar_con_ia
except ImportError:
    # Si falla, definimos una función interna para que no se detenga
    def identificar_con_ia(datos): return "Análisis IA no disponible."

def escanear_ip(ip, categoria="General"):
    # 🎯 NORMALIZACIÓN DEL OBJETIVO:
    # Convierte entradas como 'https://sitio.com/reto1.html' en 'sitio.com'
    # Si es una dirección IP válida, se mantiene intacta.
    objetivo_limpio = ip.strip()
    if objetivo_limpio.startswith(("http://", "https://")):
        parsed_url = urlparse(objetivo_limpio)
        objetivo_limpio = parsed_url.netloc

    hallazgos = []
    ruta_modulos = os.path.join(BASE_DIR, "modulos")
    
    if os.path.exists(ruta_modulos):
        # Recorre todos los archivos en la carpeta 'modulos'
        for archivo in os.listdir(ruta_modulos):
            if archivo.endswith(".py") and archivo != "__init__.py":
                nombre_mod = archivo[:-3]
                try:
                    # Carga dinámica del módulo
                    spec = importlib.util.spec_from_file_location(nombre_mod, os.path.join(ruta_modulos, archivo))
                    m = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(m)
                    
                    # Ejecuta la función run() pasándole el host ya procesado y limpio
                    if hasattr(m, 'run'):
                        res = m.run(objetivo_limpio)
                        hallazgos.append((nombre_mod, res))
                except Exception as e:
                    hallazgos.append((nombre_mod, f"Error al ejecutar: {e}"))

    # Análisis de los resultados usando el "cerebro" de IA
    res_ia = identificar_con_ia(str(hallazgos))
    hallazgos.append(("Analisis_IA", res_ia))
    
    return hallazgos