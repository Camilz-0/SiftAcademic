import logging
import os
import time

# CONFIGURACIÓN DE LOGS 
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s — [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# LÓGICA DEL PROYECTO 
class SiftAcademic:
    def __init__(self, thesis_topic):
        self.thesis_topic = thesis_topic
        logging.info(f"SiftAcademic inicializado con el tema: '{thesis_topic}'")

    def extract_text(self, document_name):
        logging.info(f"Iniciando extracción de texto del archivo: {document_name}")
        # Simulación extracción de texto
        if ".pdf" not in document_name:
            logging.error(f"Error: El archivo {document_name} no es un formato válido.")
            return None
        
        logging.info(f"Archivo '{document_name}' procesado con éxito.")
        return "Texto académico simulado para análisis"

    def analyze_compatibility(self, doc_text):
        logging.info("Calculando compatibilidad semántica...")
        # Simulación cálculo de coseno (match_score)
        match_score = 0.85 
        logging.info(f"Análisis completado. Puntaje de relevancia: {match_score * 100}%")
        return match_score

# EJECUCIÓN DEL FLUJO 
if __name__ == "__main__":
    # Configuración del usuario
    mi_proyecto = SiftAcademic(thesis_topic="Inteligencia Artificial en la Educación")
    
    # Paso 1: Extracción
    contenido = mi_proyecto.extract_text("tesis_final.pdf")
    
    # Paso 2: Análisis
    if contenido:
        puntaje = mi_proyecto.analyze_compatibility(contenido)
        print(f"Proyecto SiftAcademic — Análisis finalizado. Puntaje: {puntaje*100}%")