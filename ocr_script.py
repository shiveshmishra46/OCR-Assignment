import pytesseract
import cv2
import json
import easyocr
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base, sessionmaker

# Database Configuration
DATABASE_URL = "postgresql://postgres:yourpassword@localhost:5432/ocr_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Database Model
class PatientData(Base):
    __tablename__ = 'forms_data'
    id = Column(Integer, primary_key=True)
    patient_name = Column(String, nullable=False)
    dob = Column(String, nullable=False)
    form_json = Column(JSON, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# OCR Function using Tesseract
def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

# EasyOCR Alternative
def extract_text_easyocr(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path, detail=0)
    return " ".join(result).strip()

# Process Image and Store in Database
def process_ocr(image_path):
    raw_text = extract_text_easyocr(image_path)  # Using EasyOCR

    ocr_data = {
        "text": raw_text  # Only extracted text is stored here
    }


    new_entry = PatientData(patient_name="John Doe", dob="01/05/1988", form_json=ocr_data)
    session.add(new_entry)
    session.commit()

    print(json.dumps(ocr_data, indent=4))  # Pretty Print Output
    return ocr_data


if __name__ == "__main__":
    image_path = "sample_form.jpg"  # Change this to actual image path
    process_ocr(image_path)
