import nmap

def run(ip):
    try:
        nm = nmap.PortScanner()
        print("   ↳ [Nmap Pro] Escaneando puertos clave de infraestructura...")

        nm.scan(ip, '21,22,80,443,445,3389', arguments='-sV --version-intensity 3')

        if ip not in nm.all_hosts():
            return "[-] El objetivo no respondió (Host Down o bloquea pings)."

        resultados = []
        for proto in nm[ip].all_protocols():
            lport = sorted(nm[ip][proto].keys())
            for port in lport:
                estado = nm[ip][proto][port]['state']
                servicio = nm[ip][proto][port]['name']
                version = nm[ip][proto][port]['version']

                linea = f"Puerto {port}/{proto}: {estado} | Servicio: {servicio}"
                if version:
                    linea += f" (Versión: {version})"
                resultados.append(linea)

        return "\n".join(resultados) if resultados else "[-] No se encontraron puertos abiertos."
    except Exception as e:
        return f"[-] Error en Nmap Pro: {e}. Revisa si 'python-nmap' está instalado."
