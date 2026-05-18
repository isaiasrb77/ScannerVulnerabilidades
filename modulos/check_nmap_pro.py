import nmap

def run(ip):
    try:
        nm = nmap.PortScanner()
        # Escaneamos puertos clave: 21(FTP), 22(SSH), 80(HTTP), 443(HTTPS), 445(SMB), 3389(RDP)
        nm.scan(ip, '21,22,80,443,445,3389', arguments='-sV')
        
        if ip not in nm.all_hosts():
            return "El objetivo no respondió (Host Down)."
        
        resultados = []
        for proto in nm[ip].all_protocols():
            lport = nm[ip][proto].keys()
            for port in lport:
                estado = nm[ip][proto][port]['state']
                servicio = nm[ip][proto][port]['name']
                version = nm[ip][proto][port]['version']
                resultados.append(f"Puerto {port}: {estado} | Servicio: {servicio} | Versión: {version}")
        
        return "\n".join(resultados) if resultados else "No se encontraron puertos abiertos comunes."
    except Exception as e:
        return f"Error en Nmap: Instala Nmap en tu PC o revisa la librería. Detalle: {e}"