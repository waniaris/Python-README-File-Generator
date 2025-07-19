from rich.progress import Progress
import time
import os

def write_file(lines):
    status = False

    total_lines = len(lines)

    # Show progress bar
    try:
        # Get the parent directory (one level up)
        parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        # Define the file path in the parent directory
        file_path = os.path.join(parent_dir, "README.md")

        with Progress() as progress: 
            task = progress.add_task("[cyan]Writing to README.md...", total=total_lines)

            # Create and write to the file
            with open(file_path, "w") as file:
                for line in lines:
                    file.write(line + "\n")
                    time.sleep(0.1)
                    progress.update(task, advance=1)

        print(f"File created at: {file_path}")
        status = True

    except Exception as e:
        status = False
    
    return status
 
        #  with Progress() as progress: 
        #     task = progress.add_task("[cyan]Writing to readme.md...", total=total_lines)

        #     with open("README.md", "w") as file:
        #         for line in lines:
        #             file.write(line + "\n")
        #             time.sleep(0.1)
        #             progress.update(task, advance=1)