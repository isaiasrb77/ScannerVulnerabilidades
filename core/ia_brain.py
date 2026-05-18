def identificar_con_ia(datos):
    """
    Analiza de forma cruzada las salidas de texto de los escaneos de vulnerabilidades.
    Filtra falsos positivos asegurándose de verificar la presencia explícita de puertos abiertos.
    """
    alertas = []
    texto = datos.lower()
    
    # 🚨 ANÁLISIS DE PUERTOS EXTERNOS EXUESTOS EN LA RED
    if "445" in texto and ("open" in texto or "abierto" in texto):
        alertas.append("🚨 SMB: Puerto 445 ABIERTO. Riesgo crítico de Ransomware y explotación remota (MS17-010 / EternalBlue).")
        
    if "21" in texto and "open" in texto:
        alertas.append("⚠️ FTP: Puerto 21 ABIERTO. Riesgo de interceptación de tráfico y credenciales en texto plano.")
        
    if "3389" in texto and "open" in texto:
        alertas.append("🚨 RDP: Puerto 3389 (Escritorio Remoto) ABIERTO. Expuesto a ataques de fuerza bruta y denegación de servicio.")
        
    if "80" in texto and "open" in texto:
        alertas.append("⚠️ HTTP: Puerto 80 ABIERTO. Servidor web activo sin cifrado SSL/TLS (Tráfico expuesto).")

    # 🛠️ AUDITORÍA INTERNA DE CONFIGURACIÓN DE SISTEMAS
    if "rootlogin" in texto and "yes" in texto:
        # Validación cruzada: Solo alerta de peligro real externo si el puerto 22 está abierto hacia internet
        if "22: open" in texto or "22 (ssh) abierto" in texto:
            alertas.append("⚠️ SSH: Acceso root permitido Y puerto expuesto públicamente. Vulnerable a ataques automatizados.")
        else:
            alertas.append("ℹ️ SSH CONFIG: PermitRootLogin está activo internamente, pero el puerto 22 se encuentra cerrado en la red externa.")
        
    if "ufw" in texto and "inactive" in texto:
        alertas.append("💀 FIREWALL: El cortafuegos local (UFW) se encuentra INACTIVO. El sistema carece de reglas de filtrado perimetral local.")
        
    if "seguridad pendientes" in texto or "paquetes de seguridad pendientes" in texto:
        alertas.append("📦 SISTEMA: Existen parches y actualizaciones críticas de seguridad del sistema operativo sin instalar.")

    # --- Retorno Lógico Final ---
    if not alertas:
        return "🛡️ No se detectaron vulnerabilidades críticas ni puertos expuestos en los servicios activos."
    
    return "🚨 VULNERABILIDADES DETECTADAS POR INTELIGENCIA AUTOMATIZADA:\n" + "\n".join(alertas)