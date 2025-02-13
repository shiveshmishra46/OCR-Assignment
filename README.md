<<<<<<< HEAD
# OCR-Assignment
=======
# OCR Assignment

## 📌 Overview
This project extracts text from scanned patient forms using OCR, structures it into JSON, and stores it in a PostgreSQL database.

## 🛠️ Setup Instructions
Follow these steps to set up and run the project.

### 1️⃣ **Clone the repository**
```bash
git clone <your-repo-link>
cd OCR-Assignment
```

### 2️⃣ **Create a virtual environment**
```bash
python -m venv ocr_env
source ocr_env/bin/activate  # For Mac/Linux
ocr_env\Scripts\activate  # For Windows
```

### 3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Setup Database**
Ensure that PostgreSQL is running and then execute:
```bash
psql -U postgres -d ocr_db -f database_schema.sql
```

### 5️⃣ **Run the script**
```bash
python ocr_script.py
```

---

## 📦 Sample JSON Output
```json
{
    "text": "Extracted text from OCR here..."
}
```

---

## 📂 Project Structure
```
/OCR-Assignment
 ├── ocr_script.py          # Main Python Script
 ├── requirements.txt       # Dependencies
 ├── database_schema.sql    # SQL Schema
 ├── sample_form.jpg        # Sample Test Image
 ├── README.md              # Project Documentation
```

---

## 📌 Author Shivesh Mishra **

