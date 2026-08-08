import sys
import os
from google.cloud import vision
from fpdf import FPDF
from compliance_engine import ComplianceEngine
from config import ASSETS_DIR, REPORTS_DIR

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "MaanakAI Compliance Audit", ln=True, align='C')

    def generate(self, filename, results, extracted, output_path):
        self.add_page()
        
        # 1. Add Image
        if os.path.exists(filename):
            try:
                self.image(filename, x=55, y=25, w=100)
                self.ln(90) 
            except Exception as e:
                print(f"Could not add image: {e}")
        
        # 2. Header
        self.set_font("helvetica", 'B', 16)
        self.cell(0, 10, "MaanakAI Compliance Report", ln=True, align='C')
        self.ln(5)

        # 3. Status Table
        self.set_font("helvetica", 'B', 12)
        for key, status in results.items():
            display_key = key.replace('_', ' ').upper()
            self.cell(0, 10, f"{display_key} | {status}", ln=True)
        
        self.ln(10)

        # 4. Raw Data Section
        self.set_font("helvetica", '', 10)
        for key, value in extracted.items():
            self.cell(0, 8, f"{key.upper()}: {value}", ln=True)
            
        self.ln(10)
        
        # 5. Disclaimer
        self.set_font("helvetica", 'I', 8)
        self.cell(0, 10, "DISCLAIMER: Automated AI Audit. Verify against official FSSAI regulations.", ln=True)
            
        # 6. Save
        self.output(output_path)
        return output_path

def get_ocr_text(image_path):
    client = vision.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    response = client.text_detection(image=vision.Image(content=content))
    return response.text_annotations[0].description if response.text_annotations else ""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main_orchestrator.py <image_filename>")
        sys.exit(1)

    image_name = sys.argv[1]
    img_path = os.path.join(ASSETS_DIR, image_name)
    
    if not os.path.exists(img_path):
        print(f"Error: Could not find image at {img_path}")
        sys.exit(1)

    raw_text = get_ocr_text(img_path)
    res, data = ComplianceEngine().validate(raw_text)
    
    report_filename = f"{os.path.splitext(image_name)[0]}_final_report.pdf"
    output_path = os.path.join(REPORTS_DIR, report_filename)
    
    pdf = PDFReport()
    path = pdf.generate(img_path, res, data, output_path)
    
    print(f"Audit Complete. Report generated: {path}")