import re
import pytesseract
from PIL import Image
import cv2
from datetime import datetime

# Optional: Path to your tesseract binary (Windows users)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_field(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else None

def process_receipt(image_path):
    # 1️⃣ Preprocess Image for better OCR
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    # 2️⃣ OCR - Extract text
    text = pytesseract.image_to_string(gray)

    # 3️⃣ Extract Fields
    parsed = {
        "bank": extract_field(r"(KCB|EQUITY|COOPERATIVE|ABSA|NCBA)", text),
        "date": extract_field(r"Date[:\s]+(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})", text),
        "amount": extract_field(r"Amount[:\s]+(?:KES|Ksh)?\s?([\d,]+(?:\.\d{1,2})?)", text),
        "accountNumber": extract_field(r"Account\s?(No|Number)[:\s]+(\d+)", text),
        "accountName": extract_field(r"Account\s?Name[:\s]+([A-Za-z\s]+)", text),
        "reference": extract_field(r"Reference[:\s]+([A-Z0-9]+)", text),
        "depositor": extract_field(r"Depositor[:\s]+([A-Za-z\s]+)", text)
    }

    # 4️⃣ Clean/Format Fields
    if parsed["amount"]:
        parsed["amount"] = float(parsed["amount"].replace(",", ""))
    if parsed["date"]:
        try:
            parsed["date"] = datetime.strptime(parsed["date"], "%d-%m-%Y").date().isoformat()
        except:
            pass  # leave as is if parsing fails

    return {"raw_text": text, "parsed": parsed}

# Example usage
if __name__ == "__main__":
    result = process_receipt("image.jpeg")
    print(result)
