import requests

def run(objetivo):
    # Definimos payloads clásicos para causar errores de sintaxis SQL
    payloads = ["'", '"', "';--", "admin'--"]
    hallazgos = []
    
    # Si el objetivo es una IP, intentamos tratarla como web
    url = objetivo if objetivo.startswith("http") else f"http://{objetivo}"
    
    try:
        # Probamos en un parámetro genérico '?id='
        for p in payloads:
            test_url = f"{url}/index.php?id={p}" 
            res = requests.get(test_url, timeout=3)
            
            # Firmas de errores de bases de datos comunes
            errors = [
                "mysql_fetch_array()", "you have an error in your sql syntax",
                "warning: mysql", "pg_query()", "oracle error"
            ]
            
            for error in errors:
                if error in res.text.lower():
                    return f"⚠️ POSIBLE SQLi: Error de sintaxis detectado con payload [{p}]"
        
        return "No se detectaron indicios de SQL Injection (basado en errores)."
    except Exception:
        return "Servicio web no disponible para pruebas de SQLi."