import socket

def run(ip):
    puerto = 22
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, puerto))
    sock.close()
    
    if result == 0:
        return "🐧 Puerto 22 (SSH) abierto. Común en servidores Linux. Verificar que no use contraseñas débiles."
    return "Puerto 22 (SSH) cerrado."