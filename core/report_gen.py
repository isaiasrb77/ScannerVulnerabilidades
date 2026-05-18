from fpdf import FPDF

def generar_pdf(objetivo, hallazgos):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"REPORTE TECNICO: {objetivo}", ln=True, align='C')
    pdf.ln(10)
    
    for mod, res in hallazgos:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"Modulo: {mod.upper()}", ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 5, txt=str(res))
        pdf.ln(5)
    
    pdf.output("Reporte_Escaneo.pdf")