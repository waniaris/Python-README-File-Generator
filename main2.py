# Reference: Week 6, Rich exercise
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from prompts import user_input
import time

class Project:
    def __init__(self, title, description, installation, 
                 usage, license, author, contact):
        self.title = title
        self.description = description
        self.installation = installation
        self.usage = usage
        self.license = license
        self.author = author
        self.contact = contact

    # def display(self):
    #     print(f"Name: {self.name}, Age: {self.age}")

if __name__ == "__main__":

    console = Console()  # Initialize the Rich Console tool

    # Welcome message
    console.print("[bold cyan]Hello! Please provide the details of your GitHub project.[/bold cyan]\n")


    # Get input by calling the function
    answers = user_input()

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

    try:
        with open("README.md", "w") as file:
            file.write(content)
            
        # Success creation message
        console.print("[bold green]README.md generation complete![/bold green] ✅")

    except Exception as e:
        console.print(f"[bold red]Failed to write README.md: {e}[/bold red]")