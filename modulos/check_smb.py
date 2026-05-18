import socket

def run(ip):
    puerto = 445
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, puerto))
    sock.close()
    
    if result == 0:
        return "⚠️ ALERTA: Puerto 445 (SMB) ABIERTO. Riesgo de exploits de red y Ransomware."
    return "Puerto 445 (SMB) cerrado o protegido."