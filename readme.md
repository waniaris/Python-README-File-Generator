# Python README File Generator

## Description

This project creates a `README.md` file for the user's GitHub repositories that is reusable. It prompts the user for details about their GitHub project using `InquirerPy`.

The application will then generate a `README.md` file in the parent directory using GitHub-flavored markdown.

The codes are organised using classes and modules. A `requirements.txt` file and a virtual environment are used, and instructions for setting up the project are also included.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/waniaris/Python-README-File-Generator
   ```
2. Navigate into the project directory::
   ```bash
   cd Python-README-File-Generator
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv myenv
   ```
4. Activate the virtual environment:
   ```bash
   # Windows:
   myenv\Scripts\activate
   
   # macOS/Linux:
   source myenv/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the script:
   ```bash
   pip install -r requirements.txt
   ```
7. Follow the steps in usage information below.

## Usage Information

1. Run the Python script to generate a README.md file:
    ```bash
    python main.py
    ```
3. The script will prompt the user for the following details regarding the user's project:

    - Title
    - Description
    - Installation Instructions
    - Usage Information
    - License
    - Author Name
    - Contact Information

4. After the user has provided the necessary inputs, the script will generate a README.md file in the parent directory.
5. The user can open the README.md file to check the generated content, which will follow GitHub-flavored markdown format.

## License
MIT

## Author Name
Wani Aris

## Contact Information
norhazwaniaris@gmail.com

## Useful Resources

- [Open sources licenses](https://choosealicense.com/licenses/) - An introduction to Test Driven Development.
- [InquirerPy Documentation](https://inquirerpy.readthedocs.io/en/latest/)
- [Rich Documentation](https://rich.readthedocs.io/en/latest/)
- [Using Rich for Beautiful Console Output](https://realpython.com/python-rich-module/)
