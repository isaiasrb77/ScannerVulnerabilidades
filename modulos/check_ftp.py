import socket

def run(ip):
    puerto = 21
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, puerto))
        
        if result == 0:
            # Intentamos leer el banner para ver la versión
            sock.send(b"QUIT\r\n")
            banner = sock.recv(1024).decode(errors='ignore').strip()
            sock.close()
            return f"⚠️ FTP DETECTADO: {banner}. Riesgo de transferencia de datos en texto plano."
        sock.close()
        return "Puerto 21 (FTP) cerrado."
    except:
        return "No se pudo determinar el estado del FTP."