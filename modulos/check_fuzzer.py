import requests

def run(objetivo):
    url = objetivo if objetivo.startswith("http") else f"http://{objetivo}"
    # Lista de archivos y rutas sensibles
    wordlist = ["admin", "config.php", "db.php", ".env", ".git", "backup", "v1/api"]
    encontrados = []
    
    for ruta in wordlist:
        try:
            res = requests.get(f"{url}/{ruta}", timeout=2)
            if res.status_code == 200:
                encontrados.append(f"/{ruta}")
        except:
            continue
            
    if encontrados:
        return f"📂 EXPOSICIÓN: Se encontraron rutas sensibles: {', '.join(encontrados)}"
    return "No se encontraron directorios sensibles comunes."