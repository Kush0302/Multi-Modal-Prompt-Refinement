import os
import json
from utils import(
    get_file_type,
    read_text_file,
    simulate_image_extraction,
    simulate_document_extraction,
    refine_to_prompt,
    is_relevant
)

INPUT_DIR="input_samples"
OUTPUT_DIR="output_prompts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_file(filename):
    filepath = os.path.join(INPUT_DIR, filename)
    file_type = get_file_type(filename)

    extracted_text = ""

    if file_type == "text":
        extracted_text = read_text_file(filepath)

    elif file_type == "image":
        extracted_text = simulate_image_extraction(filename)

    elif file_type == "document":
        extracted_text = simulate_document_extraction(filename)

    else:
        return None
    
    intent, requirements, outputs = refine_to_prompt(extracted_text)

    if not is_relevant(intent, requirements, outputs):
        return {
            "intent": {"summary": ""},
            "functional_requirements": [],
            "expected_outputs": []
        }

    return {
        "intent": {"summary": intent},
        "functional_requirements": requirements,
        "expected_outputs": outputs
    }

def main():
    for filename in os.listdir(INPUT_DIR):
        refined_prompt = process_file(filename)

        if refined_prompt is None:
            continue

        output_filename = filename.split(".")[0] + ".json"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(refined_prompt, f, indent=4)

        print(f"Processed: {filename}")


if __name__ == "__main__":
    main()
