# To generate the readme.md file

def generate_readme_content(data):
    return f"""# {data['title']}

**Author:** {data['author']}  
**Contact:** {data['contact']}
     
## Project Description
{data['description']}

## Installation Instructions
{data['installation']}

## Usage Information
{data['usage']}

## License
This project is licensed under the {data['license']} license.

## Author
{data['author']}

## Contact
{data['contact']}
"""

def write_readme(content, filename="README.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
