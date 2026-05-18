import socket

def run(ip):
    # Chequeo básico del puerto SMB (445)
    puerto = 445
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, puerto))
    sock.close()
    
    if result == 0:
        return "⚠️ Puerto 445 (SMB) ABIERTO. Se recomienda verificar vulnerabilidad MS17-010 (EternalBlue)."
    return "Puerto 445 cerrado."