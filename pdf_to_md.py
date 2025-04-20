#!/usr/bin/env python
"""
Simple script to convert PDF to Markdown using Paper Shift
"""

import os
import sys
from papershift import convert_pdf_to_markdown

def main():
    # Check if PDF path is provided
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_md.py <pdf_path> [output_path]")
        sys.exit(1)
    
    # Get PDF path from command line argument
    pdf_path = sys.argv[1]
    
    # Check if PDF file exists
    if not os.path.isfile(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)
    
    # Get API key from environment variable
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable is not set")
        sys.exit(1)
    
    # Determine output path
    output_path = None
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = f"{base_name}.md"
    
    # Convert PDF to markdown
    try:
        print(f"Converting {pdf_path} to markdown...")
        markdown_content = convert_pdf_to_markdown(
            pdf_path=pdf_path,
            api_key=api_key
        )
        
        # Save the output
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        print(f"Conversion complete! Markdown saved to: {output_path}")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
