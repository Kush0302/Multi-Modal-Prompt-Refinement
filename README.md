# Multi-Modal Prompt Refinement System

## Overview
This project implements a system that accepts multi-modal inputs (text, images, and documents) and refines them into a standardized structured prompt format suitable for downstream AI processing.

## Supported Input Types
- Plain text files (.txt)
- Images (.jpg, .png) – simulated OCR
- Documents (.pdf) – simulated parsing

## System Workflow
1. Detect input file type
2. Extract raw text (simulated where necessary)
3. Refine extracted data into structured prompt
4. Validate relevance and reject irrelevant inputs
5. Output standardized JSON prompt

## Folder Structure

```text
project-root/
├── input_samples/      # Raw input files
├── output_prompts/     # Refined prompt outputs
├── utils.py            # Extraction & refinement logic
└── main.py             # Orchestration logic

