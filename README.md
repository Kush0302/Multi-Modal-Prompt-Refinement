# Multi-Modal Prompt Refinement System

## Overview
This project implements a system that accepts multi-modal inputs (text, images, and documents) and refines them into a standardized structured prompt format suitable for downstream AI processing.

## Supported Input Types
- Plain text files (.txt)
- Images (.jpg, .png)  
- Documents (.pdf)

## System Workflow
1. Detect input file type
2. Extract raw text (simulated where necessary)
3. Refine extracted data into structured prompt
4. Validate relevance and reject irrelevant inputs
5. Output standardized JSON prompt

## Folder Structure

```text
project-root/
├── input_samples/        # Raw input files
├── output_prompts/       # Refined prompt outputs
├── README.md             # Project overview
├── explanation.md        # Detailed design and reasoning
├── main.py               # Orchestration logic
├── prompt_template.json  # Prompt schema
├── requirements.txt      # Dependencies
├── utils.py              # Extraction and refinement logic
```

How the Prototype Works

This is a command-line prototype.

Steps to Run
1. Place input files inside input_samples/
2. Run the program:
```
python main.py
```
3. Refined prompts are generated inside output_prompts/
