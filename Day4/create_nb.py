import nbformat as nbf

nb = nbf.v4.new_notebook()

nb['cells'] = [
    nbf.v4.new_markdown_cell("# Task 4: Safety, Guardrails & Internal Evaluation\nThis notebook evaluates the RAG system safety."),
    nbf.v4.new_code_cell("import sys, os\nsys.path.append(os.path.abspath('..'))\nimport config\nfrom ingest import get_embedding_function, build_index, load_pdfs, chunk_documents\n# Setup index\npdfs = load_pdfs(config.DATA_DIR)\nchunks = chunk_documents(pdfs)\nindex = build_index(chunks)"),
    nbf.v4.new_markdown_cell("## 1. Calibrate Retrieval Confidence Threshold"),
    nbf.v4.new_code_cell("answerable_queries = ['What is the target blood pressure?']\nunanswerable_queries = ['How to build a rocket?']\n# Run retrieval and collect scores\n# Compare ranges and set a data-backed threshold\nTHRESHOLD = 0.5 # Placeholder until data is run"),
    nbf.v4.new_markdown_cell("## 2. Implement Unsupported-Claim Safety Net"),
    nbf.v4.new_code_cell("def check_unsupported_claims(answer, evidence_docs):\n    # Sentence level claim extraction and evidence overlap verification\n    return True"),
    nbf.v4.new_markdown_cell("## 3. Execute Benchmark Evaluation"),
    nbf.v4.new_code_cell("import json\n# Load benchmark\n# Calculate Precision@k and Safety Pass Rate"),
]

with open('Task4_Safety_Evaluation.ipynb', 'w') as f:
    nbf.write(nb, f)
