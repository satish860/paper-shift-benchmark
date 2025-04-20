#!/usr/bin/env python
"""
CLI for converting PDF documents to Markdown using Paper Shift
"""

import argparse
import os
import sys
from typing import Optional

from papershift import convert_pdf_to_markdown


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert PDF documents to Markdown using Paper Shift"
    )
    
    # Required arguments
    parser.add_argument(
        "pdf_path", 
        help="Path to the PDF file to convert"
    )
    
    # Optional arguments
    parser.add_argument(
        "-o", "--output", 
        dest="output_path",
        help="Output file path for the markdown (default: same name as PDF with .md extension)"
    )
    parser.add_argument(
        "-d", "--output-dir", 
        dest="output_dir",
        help="Directory to save output files (default: current directory)"
    )
    parser.add_argument(
        "--dpi", 
        type=int, 
        default=300,
        help="DPI for PDF rendering (default: 300)"
    )
    parser.add_argument(
        "--target-height", 
        type=int, 
        default=2048,
        dest="target_height_px",
        help="Target height in pixels for rendered images (default: 2048)"
    )
    parser.add_argument(
        "--model", 
        default="openrouter/google/gemini-2.0-flash-001",
        help="Model to use for conversion (default: openrouter/google/gemini-2.0-flash-001)"
    )
    parser.add_argument(
        "--api-key", 
        dest="api_key",
        help="OpenRouter API key (can also be set via OPENROUTER_API_KEY environment variable)"
    )
    parser.add_argument(
        "--max-workers", 
        type=int, 
        default=4,
        dest="max_workers",
        help="Maximum number of worker threads (default: 4)"
    )
    parser.add_argument(
        "--batch-size", 
        type=int, 
        default=5,
        dest="batch_size",
        help="Batch size for processing (default: 5)"
    )
    parser.add_argument(
        "--fast", 
        action="store_true",
        dest="fast_mode",
        help="Enable fast mode for quicker processing"
    )
    
    return parser.parse_args()


def main():
    """Main entry point for the CLI."""
    args = parse_args()
    
    # Check if PDF file exists
    if not os.path.isfile(args.pdf_path):
        print(f"Error: PDF file not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)
    
    # Get API key from environment if not provided
    api_key = args.api_key or os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: API key is required. Provide it with --api-key or set OPENROUTER_API_KEY environment variable.", 
              file=sys.stderr)
        sys.exit(1)
    
    # Determine output path
    output_path = args.output_path
    if not output_path:
        base_name = os.path.splitext(os.path.basename(args.pdf_path))[0]
        output_dir = args.output_dir or os.getcwd()
        output_path = os.path.join(output_dir, f"{base_name}.md")
    
    # Convert PDF to markdown
    try:
        print(f"Converting {args.pdf_path} to markdown...")
        markdown_content = convert_pdf_to_markdown(
            pdf_path=args.pdf_path,
            output_dir=args.output_dir,
            dpi=args.dpi,
            target_height_px=args.target_height_px,
            model=args.model,
            api_key=api_key,
            max_workers=args.max_workers,
            batch_size=args.batch_size,
            fast_mode=args.fast_mode
        )
        
        # Save the output
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        print(f"Conversion complete! Markdown saved to: {output_path}")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
