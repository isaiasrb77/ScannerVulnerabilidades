import subprocess

def run(ip):
    print("   ↳ [SSLScan Pro] Evaluando cifrado y certificados en puerto 443...")
    try:
        # Ejecuta sslscan ocultando los intentos fallidos para dejar limpio el reporte
        comando = ["sslscan", "--no-failed", f"{ip}:443"]
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=30)

        if resultado.returncode == 0 and resultado.stdout.strip():
            return resultado.stdout.strip()
        return "[-] El puerto 443 (HTTPS) no respondió a cifrados SSL/TLS."
    except FileNotFoundError:
        return "[-] sslscan no está instalado en este sistema Kali."
    except Exception as e:
        return f"[-] Error al analizar SSL/TLS: {e}"
