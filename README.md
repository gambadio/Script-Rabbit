# Script Rabbit

Script Rabbit is a desktop application for splitting large Word or PDF documents, processing them with the Anthropic API, and merging the resulting HTML files back into a single document. It is built with Python's `tkinter` library and organised into three main tools:

1. **Splitter** – breaks a document into chapters and saves them as individual `.docx` files.
2. **Processor** – sends each `.docx` to the Anthropic API using selectable prompts and saves the response as HTML.
3. **Merger** – combines multiple HTML files into one HTML file and optionally converts it to PDF.

The application stores temporary data about your last processed batch and can reload it automatically when you open the merger tab.

## Repository Contents

- `integrated_app.py` – assembles the splitter, processor and merger into a single `tkinter` interface.
- `main.py` – launches the application, applies theming and clears temporary data on start.
- `splitter.py` – handles document upload, chapter selection and file splitting. Supports DOCX and PDF (via conversion to DOCX).
- `processor.py` – communicates with the Anthropic API to convert DOCX sections into HTML using prompts. API keys are encrypted and stored in `config.json` using `encryption.key`.
- `merger.py` – merges HTML files and can generate a PDF using headless Chrome via Selenium.
- `default_prompts.py` – predefined prompts for the processor.
- `saved_prompts.json` – user‑saved prompts loaded by the processor.
- `temp_data.py` – stores metadata about the last processing batch.
- `config.json` and `encryption.key` – store the encrypted Anthropic API key.

## Requirements

This project depends on several third‑party packages including:

- `anthropic`
- `python-docx`
- `cryptography`
- `selenium` and `webdriver-manager`
- `pywin32` (for PDF to DOCX conversion on Windows)
- `sv_ttk`, `darkdetect` and `pywinstyles` for styling

Install the requirements with `pip`:

```bash
pip install anthropic python-docx cryptography selenium webdriver-manager pywin32 sv_ttk darkdetect pywinstyles
```

A local installation of Google Chrome is required for PDF generation.

## Usage

Run the application from the repository root:

```bash
python main.py
```

1. Use the **Splitter** tab to upload a DOCX or PDF file, adjust the chapter depth and split the document.
2. In the **Processor** tab, set your Anthropic API key, select a prompt and process the generated DOCX files.
3. Switch to the **Merger** tab to combine the processed HTML files and optionally create a PDF.

Processed files are saved under the `projects/` directory with a timestamped folder for each run.

## License

The project is released under the following terms:

> Permission is granted to use, copy and modify this software free of charge for **non‑commercial purposes only**. Any commercial use, distribution or sublicensing is expressly prohibited. This notice must be included in all copies or substantial portions of the software.

By using this repository you agree to these terms.

