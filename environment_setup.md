# Environment Setup

These are the steps used to set up the environment for running the HEARTS Text Stereotype Detection project.

## 1. Clone the Repository
```bash
git clone https://github.com/OleinikovMV/HEARTS-Text-Stereotype-Detection.git
cd HEARTS-Text-Stereotype-Detection
```

## 2. Create and activate conda environment
```bash
conda create -n hearts_env python=3.11 -y
conda activate hearts_env
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Verify Installation
```bash
python -c "import torch, spacy; print(torch.__version__, spacy.__version__)"
```

## 5. Install spaCy Model
```bash
python -m spacy download en_core_web_sm
```

Environment setup tested on commit: `3cbeabb30e3589723bbb1d81ff1d728d9b85ffaa`.

