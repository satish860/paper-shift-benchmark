# Paper Shift Benchmark

A command-line interface for converting PDF documents to Markdown using the Paper Shift library.

## Installation

```bash
# Using pip
pip install -e .

# Or using uv
uv install -e .
```

## Usage

The CLI provides a simple interface to the Paper Shift library's PDF to Markdown conversion functionality.

### Basic Usage

```bash
pdf-to-md path/to/your/document.pdf --api-key YOUR_API_KEY
```

You can also set your API key as an environment variable:

```bash
export OPENROUTER_API_KEY=your-api-key
pdf-to-md path/to/your/document.pdf
```

### Advanced Options

```bash
pdf-to-md path/to/your/document.pdf \
  --output custom_output.md \
  --output-dir output_folder \
  --dpi 300 \
  --target-height 2048 \
  --model openrouter/google/gemini-2.0-flash-001 \
  --api-key YOUR_API_KEY \
  --max-workers 4 \
  --batch-size 5 \
  --fast
```

### Command Line Options

- `pdf_path`: Path to the PDF file to convert (required)
- `-o, --output`: Output file path for the markdown (default: same name as PDF with .md extension)
- `-d, --output-dir`: Directory to save output files (default: current directory)
- `--dpi`: DPI for PDF rendering (default: 300)
- `--target-height`: Target height in pixels for rendered images (default: 2048)
- `--model`: Model to use for conversion (default: openrouter/google/gemini-2.0-flash-001)
- `--api-key`: OpenRouter API key (can also be set via OPENROUTER_API_KEY environment variable)
- `--max-workers`: Maximum number of worker threads (default: 4)
- `--batch-size`: Batch size for processing (default: 5)
- `--fast`: Enable fast mode for quicker processing