import os
import sys
from datetime import datetime

# Rutas del sistema
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    from main import escanear_ip
except ImportError as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*55)
    print(f"🛡️  MISCANNER PRO v2.1 | {datetime.now().strftime('%d/%m/%Y')}")
    print("="*55)
    
    target = input("\n🎯 Objetivo (IP o URL): ")
    if not target: return

    print(f"\n[+] Auditoría en progreso para: {target}...")
    
    try:
        # Ejecutamos el escaneo
        resultados = escanear_ip(target, "Completa")
        
        # Generar nombre: Reporte_192_168_0_9_20260512_1430.txt
        fecha_id = datetime.now().strftime("%Y%m%d_%H%M")
        limpiar_nombre = target.replace(".", "_").replace(":/", "").replace("/", "_")
        nombre_archivo = f"Reporte_{limpiar_nombre}_{fecha_id}.txt"
        
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(f"REPORTE TÉCNICO DE CIBERSEGURIDAD\n")
            f.write(f"OBJETIVO: {target}\n")
            f.write(f"FECHA: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*55 + "\n")
            
            for mod, res in resultados:
                f.write(f"\n[MÓDULO: {mod.upper()}]\n{res}\n")
                f.write("-" * 40 + "\n")
                
        print(f"\n✅ ESCANEO FINALIZADO")
        print(f"📄 Reporte guardado: {nombre_archivo}")
        
    except Exception as e:
        print(f"❌ Error durante el escaneo: {e}")

if __name__ == "__main__":
    menu()