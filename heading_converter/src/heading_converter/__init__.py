import sys
from pathlib import Path

def convert_presentation_to_article(content):
    """
    Convert presentation headings to article format by adding two levels
    to each heading (## to ####, # to ###, etc.)
    
    Args:
        content (str): The markdown content with presentation headings
        
    Returns:
        str: Content with adjusted heading levels
    """
    lines = content.split('\n')
    converted_lines = []
    
    for line in lines:
        # Check if line starts with markdown heading
        if line.strip().startswith('#'):
            # Count existing hash symbols
            hash_count = len(line) - len(line.lstrip('#'))
            # Get the heading text (everything after the hashes and space)
            heading_text = line.lstrip('#').lstrip()
            # Add two more levels (## becomes ####)
            new_line = '#' * (hash_count + 2) + ' ' + heading_text
            converted_lines.append(new_line)
        else:
            converted_lines.append(line)
    
    return '\n'.join(converted_lines)

def include_and_convert(file_path):
    """
    Include and convert a file for use in Quarto documents
    Similar to {{< include file.qmd >}} but with heading conversion
    
    Args:
        file_path (str): Path to the markdown file to include and convert
        
    Returns:
        str: Converted markdown content ready for inclusion
    """
    try:
        # Convert to Path object for better path handling
        path = Path(file_path)
        
        # Check if file exists
        if not path.exists():
            return f"<!-- Error: File {file_path} not found -->"
        
        # Read the file
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert headings and return
        converted_content = convert_presentation_to_article(content)
        
        # Add a comment to indicate the source
        header_comment = f"<!-- Content included and converted from {file_path} -->\n\n"
        
        return header_comment + converted_content
        
    except Exception as e:
        return f"<!-- Error processing {file_path}: {str(e)} -->"

# For direct use in Quarto code blocks
def process_file(file_path):
    """
    Process and print file content for Quarto code block execution
    
    Args:
        file_path (str): Path to the file to process
    """
    result = include_and_convert(file_path)
    print(result)

# Command line interface for external use
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python heading_converter.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    result = include_and_convert(file_path)
    print(result)

# Example usage functions for testing
def demo_usage():
    """
    Demonstrate how to use this in different ways
    """
    # Create a sample presentation file
    sample_content = """# My Presentation

## Introduction
Welcome to my talk

### Key Points
- Point 1
- Point 2

## Main Content
Here's the main content

### Details
Some detailed information

## Conclusion
Thank you for listening
"""
    
    # Save sample file
    with open('sample_presentation.qmd', 'w') as f:
        f.write(sample_content)
    
    print("Sample presentation content:")
    print(sample_content)
    print("\n" + "="*60 + "\n")
    
    print("Converted for article:")
    converted = include_and_convert('sample_presentation.qmd')
    print(converted)

if __name__ == "__main__" and len(sys.argv) == 1:
    # Run demo if no arguments provided
    demo_usage()