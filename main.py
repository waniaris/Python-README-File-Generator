from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
import time


class ProjectPrompt:
    """Handles user input for GitHub project details."""

    def __init__(self):
        self.questions = [
            {"type": "input", "name": "title", "message": "Project Title:"},
            {"type": "input", "name": "description", "message": "Project Description:"},
            {"type": "input", "name": "installation", "message": "Installation Instructions:"},
            {"type": "input", "name": "usage", "message": "Usage Information:"},
            {
                "type": "list",
                "name": "license",
                "message": "Choose a license:",
                "choices": ["MIT", "Apache 2.0", "Boost Software", "None"]
            },
            {"type": "input", "name": "author", "message": "Author Name:"},
            {"type": "input", "name": "contact", "message": "Email:"}
        ]
        self.answers = {}

    def collect(self):
        """Prompt the user and store the answers."""
        self.answers = prompt(self.questions)
        return self.answers

if __name__ == "__main__":
    # Initialize Rich console
    console = Console()

    # Welcome message
    console.print("[bold cyan]Hello! Please provide the details of your GitHub project.[/bold cyan]\n")

    # Collect input
    project = ProjectPrompt()
    answers = project.collect()

    # Display confirmation
    console.print("\n[bold green]Thank you! Your project details have been collected.[/bold green]\n")

    # Create Rich table summary
    table = Table(title=answers["title"])
    table.add_column("Project Info", style="bold cyan", justify="right")
    table.add_column("Response", style="bold magenta")

    # Display answers in console
    project_info = [
        ("description", "Description"), ("installation", "Installation"),
        ("usage", "Usage"), ("license", "License"),
        ("author", "Author"), ("contact", "Contact")
    ]
    for key, label in project_info:
        table.add_row(label, answers[key])
        console.print(table)

    # Build README content
    content = f"""# {answers['title']}

## Description
{answers['description']}

## Installation
{answers['installation']}

## Usage
{answers['usage']}

## License
{answers['license']}

## Author
{answers['author']}

## Contact
{answers['contact']}
"""
    
    # Separate content into lines
    lines = content.strip().splitlines()
    total_lines = len(lines)

    # Show progress bar
    try:
        with Progress() as progress:
            task = progress.add_task("[cyan]Writing to readme.md...", total=total_lines)

            with open("README.md", "w") as file:
                for line in lines:
                    file.write(line + "\n")
                    time.sleep(0.1)
                    progress.update(task, advance=1)

        console.print("[bold green]README.md generation complete![/bold green] ✅")

    except Exception as e:
        console.print(f"[bold red]README.md generation failed! {e}[/bold red]")
