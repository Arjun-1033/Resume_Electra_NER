# Resume NER using ELECTRA

This project demonstrates an end-to-end Resume Named Entity Recognition (NER)
pipeline using the ELECTRA model.

## Pipeline Overview
- Resume text extraction
- Manual annotation using Doccano
- IOB / CoNLL conversion
- ELECTRA model fine-tuning
- Evaluation using Precision, Recall, and F1-score
- Inference on new resumes

## Tech Stack
- Python
- Hugging Face Transformers
- ELECTRA
- PyTorch
- Datasets
- seqeval
- Doccano

## Project Structure

RESUME_ELECTRA_NER/
├── conversion/
│   └── convert.py
├── data/
│   ├── Annotated/
│   │   └── admin.json
│   ├── pre_annotated/
│   │   └── preannotation_doccano.json
│   ├── processed/
│   │   └── resumes.json
│   └── raw/
│       └── resumes.bio.conll
├── notebook/
│   ├── 1_resume_parser.ipynb
│   ├── 2_pre_annotation.ipynb
│   ├── 3_doccano_setup.ipynb
│   └── 4_trainin_1.ipynb
├── requirements.txt
├── README.md
└── .gitignore


## Sample Data Notice
This repository uses synthetic and anonymized sample resumes.
No real personal or client data is included.

## How to Run
1. Install dependencies  
   pip install -r requirements.txt
2. Run notebooks in order (1 → 4)

## use the convet.py for converting the export_doccano.jsonl into .conll file format

## Team Members
- Arjun M
- Shijin KC
