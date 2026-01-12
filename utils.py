import os

def get_file_type(filename): #Determine input type based on file extension
    if filename.endswith(".txt"):
        return "text"
    elif filename.endswith((".jpg", ".png", ".jpeg")):
        return "image"
    elif filename.endswith(".pdf"):
        return "document"
    else:
        return "unknown"


def read_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def simulate_image_extraction(filename): #Simulates OCR text extraction from an image file
    return "Dashboard Login User Profile"


def simulate_document_extraction(filename): #Simulates text extraction from a document file
    #simulated document parsing
    return "Project online platform features deliverables"


def refine_to_prompt(extracted_text): #Converts extracted text into a structured prompt.
    extracted_text = extracted_text.lower()

    intent = ""
    requirements = []
    outputs = []

    if "dashboard" in extracted_text:
        intent = "Build a dashboard system"
        outputs.append("Dashboard UI")

    if "login" in extracted_text:
        requirements.append("User authentication")

    if "user profile" in extracted_text or "profile" in extracted_text:
        requirements.append("User profile management")

    if "deliverables" in extracted_text:
        outputs.append("Final project documentation")

    return intent, requirements, outputs


def is_relevant(intent, requirements, outputs):
    return bool(intent or requirements or outputs)
