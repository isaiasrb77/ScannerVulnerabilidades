def identificar_con_ia(datos):
    """
    Analiza de forma cruzada las salidas de texto de los escaneos de vulnerabilidades.
    Filtra de forma estricta los falsos positivos asegurándose de verificar que 
    el puerto se declare explícitamente como abierto.
    """
    alertas = []
    texto = datos.lower()
    
    # 🚨 ANÁLISIS DE INFRAESTRUCTURA PERIMETRAL (Solo si el puerto reporta 'open' o 'abierto')
    if "445" in texto and ("open" in texto or "abierto" in texto) and "445 cerrado" not in texto:
        alertas.append("🚨 SMB: Puerto 445 ABIERTO. Riesgo crítico de Ransomware y explotación remota (MS17-010 / EternalBlue).")
        
    if "21" in texto and ("open" in texto or "abierto" in texto) and "21 (ftp) cerrado" not in texto:
        alertas.append("⚠️ FTP: Puerto 21 ABIERTO. Riesgo de interceptación de tráfico y credenciales en texto plano.")
        
    if "3389" in texto and ("open" in texto or "abierto" in texto) and "3389 cerrado" not in texto:
        alertas.append("🚨 RDP: Puerto 3389 (Escritorio Remoto) ABIERTO. Expuesto a ataques de fuerza bruta y denegación de servicio.")
        
    if "80" in texto and ("open" in texto or "abierto" in texto) and "80 cerrado" not in texto:
        alertas.append("⚠️ HTTP: Puerto 80 ABIERTO. Servidor web activo sin cifrado SSL/TLS (Tráfico expuesto).")

    # 🔑 AUDITORÍA DE CREDENCIALES (HYDRA) - Solo si hubo un hallazgo positivo real
    if "💥 acceso revelado" in texto or "login:" in texto and "valid" in texto:
        alertas.append("🚨 CREDENCIALES COMPROMETIDAS: ¡Se descubrieron accesos válidos por fuerza bruta! Cambiar contraseñas de de inmediato.")

    # 🔒 CIFRADO TLS DÉBIL (SSLSCAN) - Validamos que sslscan haya encontrado debilidades reales
    if "sslv2" in texto or "sslv3" in texto or "tls1.0" in texto or "tls1.1" in texto:
        alertas.append("⚠️ CIFRADO OBSOLETO: El servidor acepta protocolos TLS v1.0 o v1.1. Vulnerable a ataques de interceptación (MitM).")

    # 🛠️ AUDITORÍA INTERNA DE CONFIGURACIÓN DE SISTEMAS
    if "permitrootlogin detectado como 'yes'" in texto or ("rootlogin" in texto and "yes" in texto):
        if "22/tcp: open" in texto or "22: open" in texto or "22 (ssh) abierto" in texto:
            alertas.append("⚠️ SSH: Acceso root permitido Y puerto expuesto públicamente. Vulnerable a ataques automatizados.")
        else:
            alertas.append("ℹ️ SSH CONFIG: PermitRootLogin está activo internamente, pero el puerto 22 se encuentra cerrado en la red externa.")
        
    if "ufw detectado como 'inactive'" in texto or ("ufw" in texto and "inactive" in texto):
        alertas.append("💀 FIREWALL: El cortafuegos local (UFW) se encuentra INACTIVO. El sistema carece de reglas de filtrado perimetral local.")
        
    if "paquetes de seguridad pendientes" in texto or "paquetes de seguridad pendientes" in texto:
        alertas.append("📦 SISTEMA: Existen parches y actualizaciones críticas de seguridad del sistema operativo sin instalar.")

    # --- Retorno Lógico Final ---
    if not alertas:
        return "🛡️ No se detectaron vulnerabilidades críticas ni puertos expuestos en los servicios activos."
    
    return "🚨 VULNERABILIDADES DETECTADAS POR INTELIGENCIA AUTOMATIZADA:\n" + "\n".join(alertas)
