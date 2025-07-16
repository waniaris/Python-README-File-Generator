# from Week6 Rich exercise example, use PyInquirer instead of InquirerPy
from PyInquirer import prompt
from rich.console import Console  
from rich.progress import Progress
from rich.table import Table
import time

console = Console() #  initializing the Rich Console tool so it can be reused later

# Welcome message
console.print("[bold cyan]Hello! Please provide the details of your GitHub project.[/bold cyan]\n")

# Get user input for README file
def user_input():
    questions = [
        {
            'type': 'input', 
            'name': 'title', 
            'message': 'Project Title:'
        },
                {
            'type': 'input', 
            'name': 'description', 
            'message': 'Project Description:'
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
            'message': 'Contact Information:'}
    ]
    return prompt(questions)

# Get input by calling the function
user_answers = user_input()

# Info Received Message
console.print("\n[bold green] Thank you! Your project details have been collected.[/bold green]\n")

# Create a table to display project details using Rich
# from Week6 Rich exercise example

table = Table(title="Your Project Summary")

table.add_column("Project Info", style="bold cyan", justify="right")
table.add_column("Response", style="bold magenta")

# Fill table with info
table.add_row("Project Title", user_answers["title"])
table.add_row("Description", user_answers["description"])
table.add_row("Installation", user_answers["installation"])
table.add_row("Usage", user_answers["usage"])
table.add_row("License", user_answers["license"])
table.add_row("Author", user_answers["author"])
table.add_row("Contact", user_answers["contact"])

console.print(table)

# Show a progress bar
with Progress() as progress:
    task = progress.add_task("[yellow]Generating...", total=100)
    for _ in range(10):
        time.sleep(0.3)
        progress.update(task, advance=10)

# Success creation message
console.print("[bold green]README.md generation complete![/bold green] ✅")
