import requests

def run(ip):
    try:
        # Intentamos conectar por HTTP y HTTPS
        url = f"http://{ip}"
        response = requests.get(url, timeout=3)
        server = response.headers.get('Server', 'Desconocido')
        return f"Servidor Web detectado. Código: {response.status_code}. Software: {server}"
    except Exception:
        return "No se detectó un servidor web activo en el puerto 80."