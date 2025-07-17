# Reference: Week 6, Rich exercise

from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
import time

# class Project:
#     def __init__(self, age, height=0):
#         self.name = name
#         self.age = age
#         self.height = 0

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")


console = Console()  # Initialize the Rich Console tool

# Welcome message
console.print("[bold cyan]Hello! Please provide the details of your GitHub project.[/bold cyan]\n")

# Get user input for README file
def input():
    questions = [
        {
            'type': 'input', 
            'name': 'title', 
            'message': 'Title:'
        },
                {
            'type': 'input', 
            'name': 'description', 
            'message': 'Description:'
        },
        {
            'type': 'input', 
            'name': 'installation', 
            'message': 'Installation Instructions:'
        },
        {
            'type': 'input', 
            'name': 'usage', 
            'message': 'Usage Information:'
        },        
        {
            'type': 'list', 
            'name': 'license', 
            'message': 'Choose a license:', 
            'choices': ['MIT', 'Apache 2.0', 'Boost Software', 'None'] # reference: https://choosealicense.com/licenses/
        },
        {
            'type': 'input', 
            'name': 'author', 
            'message': 'Author Name:'
        },
        {
            'type': 'input', 
            'name': 'contact', 
            'message': 'Contact:'
        }
    ]
    return prompt(questions)

# Get input by calling the function
answers = input()

# Info Received Message
console.print("\n[bold green]Thank you! Your project details have been collected.[/bold green]\n")

# Create a table to display project details using Rich
table = Table(title=answers["title"])

table.add_column("Project Info", style="bold cyan", justify="right")
table.add_column("Response", style="bold magenta")

# Fill table with info
table.add_row("Description", answers["description"])
table.add_row("Installation", answers["installation"])
table.add_row("Usage", answers["usage"])
table.add_row("License", answers["license"])
table.add_row("Author", answers["author"])
table.add_row("Contact", answers["contact"])

console.print(table)

# Show a progress bar
with Progress() as progress:
    task = progress.add_task("[yellow]Generating...", total=100)
    for _ in range(10):
        time.sleep(0.3)
        progress.update(task, advance=10)

# README content
content = f"""# {answers['title']}

**Author:** {answers['author']}  
**Contact:** {answers['contact']}

## Description
{answers['description']}

## Installation
{answers['installation']}

## Usage
{answers['usage']}

## License
{answers['license']}

"""

# with open("README.md", "w") as file:
#     file.write(content)w

# console.print("[bold green]README.md generation complete![/bold green] ✅")

try:
    with open("README.md", "w") as file:
        file.write(content)
        
    # Success creation message
    console.print("[bold green]README.md generation complete![/bold green] ✅")

except Exception as e:
    console.print(f"[bold red]Failed to write README.md: {e}[/bold red]")