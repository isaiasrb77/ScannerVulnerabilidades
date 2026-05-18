import socket

def run(ip):
    # Puertos comunes: MySQL (3306), SQL Server (1433), PostgreSQL (5432)
    puertos = [3306, 1433, 5432]
    encontrados = []
    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, puerto))
        if result == 0:
            encontrados.append(f"Puerto {puerto} ABIERTO")
        sock.close()
    
    return "\n".join(encontrados) if encontrados else "No se detectaron bases de datos expuestas."