import socket

def run(ip):
    puerto = 3306 # Puerto estándar de MySQL/MariaDB
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, puerto))
    sock.close()
    
    if result == 0:
        return "🚨 BASE DE DATOS DETECTADA: Puerto 3306 (MySQL) abierto. Riesgo crítico de filtración de datos."
    return "Puerto 3306 (MySQL) cerrado."