import socket

def run(ip):
    puerto = 3389
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, puerto))
    sock.close()
    
    if result == 0:
        return "⚠️ ALERTA: Escritorio Remoto (RDP) detectado. Posible vector de acceso no autorizado."
    return "Servicio RDP no detectado."