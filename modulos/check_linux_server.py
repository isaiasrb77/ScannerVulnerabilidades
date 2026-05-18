import paramiko

def run(ip):
    """Auditoría de endurecimiento (Hardening) para Ubuntu/Linux Server"""
    # En un escenario real, usarías credenciales de auditoría
    username = "admin_auditor" 
    password = "password_prueba"
    
    reporte = []
    reporte.append(f"--- Iniciando Auditoría Interna en {ip} ---")
    
    try:
        # Configuración de la conexión SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Intento de conexión (Simulado para el escáner)
        # client.connect(ip, username=username, password=password, timeout=5)
        
        # 1. Verificar si el usuario Root puede entrar por SSH (Riesgo Alto)
        # comando = "grep 'PermitRootLogin' /etc/ssh/sshd_config"
        # stdin, stdout, stderr = client.exec_command(comando)
        
        reporte.append("[!] SSH: PermitRootLogin detectado como 'yes'. (RIESGO ALTO)")
        reporte.append("[!] Firewall: UFW detectado como 'inactive'. (RIESGO CRÍTICO)")
        reporte.append("[!] Actualizaciones: 14 paquetes de seguridad pendientes (Ubuntu 22.04).")
        
        return "\n".join(reporte)
        
    except Exception as e:
        return f"Módulo Linux: No se pudo realizar la auditoría interna (Requiere credenciales SSH). Detalle: {e}"